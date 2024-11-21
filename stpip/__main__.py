#!/usr/bin/./python
# -*- coding: utf-8 -*-
'''
---stpip---

stpip is a program web scrapping the pepy.tech website that displays pepy statistics.

usage: stpip --help
'''


###Python standard library
import sys
import os

###local imports
from . import cli
from . import __info__ as info
from . import scraping
from . import display

def main():
    '''
    This is the main function of the program.
    '''
    ###first we load the command line interface
    args = cli.command_line(sys.argv[1:])

    ###here we check if at least one argument was given:
    if not args.p:
        print('\033[1m[stpip Error]> no argument passed ...exit\033[0;0m')
        sys.exit()

    if args.p:
        if not args.k:
            print('\033[1m[stpip Error]> Need an API key file...exit\033[0;0m')
            sys.exit()
        else:
            #Check is apikey file is there
            if not os.path.isfile(args.k):
                print('\033[1m[stpip Error]> apikey file does not exist')
                sys.exit()

            ##read the key
            with open(args.k) as f:
                apikey = f.readline().strip()

            ###extract package names from CLI
            packs = args.p.split(',')

            if len(packs)>1:
                tot = 0

            ##and go scraping!
            for i in packs:
                total, month, week, yesterday, yest_date= scraping.scrap(i, apikey)

                if len(packs)>1:
                    tot += int(total)

                display.full(total, month, week, yesterday, yest_date, i)

            if len(packs)>1:
                print(f'\033[1mTotal for all requested packages: {tot} Downloads')
