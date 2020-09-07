FROM python:3.9.0b3-alpine3.12

RUN apk add -f gcc

COPY server.py server.py
COPY requirements.txt /pip/

RUN pip install -r /pip/requirements.txt

ENV PYTHONUNBUFFERED=1
ENV NUMBEROFROWSPEREVENT=2
ENV LANG=en_GB.utf8
ENV FLASK_APP=server.py
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0"]
