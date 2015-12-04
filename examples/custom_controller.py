#!/usr/bin/env python

'''
    Custom controller
    -------------------------
    This example shows how to build custom controller
    
    Authors:
        Rony Novianto (rony@ronynovianto.com)
'''

import time
import asmo

def run(attention):
    results = attention.compete()
    for (name, details) in results['winners'].items():
        print(name, details['total_attention_level'])
    for (action_name, parameter) in results['actions'].items():
        print(action_name, parameter)
    return True
    
def main():
    attention = asmo.Attention('http://localhost:12766')
    print('[ OK ] Start custom_controller')
    while run(attention): time.sleep(0.5)
    
if __name__ == '__main__':
    main()
