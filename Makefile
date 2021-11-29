test: FORCE
	mypy connectionSearch
	python3 -m unittest

create_db:
	python3 database/setup.py

create_db_delete_old:
	- rm database/data.db
	python3 database/setup.py

FORCE: ;
