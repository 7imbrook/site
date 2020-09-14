FROM envoyproxy/envoy-alpine:v1.14-latest

COPY --from=consul:1.8.4 /bin/consul /bin/consul

RUN apk add --no-cache gettext

COPY ./register_service /bin/register_service
COPY ./shutdown /bin/shutdown