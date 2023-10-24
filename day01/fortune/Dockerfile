FROM node:21

WORKDIR /app

RUN apt update && apt install -y curl

COPY package.json .
COPY package-lock.json .
COPY main.js .
COPY public public
COPY views views

RUN npm ci


ENV APP_PORT=3000

EXPOSE ${APP_PORT}

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl -s http://localost:${APP_PORT}/health || exit 1

ENTRYPOINT node main.js
