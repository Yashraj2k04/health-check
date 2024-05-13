#!/usr/bin/env python3
import os
import sys
import shutil
import socket
def check_reboot():
    '''returns True if the computer has a pending reboot'''
    return os.path.exists("/run/reboot-required")

def check_disk_usage(disk, min_gb, min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free/du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def check_root_full():
    '''returns True if the rool partition is full, False otherwise'''
    return check_disk_usage(disk="/",min_gb=2, min_percent=10)

def check_no_network():
    '''returns True if it fails ti resolve goolge's URL, false otherwise'''
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

def main():
    checks =  [
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition full")
        (check_no_network, "No working newtwork"),
    ]
    everythin_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everythin_ok= False
    if not everythin_ok:
        sys.exit(1)
        
    print("Everything ok.")
    sys.exit(0)
main()