#!/usr/bin/env python
#-*- coding:utf-8 -*-

from GLPI import GLPIClient

# Connection parameters
host = 'glpitest.systea.fr'
username = 'glpi'
password = 'cela2G!'

# Init the object
glpi=GLPIClient.Client()

# Connect
glpi.connect(host,username,password)

# Who am I ?
glpi.get_my_info()
