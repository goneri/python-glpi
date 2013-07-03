#!/usr/bin/env python
#-*- coding:utf-8 -*-

from GLPI import GLPIClient

# Init the object
glpi=GLPIClient.Client('http://localhost/plugins/webservices/xmlrpc.php')

# Connect
glpi.connect(host,username,password)

# Who am I ?
glpi.get_my_info()
