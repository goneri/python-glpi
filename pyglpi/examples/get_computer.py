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
    
    glpi = GLPIClient.Client('http://localhost/plugins/webservices/xmlrpc.php')
    glpi.connect("glpi", "glpi")
    
    print "\nGetting Computer\n"
    pprint.pprint(glpi.get_computer(29))

    print "\nGetting Help\n"
    pprint.pprint(glpi.get_computer(29,help=True))

    print "\nGetting Computer With All Options\n"
    pprint.pprint(glpi.get_computer(29, id2name=True,
                                    networkports=True, contracts=True ))

    print "\nGetting with infocoms doesn't work for some reason, skipping\n"

    # pprint.pprint(glpi.get_computer(29, id2name=True,
    #                                 networkports=True, contracts=True,
    #                                 infocoms=True))
