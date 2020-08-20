# pull official base image
FROM python:3.8.0-alpine
# set work directory
RUN mkdir /code
WORKDIR /code
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add build-base postgresql-dev gcc openssl-dev libffi-dev python3-dev python-dev 
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /code/
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
RUN pip install -r requirements.txt
# copy project
COPY . /code/
EXPOSE 5000