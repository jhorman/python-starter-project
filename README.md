# python-starter-project

## Installation / Setup

```bash
# https://github.com/pyenv/pyenv#installation
# https://pipenv.readthedocs.io/en/latest/#install-pipenv-today
brew install pyenv redis pipenv
pyenv install 3.9.6

# from project dir
pipenv shell --python 3.9.6
pipenv install --dev

# make sure black pre-commit hooks are in
pre-commit install
pre-commit install --hook-type pre-push
```

## Running tests

```bash
pipenv run pytest
```

## Running code reformatter

```bash
pipenv run black starter_project
```

## Running a Local Dev Server

```bash
pipenv run uvicorn starter_project.www.server:app --reload --port 5000
```