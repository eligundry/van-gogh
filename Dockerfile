FROM python:3-slim

ADD ./requirements.txt /opt/van_gogh/requirements.txt
RUN pip install -r /opt/van_gogh/requirements.txt

ADD . /opt/van_gogh
WORKDIR /opt/van_gogh

EXPOSE 8000

USER nobody
