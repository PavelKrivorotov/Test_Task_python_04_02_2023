# syntax=docker/dockerfile:1

FROM python:3.10-alpine3.15

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["python", "manage.py"]