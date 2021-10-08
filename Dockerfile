# get the official python image
FROM python:3.9

# disable buffering to write to logs instantly
ENV PYTHONUNBUFFERED 1

# set the working directory
RUN mkdir -p /alpha-app
WORKDIR /alpha-app

# install the dependencies
COPY Pipfile Pipfile.lock /alpha-app/
RUN pip install pipenv && pipenv install --ignore-pipfile --system

# copy the code to WD
COPY . /alpha-app/
