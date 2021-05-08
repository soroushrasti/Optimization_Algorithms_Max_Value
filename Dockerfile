#load an appropaorate image file for fastAPI
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

#copy files/folders
COPY ./assignment /assignment
COPY ./requirements.txt /requirements.txt

#install dependencies
RUN pip install -r /requirements.txt

WORKDIR /assignment

#unit test
CMD python -m unittest main.py
#run django server
RUN pipenv shell
CMD pyhton manage.py runserver