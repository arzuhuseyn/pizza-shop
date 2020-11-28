dev:
	@docker-compose \
			-f _development/docker-compose.yml \
		up --build -d
	

down:
	@docker-compose \
		-f _development/docker-compose.yml \
		down