#!/bin/bash

if true; then
	## Make the files executable
	chmod +x index.py
	chmod +x naturopplevelser.py
	chmod +x verneforslag.py
	chmod +x forvaltningsforslag.py
	chmod +x annet.py
fi

## update the pywfs-package
#cd ~/Documents/pywfs

if false; then
	# Create a virtual environment
	python3 -m venv virtEnv
	source virtEnv/bin/activate
fi

if true; then
	# Update package
	
	# Uninstall current package
	pip uninstall pywfs -y
	
	# Prepare area
	mkdir -p whl_file
	rm whl_file/* 

	# Build package from testlab
	python3 -m build --sdist --outdir ./whl_file  /home/ajaad/Documents/pywfs

	# Install package
	pip3 install whl_file/pywfs-*
fi




