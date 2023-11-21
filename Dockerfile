FROM python:3.11

WORKDIR /my_project

COPY ./requirements.txt /my_project/

RUN pip install -r /my_proj/requirements.txt

COPY . .