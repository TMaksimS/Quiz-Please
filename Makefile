up_test_db:
	docker compose -f docker-compose-local.yaml up -d
make_migrations: up_test_db
	sleep 2 && alembic upgrade head
up_local: make_migrations
	python3 main.py
down_local:
	docker compose -f docker-compose-local.yaml down --remove-orphans
up_ci:
	docker compose -f docker-compose-ci.yaml up -d
down_ci:
	docker compose -f docker-compose-ci.yaml down --remove-orphans