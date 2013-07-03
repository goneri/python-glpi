#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os

# nothing is packaged yet, and I'm trying to not depend on my custom
# environment vars for everthing, so.....
glpimodpath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.split(glpimodpath)[0])

# now this part should work:
from GLPI import GLPIClient

if __name__ == '__main__':

    import warnings
    import getpass
    import pprint
    
    username = "glpi"
    password = "glpi"
    glpi = GLPIClient.Client('http://localhost/plugins/webservices/xmlrpc.php')
    glpi.connect(username,password)
    
    pprint.pprint(glpi.create_objects({
        'Computer': [{
                'name': 'python-computer'
            }]
        }))
    result = glpi.list_objects('Computer', name='python-computer')

    print "%d python-computer computer created!" % len(result)
