FROM alpine

COPY --from=consul:1.8.4 /bin/consul /bin/consul

RUN apk add --no-cache gettext

COPY ./register_service /bin/register_service