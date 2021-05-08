<a name='API'></a>
## API
In order to deploy my model, I have to wrap it into unified application programming interfaces (APIs) and put them into Docker images.
I use [FastAPI](https://fastapi.tiangolo.com/) for the API implementation and this FastAPI friendly [docker image](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker).

<a name='Algorithms and untitest'></a>
##  Algorithms and untitest
The Algorithms are implemented in the `/assignment/main.py` and following that the `unittesting` are written. The algorithms are implemented in the specified paths and can interact with an API.
Honestly, I did not fully understand the purpose of benchmarking function. So, I felt a little bit freedom in implementing that functionality and only implemented the average and standard deviation of the results when random list are feeded into the `naive` and `efficient` functions

<a name='Django'></a>
## Django
For the front-end application I have used Django. For running the web application you just need to be in the assignment folder and while being in the virtual environnement run:
 ```
 pip install django
 pipenv shell
 pyhton manage.py runserver
 ```
 Then, in your browser, you can open the local link to the website.
 The [front-end](http://127.0.0.1:8000/optimize/) contains a table that compared the performance of Naive and Efficient algorithms for finding the maximum value for different value of `K`.


<a name='docker'></a>
## Docker
In order to put the API into a complete black box, I need to build a docker image with it. The following paragraphs tell you how to create it, then run and test it, and finally stop/remove it. 

Before we build our docker image, let's assert that the folder structure is correct.
The API has to be implemented in the `assignment/main.py` file, while the `Dockerfile` is in the root (parent) folder.
