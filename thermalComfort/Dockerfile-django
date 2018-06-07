FROM python:3.6
ENV PYTHONUNBUFFERED=1
ENV C_FORCE_ROOT=1

RUN mkdir /app
WORKDIR /app

ADD ./requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 8000
