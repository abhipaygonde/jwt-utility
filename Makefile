DOCKER = docker-compose -p jwt-utility -f docker-compose.yaml

run:
	docker run -d --name jwt-utility -t -p 80:80 jwt-utility
build:	
	docker build . -t jwt-utility
compose:
	$(DOCKER) up