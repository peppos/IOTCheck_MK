# IOTCheck_MK

Use Raspberry Pi to visualize your Check_MK alarm.

- Green LED is ON when no alarms in check_mk.
- Red LED is ON when exist alarms in check_mk.

## What do you need

* one Raspberry Pi board
* one CheckMK server
* two leds, one red and one green
* username and login for CheckMK

## Configure CheckMK

Create a public view with all servers or services in scope.

Create a automation user and assign it administrator permissions.

## Configure Raspberry Pi

Boot your Raspbian OS and clone this repo.
```sh
# mkdir /opt/prj
# cd /opt/prj
# git clone https://github.com/peppos/IOTCheck_MK.git
```
Edit the config.ini and put in your data

```ini
[cmk_auth]

CheckMKMaster = < chekmk_ip >
CheckMKAutomationUser = < checkmk_user >
CheckMKAutomationPassword = < checkmk_user_password >
CheckMKSite = < checkmk_site >
CheckMKView = < checkmk_view >
CheckMKHostGroup = < checkmk_hostgroup >

[piezo]

PiezoPin = 15 ## actually not used

[led]

RedLedPin = 24 --> change if you prefer another pin
GreenLedPin = 23 --> change if you prefer another pin
```
Install systemd service
```sh
# cp mon.service /etc/systemd/system/
# systemctl daemon-reload
```
Enable and start service
```sh
# systemctl enable mon.service
# systemctl start mon.service
```
Check the service
```sh
# systemctl status mon.service
● mon.service - Start IOTCheck_mk
   Loaded: loaded (/etc/systemd/system/mon.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2019-06-13 16:18:30 CEST; 55min ago
 Main PID: 438 (python)
   CGroup: /system.slice/mon.service
           └─438 /opt/prj/IOTCheck_MK/venv/bin/python /opt/prj/IOTCheck_MK/IOTCheck_mk.py

Jun 13 16:18:30 raspberrypi systemd[1]: Started Start IOTCheck_mk.
```
