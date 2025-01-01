CMD ?= sh
DEV_COMPOSE ?= docker/docker-compose.yml
CONTAINER_NAME ?= app

DC_TYPE := $(shell which docker-compose > /dev/null; echo $$?)
ifeq ($(DC_TYPE),1)
	DOCK_COMP=docker compose
else
	DOCK_COMP=docker-compose
endif

rebuild build:
	$(DOCK_COMP) build

force-build:
	$(DOCK_COMP) build --no-cache

up:
	$(DOCK_COMP) up -d

down:
	$(DOCK_COMP) down --remove-orphans

log logs:
	$(DOCK_COMP) logs -f $(CONTAINER_NAME)

shell: up
	$(DOCK_COMP) exec $(CONTAINER_NAME) $(CMD)

root: up
	$(DOCK_COMP) exec -u 0 $(CONTAINER_NAME) $(CMD)

clean: down
	rm -rf output/*
