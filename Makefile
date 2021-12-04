test: FORCE
	mypy connectionSearch
	python3 -m unittest
	find ./connectionSearch -iname "*.py" -print -exec pylint --disable=invalid-name --disable=missing-docstring --disable=bad-indentation --disable=line-too-long --disable=too-few-public-methods --disable=trailing-whitespace {} \;
	find ./test -iname "*.py" -print -exec pylint --disable=invalid-name --disable=missing-docstring --disable=bad-indentation --disable=line-too-long --disable=too-few-public-methods --disable=protected-access --disable=trailing-whitespace {} \;

create_db:
	python3 database/setup.py

create_db_delete_old:
	- rm database/data.db
	python3 database/setup.py

create_dataset_basic:
	python3 -c 'from database.add_data import create_dataset_basic; create_dataset_basic() '

create_whole_db: create_db create_dataset_basic

recreate_whole_db: create_db_delete_old create_dataset_basic

FORCE: ;
