FROM python:2.7-alpine

WORKDIR /app
COPY ./ /app/frontend

RUN pip install \
    flask

EXPOSE 80

ENTRYPOINT [ "sh", "-c", "python -m frontend" ]