FROM python:3.9-alpine

WORKDIR /flask

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:5000 --chdir ./app main:app
