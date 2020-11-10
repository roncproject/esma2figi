# esma2figi
Enrich a csv file with ISIN codes with FIGI data

# About
This is a Python script which takes a CSV with ISIN codes as input, and enriches these with OpenFIGI data

# Prerequisites
* Python, I use Python 3.8.3 from: https://www.python.org/downloads/ 
* GIT, I use 2.28.0 (windows) from: https://git-scm.com/downloads
* A commandline, Unix or Windows
* ESMA files from: "https://www.esma.europa.eu/data-systematic-internaliser-calculations"

# Installation
* Clone with GIT, from repo at: https://github.com/roncproject/esmasidata2csv.git

# Usage
* Get an ESMA file, for testing I used: https://www.esma.europa.eu/sites/default/files/equity_si_calculations_-_publication_file_august_2020.xlsx
* Convert ESMA files with the help of: https://github.com/roncproject/esmasidata2csv  
* On the UNIX/ms windows/MAC/other command line, type: "python esma2figi.py [name of the esma csv]" and press enter
* The ESMA Isin data enriched with the FIGI data will be printed to your screen
* In the app directory a file called "esma2figi.log" will appear. It contains technical logging info
* If you want to save the output, you can (on ms windows and UNIX/Linux) type: "python esma2figi.py [name of the esma csv file] **> outputfile.csv**" (Or any name you want for the output file) 

# TODO
* Make a testsuite

# Remarks
* This is a work in progress
