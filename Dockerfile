FROM python:3.10.4-alpine3.15

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt ./

RUN python -m pip install -r requirements.txt

COPY ./ ./

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8010"]