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

<img width="977" alt="image" src="https://user-images.githubusercontent.com/110877253/193379391-7bc81c97-fa89-4553-92d3-d62eaab639e1.png">

Since [GLG](https://glginsights.com/) receives 100s of these requests per day, how can they leverage machine learning to semi-automate the matching process at scale? 

</p>
</details>
  
<details><summary>The solution</summary>
<p>
<p>

<img width="883" alt="image" src="https://user-images.githubusercontent.com/110877253/204224020-1b5d9761-2d18-46be-a0bb-70bcb5578d28.png">

</p>
</details>
  
<details><summary>Data + Model</summary>
<p>
<p>

<img width="882" alt="image" src="https://user-images.githubusercontent.com/110877253/204224541-f62ca332-91a4-48d8-9d54-c8af127f503a.png">

</p>
</details>
  
<details><summary>Demo</summary>  
<p>
<p>
  
<img width="898" alt="image" src="https://user-images.githubusercontent.com/110877253/204224828-08ba6492-71c0-4862-a877-74cec80ffb34.png">
  
</p>
</details>
  
<details><summary>MLE Stack</summary>
<p>
<p>

<img width="880" alt="image" src="https://user-images.githubusercontent.com/110877253/204225162-fcec11aa-0059-4674-b18b-a749cf36cad4.png">
</p>
  
</p>
</details>

<details><summary>Conclusions</summary>
<p>

- Natural Language Processing (NLP) models work!

- Any NLP model is only as good as the data it was trained on

- Quickly jumping into the web app (Flask), even before the NLP models were working properly, was the right thing to do (MVP mindset)

- Seeing a live, working, deployed model that addresses a real business problem is priceless 

</p>
</details>

<details><summary>Future work</summary>
<p>

- Training our NLP models on larger and more diverse datasets should yield better results. For example, using this other 2.7-million news articles dataset: [All the News 2.0 - Components](https://components.one/datasets/all-the-news-2-news-articles-dataset/)

- Adapting our models to cover non-English languages would come in handy (GLG also has offices in Europe, Asia, Japan and the Middle East)

- Building a GLG topic expert(s) recommendation model with input from our NLP models would be a natural next step for this project

</p>
</details>

<details><summary>License</summary>
<p>

MIT License

Copyright (c) 2022 Cody

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

<details><summary>Deployment Instructions</summary>
<p>

This app can be (relatively, see note below) easily deployed using Docker. The instructions to deploy in the cloud or locally are the same.</p>
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
<p><strong>NOTE:</strong> This application depends on prebuilt machine learning models that were saved using <a href="https://docs.python.org/3/library/pickle.html">Pickle</a> files. The idea of Pickle files is that they can be built once and ported to any other machine. However, in testing we found that this was often not the case. If the app crashes when you try to run it, this is most likely the problem, and you need to take the steps below to remediate the issue:</p>
<ol>
  <li><a href="https://www.python.org/downloads/">Install Python</a> in the environment you're using, if you haven't already</li>
  <li>Install the requirements.txt file in the flask_app folder using the command <code>pip install -r requirements.txt</code> in the terminal</li>
  <li>Run the model_maker.py file with the command <code>python model_maker.py</code></li>
</ol>
<p>This will create new Pickle files in your environment. You can then follow the original steps above.</p>
</details>
