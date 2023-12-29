FROM python:3.10.4-alpine3.15

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

RUN mkdir /app

WORKDIR /app

RUN  apk update \
	&& apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
	&& pip install --upgrade pip 

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 8010

CMD python manage.py runserver