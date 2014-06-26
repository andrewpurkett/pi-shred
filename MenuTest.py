#!/usr/bin/env python3
import sys
import subprocess
from time import sleep
import pifacecad

def update_pin_text(event):
    event.chip.lcd.write(str(event.pin_num+1))

def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')


def show_sysinfo():
    cad.lcd.clear()
    cad.lcd.write("1) SCAN 2) WIPE\n3)SHRED 4) FIND")
    listener = pifacecad.SwitchEventListener(chip=cad)
    for i in range(4):
        listener.register(i, pifacecad.IODIR_FALLING_EDGE, update_pin_text)
    listener.activate()

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
