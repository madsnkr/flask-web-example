FROM python:3-alpine

ARG CREATED
ARG VERSION
ARG REVISION

LABEL org.opencontainers.image.title="Flask Web Example"
LABEL org.opencontainers.image.description="An example flask webapp"
LABEL org.opencontainers.image.url="https://github.com/madsnkr/flask-web-example"
LABEL org.opencontainers.image.source="https://github.com/madsnkr/flask-web-example"

ENV REDIS_HOST redis
ENV REDIS_PORT 6379
ENV WEB_PORT 8000

EXPOSE ${WEB_PORT}

RUN addgroup -S app && adduser -S app -G app

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

USER app

CMD [ "gunicorn", "-b", ":8000", "app:app" ]
