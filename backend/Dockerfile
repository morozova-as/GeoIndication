FROM python:3.7.7-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
apt-get install -y gcc

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY ./src /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]