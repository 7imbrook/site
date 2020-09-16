FROM envoyproxy/envoy-alpine:v1.14-latest

COPY --from=consul:1.8.4 /bin/consul /bin/consul
COPY --from=vault:1.5.3 /bin/vault /bin/vault

RUN apk add --no-cache gettext

COPY ./bin/ /bin/