FROM python:3.10-buster

RUN mkdir /home/map
WORKDIR /home/map

ENV POETRY_HOME=/opt/poetry

RUN apt-get update
RUN apt-get install --no-install-recommends -y curl git build-essential
RUN pip install poetry
RUN poetry config virtualenvs.create false
