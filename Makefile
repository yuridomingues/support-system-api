up:
	docker compose up --build -d

down:
	docker compose down -v
	
test-auth:
	pytest tests/test_auth.py

test-clients:
	pytest tests/test_clients.py

test-tickets:
	pytest tests/test_tickets.py

test: test-auth test-clients test-tickets
