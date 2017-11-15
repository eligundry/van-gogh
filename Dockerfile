FROM python:3-slim

ADD ./requirements.txt /opt/app/requirements.txt
RUN pip install -r requirements.txt

ADD . /opt/app
WORKDIR /opt/app

USER nobody
