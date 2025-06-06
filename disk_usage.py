import shutil
import sys
def check_disk_usage(disk, min_absolute, min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free/du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return True
    return False

if not check_disk_usage("/",2,10):
    print("ERROR: not enough disk space.")
    sys.exit(1)

print("everything ok")
sys.exit(0)