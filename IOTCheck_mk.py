#!/usr/bin/env python

import configparser, requests
import RPi.GPIO as GPIO
from time import sleep
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

config = configparser.ConfigParser()
config.read(os.path.dirname(os.path.realpath(__file__)) + '/' + 'config.ini')

cmk = dict(config._sections['cmk_auth'])
led = dict(config._sections['led'])

redled = int(led['redledpin'])
greenled = int(led['greenledpin'])

GPIO.setup(redled,GPIO.OUT)
GPIO.setup(greenled,GPIO.OUT)

while True:
  print("Checking...")
  uri = "http://{checkmkmaster}/{checkmksite}/check_mk/view.py?neg_opthost_group=&opthost_group={checkmkhostgroup}&st1=on&st2=on&st3=&stp=&view_name={checkmkview}&_username={checkmkautomationuser}&_secret={checkmkautomationpassword}&request_format=python&output_format=json".format(**cmk)
  output = requests.get(uri)
  if len(output.json()) > 1:
    print("Error found")
    GPIO.output(redled,GPIO.HIGH)
    GPIO.output(greenled,GPIO.LOW)
  else:
    print("No error found")
    GPIO.output(greenled,GPIO.HIGH)
    GPIO.output(redled,GPIO.LOW)
  sleep(30)
