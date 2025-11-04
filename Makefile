rusty:
	cd backend && uv run maturin develop

run-checks:
	ruff check --fix
	black .

checkout:
	git pull origin main
	git checkout $(branch)