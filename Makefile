
SUDO= sudo
DOCKER_COMPOSE:=$(shell which docker-compose || echo "docker compose")
DOCKER= docker
PROJET= hades

.PHONY: all

all: builds up

builds:
	$(SUDO) $(DOCKER_COMPOSE) build --force-rm

up:
	$(SUDO) $(DOCKER_COMPOSE) up

clean:
	$(SUDO) $(DOCKER) image rm -f $(PROJET) 
