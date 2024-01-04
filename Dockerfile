# pull base image
FROM python:3.10.12

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUBUFFERED 1

# setup working directory
WORKDIR /code

# copy requirement files
COPY Pipfile Pipfile.lock /code/

# install pipenv and requirements
RUN pip install pipenv && pipenv install --system

# copy project files
COPY . /code/



