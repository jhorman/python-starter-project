################################
# Setup the expensive build env
#

FROM python:3.9.6-buster as build

ENV PYTHONUNBUFFERED=1
ENV PIPENV_VENV_IN_PROJECT=1

RUN set -ex && apt-get -y update && apt-get -y install git wget

WORKDIR /app

# Install the python dependencies
RUN set -ex && pip3 install virtualenv==20.4.7 && pip3 install pipenv==2021.5.29
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock
RUN set -ex && pipenv install --deploy --python /usr/local/bin/python

################################
# Setup the main app
#

FROM python:3.9.6-slim-buster as application
ENV PYTHONUNBUFFERED=1
ENV PIPENV_VENV_IN_PROJECT=1
ENV AWS_DEFAULT_REGION=us-east-1
ENV PATH=.venv/bin:$PATH

# Setup some unix deps
RUN set -ex && apt-get -y update && apt-get -y install wget procps
RUN set -ex && pip3 install virtualenv==20.4.7 && pip3 install pipenv==2021.5.29

WORKDIR /app
COPY --from=build /app /app/
COPY . /app

CMD pipenv run honcho start