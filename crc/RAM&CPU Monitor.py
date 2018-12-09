import psutil
import sys
from crc.config import interval


def ram_and_cpu():
    string = "RAM"+str(psutil.virtual_memory().percent)+"% CPU"+str(psutil.cpu_percent(interval=interval))+"%"
    return string
while True:
    sys.stdout.write("\r"+str(ram_and_cpu()))
    sys.stdout.flush()
