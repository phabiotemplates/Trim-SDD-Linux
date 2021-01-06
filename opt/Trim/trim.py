#!/usr/bin/env python
import os
import os.path

def verificaSuporte():
    pass

def statusTrim():
    
    if os.path.isfile("/etc/cron.hourly/timer-trim"):
        return 1
    else:
        return 0
    
def changeTrim():
    
    statusTrim()
    
    if statusTrim() == 0:
        os.system('pkexec bash /opt/Trim/scripts/create')
    else:
        os.system('pkexec bash /opt/Trim/scripts/destroy')
