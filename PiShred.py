#!/usr/bin/env python3
import sys
import subprocess
from time import sleep
import pifacecad

READ_TIME = 2 # Give user at least this many seconds to read messages
# (set to 0 if you're "kind of a big deal")

def scan_for_drives(event):
    event.chip.lcd.clear()
    event.chip.lcd.write("Scan failed\nNot implemented")
    listener = pifacecad.SwitchEventListener(chip=cad)
    listener.register(4, pifacecad.IODIR_FALLING_EDGE, interrupt_process)
    listener.activate()
    #TODO: ls /dev/ | grep -v etc...

def wipe_zero(event):
    event.chip.lcd.clear()
    event.chip.lcd.write("Wipe failed\nNot implemented")
    listener = pifacecad.SwitchEventListener(chip=cad)
    listener.register(4, pifacecad.IODIR_FALLING_EDGE, interrupt_process)
    listener.activate()
    #TODO: wipe="dd if=/dev/zero of="


def wipe_rand(event):
    event.chip.lcd.clear()
    event.chip.lcd.write("Shred failed\nNot implemented")
    listener = pifacecad.SwitchEventListener(chip=cad)
    listener.register(4, pifacecad.IODIR_FALLING_EDGE, interrupt_process)
    listener.activate()
    #TODO: wipe="dd if=/dev/urandom of="
    #TODO: Seed random with...
    # 1) owner's TV remote controls (Pressing random buttons pointed at IR sensor)
    # or 2) other PiFace input data (Buttons 5-8?)

def recover_data(event):
    event.chip.lcd.clear()
    event.chip.lcd.write("Find failed\nNot implemented")
    listener = pifacecad.SwitchEventListener(chip=cad)
    listener.register(4, pifacecad.IODIR_FALLING_EDGE, interrupt_process)
    listener.activate()
    #TODO: Learn how to implement this

def interrupt_process(event):
    event.chip.lcd.clear()
    event.chip.lcd.write("Aborted!")
    sleep(READ_TIME)
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
        sleep(READ_TIME)
    else:
        cad.lcd.clear()
        cad.lcd.backlight_on()
        cad.lcd.write("PI-SHRED v0.01\nwww.aj.cm/pi")
        sleep(READ_TIME)
        show_main_menu()
