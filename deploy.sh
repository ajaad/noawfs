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

# Build package 
mkdir -p whl_file
python3 -m build --sdist --outdir ./whl_file  /home/ajaad/Documents/pywfs







