test: FORCE
	mypy connectionSearch
	python3 -m unittest
	
FORCE: ;
