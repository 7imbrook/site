
canary: canary_push
	kubectl apply -f app.yaml

canary_push: build_canary
	docker push 7imbrook/site:canary

build_canary:
	docker build -t 7imbrook/site:canary .