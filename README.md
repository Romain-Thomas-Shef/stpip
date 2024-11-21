What is stpip?
==============

[![DOI](https://zenodo.org/badge/176632808.svg)](https://zenodo.org/badge/latestdoi/176632808)

stpip is a simple webscraping program the looks for pypi download statistics from the pepy.tech webpage [https://github.com/psincraian/pepy]


How to install stpip?
=====================

A simple `pip install stpip` will do the installation, with the only dependencies. The last version is 19.5.0.


How to use it?
==============

To display the help you can `stpip --help` and you will get:

    `usage: stpip [-h] [-k K] [-p P] [--version]

    A pepy.tech web scraping for pypi download stats, version 24.11.0,Licence: GPL

    options:
        -h, --help  show this help message and exit
        -k K        API Key for pepy.tech (you need an account)
        -p P        package, or list of packages separated by comas (no space)
        --version   show program's version number and exit


The two mandatory arguments are the apikey file and the name of the package(s). The apikey can be retrieve from pepy.tech when you create an account. Then you just need to copy it in a text file. Once done, you can start using stpip: 

	>> stpip -k apikeyfile -p matplotlib

will give:

    ###############################################
          Download counts for matplotlib
     Total all time: 2034912890
     Total last 7 days: 17319966
     Total last 30 days: 69550689
     last day 2024-11-20: 2792617
    --> visit https://pepy.tech/project/matplotlib
    ##############################################

You can also give multiple packages:

	>> stpip -k apikeyfile -p matplotlib,numpy 

This will give the same blocks for all packages.
