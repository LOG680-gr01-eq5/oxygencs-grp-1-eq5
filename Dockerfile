FROM python:3.8-slim

# Met à jour les paquets et installe les dépendances nécessaires pour pipenv
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

WORKDIR /app

COPY . .

RUN pipenv install --deploy --ignore-pipfile
RUN pipenv run test
RUN pipenv run lint
RUN pipenv run format

CMD ["pipenv", "run", "start"]