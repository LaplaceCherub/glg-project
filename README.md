# 🚀 [GLG](https://glginsights.com/) project

## A match made in machine learning heaven: 🙋 ➡️ 🤓 linking every request to the best expert
### 👏  By [Ying Hu](https://www.linkedin.com/in/ying-hu-math/), [Cody McCormack](https://www.linkedin.com/in/codymccormack/), and [Cris Fortes](https://www.linkedin.com/in/crisfortes/)

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
  
<p>  
  
**Model:** 
  
<img width="896" alt="image" src="https://user-images.githubusercontent.com/110877253/198972012-401a7fb3-8ca7-4d9e-bfe0-20d4fd62e7d2.png">

</p>
  
<img width="901" alt="image" src="https://user-images.githubusercontent.com/110877253/198972194-675e8692-ca98-48ff-b10d-61d684c3a051.png">

</p>
</details>
  
<details><summary>Where we're going (Demo)</summary>  
<p>
  
</p>
  
<img width="933" alt="image" src="https://user-images.githubusercontent.com/110877253/198979120-3143b81d-5f78-445c-9711-9bbaa3fa9c1b.png">
  
</p>
</details>
  
<details><summary>MLE Stack</summary>
<p>

- [ ] [Exploratory Data Analysis & Wrangling, Experimentation, Data Engineering Pipeline, Machine Learning Pipeline, Deployment Pipeline]

- [ ] [Maybe consider: Feature Store, Metadata store, Model registry, Model serving, Model Monitoring]
  
<img width="950" alt="image" src="https://user-images.githubusercontent.com/110877253/198978730-a0fca69c-f7ac-4b2a-8f24-d6890834f86b.png">


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

<details><summary>Deployment Instructions</summary>
<p>This app can be (relatiely, see note below) easily deployed using Docker. The instructions to deploy in the cloud or locally are the same.</p>
<ol>
  <li>Clone this repository, either on a local machine or in a cloud instance</li>
  <li>Navigate to the flask_app folder</li>
  <li>Build the Docker image, using the command <code>docker build -t image_name .</code></li>
    <ul>
      <li>If you don't have Docker installed locally or in the cloud instance, you will have to <a href="https://docs.docker.com/get-docker/">install</a> and activate the Daemon in order to build a Docker image.</li>
    </ul>
</ol>
</details>
