'''
---stpip---
This file organises the command line interface

@R. Thomas
@Santiago, Chile/ Sheffield, UK
@2019-24
'''


##standard library
import argparse

#local import
from . import __info__ as info


def command_line(args):
    '''
    This function defines the command line interface of the program.

    Parameters
    -----------
    None

    Returns
    -------
    args    Namespace with arguments
    '''

    ##create parser object
    parser = argparse.ArgumentParser(description='A pepy.tech web scraping for pypi'+\
                                                 f' download stats, version {info.__version__},'+ \
                                                 'Licence: GPL')


    ###optional arguments
    parser.add_argument('-k', help='API Key for pepy.tech (you need an account)')
    parser.add_argument('-p', help='package, or list of packages separated by comas (no space)')
    parser.add_argument('--version', action='version', version=info.__version__)

    ##create a group of arguments that are mandatory
    return parser.parse_args(args)
