.PHONY: check check-struct check-content check-split check-evals check-tests check-all
check-struct:
	python3 scripts/check_package.py
check-content:
	python3 scripts/check_content.py
check-split:
	python3 scripts/verify_split.py
check-evals:
	python3 scripts/run_evals.py
check-tests:
	python3 -m pytest tests backend/tests -q
check-all: check-struct check-content check-split check-evals check-tests
check: check-all
