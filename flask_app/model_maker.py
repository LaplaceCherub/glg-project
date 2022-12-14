# Imports
import pandas as pd
import string
import spacy
from spacy.tokens import Doc
from nltk import WordNetLemmatizer
from xgboost import XGBClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import pickle
import nltk
from nltk.corpus import stopwords 
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from gensim.corpora.dictionary import Dictionary 
from gensim import models 
from sentence_transformers import SentenceTransformer

import os
ROOT_DIR = os.path.dirname(__file__)

# NER model
ner_df = pd.read_csv(os.path.join(ROOT_DIR, '../datasets/extended_df.csv'))
ner_df.drop(columns=['Unnamed: 0'], inplace=True)
ner_df['Sentence #'] = ner_df['Sentence #'].str.replace('Sentence: ','')
ner_df['Sentence #'].fillna(method='ffill', inplace=True)
ner_df['Sentence #'] = ner_df['Sentence #'].astype('int64')

sentence_df = ner_df.groupby('Sentence #', as_index=False)['Word'].apply(lambda x:x.str.cat(sep=' '))

nlp = spacy.load('en_core_web_sm')
def sentence_preprocessor(df):
    return_list = []
    for sentence in range(df['Sentence #'].max()):
        words = nlp(Doc(nlp.vocab, df[df['Sentence #'] == sentence + 1].Word.values))
        for word in words:
            # print(word)
            word_base = word
            word_lemma = word.lemma_
            word_pos = word.pos_
            word_tag = word.tag_
            word_dep = word.dep_
            word_length = len(word)
            word_capitalization = str(word)[0].isupper()
            word_punctiation = str(word).isalnum()
            word_stop = word.is_stop
            is_ner = str(word) in set(ent.text for ent in words.ents)
            return_list.append((word_base, word_lemma, word_pos, word_tag, word_dep, word_length, word_capitalization, word_punctiation, word_stop, is_ner))
    return return_list

df_list = sentence_preprocessor(ner_df)
intermediate_df = pd.DataFrame(df_list, columns=['WordBase', 'WordLemma', 'WordPOS', 'WordTag', 
    'WordDep', 'WordLength', 'IsCapitalized', 'NonPunctuation', 'IsStop', 'PossibleNER'])

X_train = intermediate_df[:835700]
X_test = intermediate_df[835700:]
y_train = ner_df.IsNER[:835700]
y_test = ner_df.IsNER[835700:]

xgb_model = XGBClassifier(random_state=42)

categorical_cols = ['WordLemma', 'WordPOS', 'WordTag', 'WordDep']
numerical_cols = ['IsCapitalized', 'NonPunctuation', 'IsStop', 'PossibleNER', 'WordLength']

numerical_transformer = SimpleImputer(strategy='constant')

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])


pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                            ('xgb_model', xgb_model)
                            ])

pipeline.fit(X_train, y_train) 

pickle.dump(pipeline, open(os.path.join(ROOT_DIR, 'ner_model.pkl'), 'wb'))

# LDA model
ner_dataset = pd.read_csv(os.path.join(ROOT_DIR, '../datasets/ner_dataset.csv'), 
    encoding='latin1')

ner_dataset['Sentence #'] = ner_dataset['Sentence #'].str.replace('Sentence:', '')
ner_dataset = ner_dataset.fillna(method='ffill')

ner_dataset['Sentence #'] = ner_dataset['Sentence #'].astype(int)

sentences_df = ner_dataset.groupby('Sentence #', as_index=False)['Word'].apply(lambda x: x.str.cat(sep=' '))
sentences_df = sentences_df.rename(columns={'Word': 'Sentences'})

sentences_df = sentences_df.drop(labels=[8411], axis=0)
sentences_df = sentences_df.reset_index()
sentences_df = sentences_df.drop(columns='index')

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

def _lemmatize_words(sentence):
    wordnet_map = {'N':wordnet.NOUN, 'V':wordnet.VERB, 'J':wordnet.ADJ, 'R':wordnet.ADV}
    pos_tagged_text = nltk.pos_tag(sentence.split())
    return ' '.join([WordNetLemmatizer().lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN))
                    for word, pos in pos_tagged_text])
    
def lda_sent_process(text):
    text = text.lower()  
    PUNCT_TO_REMOVE = string.punctuation
    text = text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))
    STOPWORDS = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in STOPWORDS])
    text = _lemmatize_words(text)
    return text.split()

sentences_df['lda_sents'] = sentences_df['Sentences'].apply(lambda x: lda_sent_process(x))

dct = Dictionary(sentences_df['lda_sents'])
corpus = [dct.doc2bow(sentence) for sentence in sentences_df['lda_sents']]
lda = models.LdaModel(corpus, num_topics=15, random_state=36)

with open(os.path.join(ROOT_DIR, 'dct.pkl'), 'wb') as pickle_dict: 
  pickle.dump(dct, pickle_dict)
with open(os.path.join(ROOT_DIR, 'lda.pkl'), 'wb') as pickle_lda:
  pickle.dump(lda, pickle_lda)

# Transformer model

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(sentences_df['Sentences'])

from sklearn.neighbors import NearestNeighbors 
nbrs = NearestNeighbors(n_neighbors=3, algorithm='ball_tree').fit(embeddings)

with open(os.path.join(ROOT_DIR, 'emb_model.pkl'), 'wb') as pickle_emb:
  pickle.dump(model, pickle_emb)
with open(os.path.join(ROOT_DIR, 'knn_model.pkl'), 'wb') as pickle_knn:
  pickle.dump(nbrs, pickle_knn)
