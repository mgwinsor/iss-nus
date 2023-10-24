FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PORT=3000
ENV INSTANCE_NAME="dov-bear"
ENV INSTANCE_HASH="1234abcd"

EXPOSE ${PORT}

ENTRYPOINT python main.py
