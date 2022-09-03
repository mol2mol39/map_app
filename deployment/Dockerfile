FROM python:3.10-buster

RUN mkdir /home/map
WORKDIR /home/map

ENV POETRY_HOME=/opt/poetry

RUN apt-get update
RUN apt-get install --no-install-recommends -y curl git build-essential
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY map/poetry.lock map/pyproject.toml ./
RUN poetry install

CMD ["uvicorn", "src.schema:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]