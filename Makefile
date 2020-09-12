
PROTO_CC := python -m grpc_tools.protoc

protos := $(wildcard protos/*)

build: $(protos)

%.proto:
	$(PROTO_CC) \
		--proto_path=./ \
		--python_out=./backend/ \
		--grpc_python_out=./backend/ \
		--experimental_allow_proto3_optional \
		$@

sync:
	./scripts/sync_protos.sh