#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
    Shell to Python
    ---------------
    Author:
        Rony Novianto (rony@ronynovianto.com)
'''

import argparse
import re
import os
import subprocess

batch = '''
'''

def parse_arguments(batch):
    parser = argparse.ArgumentParser()
    variables = re.findall('{(.*?)}', batch)
    for variable in set(variables):
        value = None
        for v in [variable, variable.lower(), variable.upper()]:
            value = os.environ.get(v)
            if value:
                parser.set_defaults(**{variable: value})
                break
        is_required = value == None
        parser.add_argument('--' + variable, required=is_required)
    return parser.parse_args()
    
def main(arguments):
    for line in batch.split('\n'):
        if line:
            command = line.format(**vars(arguments))
            subprocess.call(command, shell=True)
            
if __name__ == '__main__':
    arguments = parse_arguments(batch)
    main(arguments)
