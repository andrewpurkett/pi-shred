#!/usr/bin/env python3
import sys
import subprocess
from time import sleep
import pifacecad

UPDATE_INTERVAL = 15  # 15 seconds

def scan_for_drives(event):
    event.chip.lcd.clear()
    event.chip.lcd.write("Scan failed\nNot implemented")
    listener = pifacecad.SwitchEventListener(chip=cad)
    listener.register(4, pifacecad.IODIR_FALLING_EDGE, interrupt_process)
    listener.activate()

def wipe_zero(event):
    event.chip.lcd.clear()
    event.chip.lcd.write("Wipe failed\nNot implemented")
    listener = pifacecad.SwitchEventListener(chip=cad)
    listener.register(4, pifacecad.IODIR_FALLING_EDGE, interrupt_process)
    listener.activate()

def wipe_rand(event):
    event.chip.lcd.clear()
    event.chip.lcd.write("Shred failed\nNot implemented")
    listener = pifacecad.SwitchEventListener(chip=cad)
    listener.register(4, pifacecad.IODIR_FALLING_EDGE, interrupt_process)
    listener.activate()

def recover_data(event):
    event.chip.lcd.clear()
    event.chip.lcd.write("Find failed\nNot implemented")
    listener = pifacecad.SwitchEventListener(chip=cad)
    listener.register(4, pifacecad.IODIR_FALLING_EDGE, interrupt_process)
    listener.activate()

def interrupt_process(event):
    event.chip.lcd.clear()
    event.chip.lcd.write("Abort failed\nNot implemented")
    sleep(2)
    show_main_menu()

def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')


def show_main_menu():
    cad.lcd.clear()
    cad.lcd.write("1) SCAN 2) WIPE\n3)SHRED 4) FIND")
    listener = pifacecad.SwitchEventListener(chip=cad)
    listener.register(0, pifacecad.IODIR_FALLING_EDGE, scan_for_drives)
    listener.register(1, pifacecad.IODIR_FALLING_EDGE, wipe_zero)
    listener.register(2, pifacecad.IODIR_FALLING_EDGE, wipe_rand)
    listener.register(3, pifacecad.IODIR_FALLING_EDGE, recover_data)
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
        show_main_menu()
