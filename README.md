# 🚀 [GLG](https://glginsights.com/) project

## A match made in machine learning heaven: 🙋 ➡️ 🤓 linking every request to the best expert
### 👏  By [Ying Hu](https://www.linkedin.com/in/ying-hu-math/), [Cody McCormack](https://www.linkedin.com/in/codymccormack/) and [Cris Fortes](https://www.linkedin.com/in/crisfortes/)

<details><summary>Context</summary>
<p>

Ying, Cody and Cris are students of [FourthBrain's](https://fourthbrain.ai/) [Machine Learning Engineer course](https://fourthbrain.ai/courses/machine-learning-engineer/), cohort 9 (August-December 2022). This repository (repo) is part of our capstone project, a required deliverable from our curriculum. For that we've chosen to work on the [GLG](https://glginsights.com/) project.

</p>
</details>
  
<details><summary>The problem</summary>
<p>

[GLG](https://glginsights.com/)'s business largely revolves around matching clients, requesting insights on a specific topic, with an expert on that topic from their large database so that they can meet by phone, video or in person. Visually: 

<img width="733" alt="image" src="https://user-images.githubusercontent.com/110877253/205419935-651c3d3a-972e-471f-9491-45c6426184f2.png">

Since [GLG](https://glginsights.com/) receives 100s of these requests per day, how can they leverage machine learning to semi-automate the matching process at scale? 

</p>
</details>
  
<details><summary>The solution</summary>
<p>
<p>

<img width="771" alt="image" src="https://user-images.githubusercontent.com/110877253/205419962-7316d77d-e5e6-483d-b20c-3716ce63db3a.png">

</p>
</details>
  
<details><summary>Data + Model</summary>
<p>
<img width="769" alt="image" src="https://user-images.githubusercontent.com/110877253/205420317-415e5226-3067-4b37-83e1-25c0a22cca56.png">
</p>
<p></p>
</details>
  
<details><summary>Demo</summary>  
<p>
<p>
<img width="771" alt="image" src="readme_assets/demo.gif">
</p>
<p>To see a longer demo, <a href="readme_assets/demo.mp4">click here.</a></p>
</details>
  
<details><summary>MLE Stack</summary>
<p>
<p>
<img width="771" alt="image" src="https://user-images.githubusercontent.com/110877253/205420458-fe94240c-7393-42d0-b976-29787fa5640d.png">
  
</p>
</details>

<details><summary>Future work</summary>
<p>

1. Improve the Topic Modeling: 
- Training an LDA model on a more diverse [dataset](https://components.one/datasets/all-the-news-2-news-articles-dataset/)
- Using semi-supervised learning method (SentenceTransformers + Label Propagation)

2. Expand the scope of the project: 
- Building the expert(s) recommendation model 
- Adapting our models to cover non-English languages 
  (GLG also has offices in Europe, Asia, and the Middle East)

</p>
</details>

<details><summary>Deployment Instructions</summary>
<p>

This app can be (relatively, see note 1 below) easily deployed using Docker. The instructions to deploy in the cloud or locally are the same.</p>
<ol>
  <li>Clone this repository, either on a local machine or in a cloud instance</li>
  <li>Navigate to the flask_app folder</li>
  <li>Build the Docker image, using the command <code>docker build -t image_name .</code></li>
    <ul>
      <li>If you don't have Docker installed locally or in the cloud instance, you will have to <a href="https://docs.docker.com/get-docker/">install</a> and <a href="https://docs.docker.com/config/daemon/systemd/">activate</a> the Daemon in order to build a Docker image.</li>
    </ul>
  <li>Run the Docker image using the command <code>docker run -d --rm --name container_name -p 8000:8000 image_name</code></li>
  <li>Navigate to either your local host, port 8000, or the public IP of the cloud instance, port 8000. E.g. 127.0.0.0:8000</li>
</ol>
<p><strong>NOTE 1:</strong> This application depends on prebuilt machine learning models that were saved using <a href="https://docs.python.org/3/library/pickle.html">Pickle</a> files. The idea of Pickle files is that they can be built once and ported to any other machine. However, in testing we found that this was often not the case. If the app crashes when you try to run it, this is most likely the problem, and you need to take the steps below to remediate the issue:</p>
<ol>
  <li>Open Dockerfile, and remove the <code>#</code> from the 3rd line from the bottom, so that it reads <code>RUN python model_maker.py</code></li>
</ol>
<p>Then you can pick up from the step <code>docker build -t image_name .</code> above.</p>
<p><strong>NOTE 2:</strong> this will slow down the Docker image build considerably, and might take up to 20 minutes, depending on your machine.</p>
</details>

<details><summary>License</summary>
<p>

MIT License

Copyright (c) 2022 Cody McCormack, Cris Fortes and Ying Hu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
  
</p>
</details>
