FROM python:3.12.1-alpine3.19

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip

COPY . /app/

RUN pip install -r requirements.txt

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8010", "--chdir", "docker_django", "docker_django.wsgi:application"]