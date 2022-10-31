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
  
Selected libraries: spaCy, The Natural Language Toolkit (NLTK)

- Step 2: Clustering
  
Topic modeling: latent Dirichlet allocation or LDA (being tested, promising)
  
K-means clustering (current results disappointing; to be tested using better embedding algorithm)

- Step 3*: build a recommendation system to suggest the highest matching expert(s) for each request
  
*Outside the scope of this project

**Illustrative and simplified example**: 

<img width="978" alt="image" src="https://user-images.githubusercontent.com/110877253/193379527-7296c4f7-3378-47bd-ba65-24d9af4380c6.png">

</p>
</details>
  
<details><summary>Data + Model</summary>
<p>

**Data:**

- Did exploratory data analysis (EDA) on two datasets from Kaggle:

  - Annotated Corpus for Named Entity Recognition | Kaggle 

<img width="980" alt="image" src="https://user-images.githubusercontent.com/110877253/193379601-9c6982a3-232f-4d94-9bc5-c5d03c66de6b.png">

</p>
</details>
  
**Model:**  
  
<img width="896" alt="image" src="https://user-images.githubusercontent.com/110877253/198972012-401a7fb3-8ca7-4d9e-bfe0-20d4fd62e7d2.png">

<img width="901" alt="image" src="https://user-images.githubusercontent.com/110877253/198972194-675e8692-ca98-48ff-b10d-61d684c3a051.png">

  
</p>
</details>
  
<details><summary>Where we're going (Demo)</summary>
<p>

<img width="935" alt="image" src="https://user-images.githubusercontent.com/110877253/198973272-2981e3c2-9df9-4085-8138-8c2259595022.png">
  
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

MIT License.
  
</p>
</details>
