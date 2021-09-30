FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=ms
ENV FLASK_ENV=production

RUN apk update \
    && apk add --no-cache \
        build-base \
        mariadb-dev	\
        python3-dev

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install -e .
RUN coverage run -m pytest
RUN coverage report
RUN chmod a+rx ./start.sh

EXPOSE 5000
CMD ["./start.sh"]
