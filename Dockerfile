FROM python:3.8-slim-buster

RUN mkdir -p /app
WORKDIR /app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

ENV PIPENV_VENV_IN_PROJECT=1

COPY . .

RUN pip install --upgrade pipenv

RUN pipenv sync

CMD ["pipenv", "run", "start"]