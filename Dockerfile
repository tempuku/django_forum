FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY requirements.txt /code/
COPY vendor /code/vendor/
RUN pip3 install -r /code/requirements.txt
COPY . /code

