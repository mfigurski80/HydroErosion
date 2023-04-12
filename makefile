release:
	python3 -m build
	python3 -m twine upload dist/*
run:
	python3 -m hydro_erosion maps/raw/heightmap.csv maps/raw/rockmap.csv maps/processed/erodedmap.csv 4 
	python3 viewLandscape.py maps/processed/erodedmap.csv
