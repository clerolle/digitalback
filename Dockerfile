FROM python:3.10.4-alpine3.15

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

RUN  apk update \
	&& apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
	&& pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python", "./manage.py", "runserver", "150.136.95.109:8010"]