import pandas as pd
import spacy

nlp = spacy.load('en_core_web_sm')

def sentence_preprocessor(text):
    return_list = []
    words = nlp(text)
    for word in words:
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
        return_list.append((word_base, word_lemma, word_pos, word_tag, word_dep, 
        word_length, word_capitalization, word_punctiation, word_stop, is_ner))
    
    columns=['WordBase', 'WordLemma', 'WordPOS', 'WordTag', 'WordDep', 'WordLength', 
            'IsCapitalized', 'NonPunctuation', 'IsStop', 'PossibleNER']

    intermediate_df = pd.DataFrame(return_list, columns=columns)

    return return_list, intermediate_df