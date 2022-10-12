# 🚀 [GLG](https://glginsights.com/) project

## A match made in machine learning heaven: 🙋 ➡️ 🤓 linking every request to the best expert
### 👏  By [Cris Fortes](https://www.linkedin.com/in/crisfortes/), [Ying Hu](https://www.linkedin.com/in/ying-hu-math/) and [Cody McCormack](https://www.linkedin.com/in/codymccormack/)

<details><summary>Context</summary>
<p>

Cris, Ying and Cody are students of [FourthBrain's](https://fourthbrain.ai/) [Machine Learning Engineer course](https://fourthbrain.ai/courses/machine-learning-engineer/), cohort 9 (August-December 2022). This repository (repo) is part of our capstone project, a required deliverable from our curriculum. For that we've chosen to work on the [GLG](https://glginsights.com/) project.

</p>
</details>
  
<details><summary>The problem</summary>
<p>

[GLG](https://glginsights.com/)'s business largely revolves around matching clients, requesting insights on a specific topic, with an expert on that topic from their large database so that they can meet by phone, video or in person. Visually: 

<img width="977" alt="image" src="https://user-images.githubusercontent.com/110877253/193379391-7bc81c97-fa89-4553-92d3-d62eaab639e1.png">

Since [GLG](https://glginsights.com/) receives 100s of these requests per day, how can they leverage machine learning to semi-automate the matching process at scale? 

</p>
</details>
  
<details><summary>The solution</summary>
<p>
  
Natural Language Processing (NLP), consisting of three steps:

- Step 1:  Named-Entity Recognition (NER)
  
Possible libraries: spaCy, The Natural Language Toolkit (NLTK), TensorFlow, Keras

- Step 2: Hierarchical clustering
  
Under consideration: decision tree, K-means clustering, Latent Dirichlet allocation (LDA)

- Step 3*: build a recommendation system to suggest the highest matching expert(s) for each request
  
*Outside the scope of this project

**Illustrative and simplified example**: 

<img width="978" alt="image" src="https://user-images.githubusercontent.com/110877253/193379527-7296c4f7-3378-47bd-ba65-24d9af4380c6.png">

</p>
</details>
  
<details><summary>Where we've been</summary>
<p>

**Data:**

- Did exploratory data analysis (EDA) on two datasets from Kaggle:

  - Annotated Corpus for Named Entity Recognition | Kaggle 

<img width="980" alt="image" src="https://user-images.githubusercontent.com/110877253/193379601-9c6982a3-232f-4d94-9bc5-c5d03c66de6b.png">

</p>
</details>
  
<details><summary>Where we're going</summary>
<p>

**Next step:** train our model using this other 2.7-million news articles dataset:

- [ ] All the News 2.0 - Components

- [ ] [PLACEHOLDER: Establish baseline model through AutoML or a pre-trained model + Document performance report in markdown]
  
NER (Named-Entity Recognition), the below tests are underway with the following preliminary results:
  
- Test 1, using spaCY predictions: 
  
Accuracy: 0.937, Recall: 0.619, Precision: 0.753, F1 Score: 0.680
  
- Test 2, lemmatization before vectorization:
  
XGB with one-hot encoding: Accuracy: 0.945, Recall: 0.906, Precision: 0.685, F1 Score: 0.780
  
Logistic Regression with one-hot encoding: Accuracy: 0.936, Recall: 0.901, Precision: 0.644, F1 Score: 0.751
  
Test 3, TPOT for AutoML: 
  
- forthcoming
  
Clustering, the below model has proven to be much better than baseline whose silhouette coefficient was less than 0.1:
  
- Model 1: CountVectorizer with tokenizer=LemmaTokenizer() + KMeans
  
    When n_cluster=2, Silhouette Coefficient is 0.28244613563900284 for random_states=1, 5, 10, 42
  
    When n_cluster=3, Silhouette Coefficient is 0.17099173313074406 for random_states=0, 1

- [ ] Starting to develop a web app in Flask

</p>
</details> 

<details><summary>Data and model iteration</summary>
<p>

- [ ] [PLACEHOLDER: Document performance, interpretation, and learnings in markdown]

- [ ] [PLACEHOLDER:Document limitations of your model / data / ML pipeline]

- [ ] [PLACEHOLDER: Restructure GitHub into scripts / modules / submodules]

- [ ] [PLACEHOLDER: Ensure that instructors can easily follow your README.md instructions to deploy your demo locally and in the cloud.]

</p>
</details>
  
<details><summary>MLE Stack</summary>
<p>

- [ ] [Exploratory Data Analysis & Wrangling, Experimentation, Data Engineering Pipeline, Machine Learning Pipeline, Deployment Pipeline]

- [ ] [Maybe consider: Feature Store, Metadata store, Model registry, Model serving, Model Monitoring]

</p>
</details>

<details><summary>Conclusions</summary>
<p>

Forthcoming.
  
</p>
</details>

<details><summary>Future work</summary>
<p>

Forthcoming.  
  
</p>
</details>

<details><summary>Authors and acknowledgment</summary>
<p>
  
Forthcoming.

</p>
</details>

<details><summary>License</summary>
<p>

Forthcoming.
  
</p>
</details>
