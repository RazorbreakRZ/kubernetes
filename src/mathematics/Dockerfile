FROM python:2.7-alpine

WORKDIR /app
COPY ./ /app/mathematics

RUN pip install \
    flask

EXPOSE 5000

ENTRYPOINT [ "sh", "-c", "python -m mathematics" ]