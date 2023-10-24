FROM golang:1.21-bookworm AS builder

WORKDIR /app

COPY go.mod .
COPY go.sum .
COPY main.go .

# statically link the binary
RUN CGO_ENABLED=true go build -o main ./...

# create a second container
FROM  debian:bookworm

RUN apt update && apt install -y curl

WORKDIR /app

COPY public public
COPY templates templates

# copy the compiles binary from 'builder' container
COPY --from=builder /app/main .

ENV PORT=3000 INSTANCE_NAME="Go Dov Bear" INSTANCE_HASH=abc123

HEALTHCHECK --interval=30s  --timeout=5s --retries=3 \
  CMD curl -s http://localhost:${PORT}/healthz || exit 1

ENTRYPOINT ./main
