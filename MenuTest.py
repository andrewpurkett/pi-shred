#!/usr/bin/env python3
import sys
import subprocess
from time import sleep
import pifacecad

UPDATE_INTERVAL = 15  # 15 seconds

def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')


def show_sysinfo():
    while True:
        cad.lcd.clear()
        cad.lcd.write("1) SCAN 2) WIPE\n3)SHRED 4) FIND")

        sleep(UPDATE_INTERVAL)


if __name__ == "__main__":
    cad = pifacecad.PiFaceCAD()
    cad.lcd.blink_off()
    cad.lcd.cursor_off()

    if "clear" in sys.argv:
        cad.lcd.clear()
        cad.lcd.display_off()
        cad.lcd.backlight_off()
        sleep(3)
    else:
        cad.lcd.clear()
        cad.lcd.backlight_on()
        cad.lcd.write("PI-SHRED v0.01\nwww.aj.cm/pi")
        sleep(3)
        show_sysinfo()
