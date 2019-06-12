#!/usr/bin/env python

import configparser, request

config = configparser.ConfigParser()
config.read('config.ini')

print(config['cmk_auth']['CheckMKMaster'])
