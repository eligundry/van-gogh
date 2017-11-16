FROM python:3-slim

ADD ./requirements.txt /opt/van_gogh/requirements.txt
RUN pip install -r /opt/van_gogh/requirements.txt

ADD . /opt/van_gogh
WORKDIR /opt/van_gogh

# Compile all the Python files so the build breaks if there is a syntax error.
RUN python3 -m compileall .

USER nobody
