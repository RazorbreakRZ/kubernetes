FROM python:2.7-alpine

WORKDIR /app
COPY ./ /app/mathematics

RUN apk add --update --no-cache g++ gcc libxslt-dev && \
    pip install \
    flask \
    flask_cors \
    requests \
    lxml

EXPOSE 5000

ENTRYPOINT [ "sh", "-c", "python -m mathematics" ]