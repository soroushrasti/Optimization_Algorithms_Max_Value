#load an appropaorate image file for fastAPI
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

#copy files/folders
COPY ./assignment /assignment
COPY ./requirements.txt /requirements.txt

#install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /assignment

#unit test
CMD python -m unittest main.py
#run django server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
