#!/usr/bin/env python

import configparser, requests

config = configparser.ConfigParser()
config.read('config.ini')

cmk = dict(config._sections['cmk_auth'])

uri = "http://{checkmkmaster}/{checkmksite}/check_mk/view.py?neg_opthost_group=&opthost_group={checkmkhostgroup}&st1=on&st2=on&st3=&stp=&view_name={checkmkview}&_username={checkmkautomationuser}&_secret={checkmkautomationpassword}&request_format=python&output_format=json".format(**cmk)

output = requests.get(uri)
