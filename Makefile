up_test_db:
	docker compose -f docker-compose-local.yaml up -d
down_local:
	docker compose -f docker-compose-local.yaml down --remove-orphans