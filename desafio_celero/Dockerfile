FROM python:3.9

WORKDIR /desafio_celero/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && \
    apt-get install -y less python3-dev build-essential \
    libxml2-dev libxmlsec1-dev libgraphviz-dev libaio1 \
    postgresql postgresql-contrib libpq-dev bash gettext \
    libyaml-dev

RUN pip install -U pip

RUN pip install -U channels

ADD . /desafio_celero/

ARG MODE
ARG FIXTURE

ENV MODE $MODE
ENV FIXTURE $FIXTURE

RUN sh docker/build.sh

RUN apt-get autoremove -y

ENTRYPOINT ["/desafio_celero/docker/entrypoint.sh"]
