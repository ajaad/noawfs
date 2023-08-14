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
	
	# Install a package for building the pywfs-package
	pip install build
fi

if true; then
	# Update package
	
	# Activate virtual environment
	source virtEnv/bin/activate
	
	# Uninstall current package
	pip uninstall pywfs -y
	
	# Prepare area
	mkdir -p whl_file
	rm whl_file/* 

	# Build package from testlab
	python3 -m build --outdir ./whl_file --sdist /home/ajaad/Documents/pywfs

	# Install package
	pip3 install whl_file/pywfs-*
fi

if false; then
	# Hardlink to apache .conf-file.
	ln /etc/apache2/sites-available/markakartet.lan.conf ./markakartet.lan.conf
	# Must be on the same partition to work
fi

if false; then
	# Copy/update the apache2 config file:
	cp /etc/apache2/sites-available/markakartet.lan.conf ./markakartet.lan.conf
fi
