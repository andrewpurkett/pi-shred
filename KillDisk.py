#!/usr/bin/env python
#Killdisk 11.10.6 - October 6th 2011
#FoundAt: http://forums.debian.net/viewtopic.php?f=8&t=71310
#Author: Marcus Dean Adams (marcusdean.adams@gmail.com)
#Licensed under version 3 of the GNU General Public License
#A copy of the GNU GPL should be included with this software.
#If it is not, you can view the latest version at
#http://www.gnu.org/licenses/gpl.html

#Imports functions
import os
import sys
import time

#Checks that the user is running a Linux/Unix system
if os.name!="posix":
    print "This program is designed to run only on Unix like"
    print "operating systems."
    print ""
    raw_input("Press Enter to exit...")
    sys.exit("Exiting...")

#Welcome message
print ""
print "KillDisk 11.10.6"
print ""
print "This program will erase any file, disk or partition you specify."
print "At any time you can press Ctrl+C to cancel the program."
print "If you do so before a wipe operation has begun, no changes"
print "will have been made to the drive."
print ""
print "If you experience any problems with this software, feel free to e-mail me:"
print "Marcus Dean Adams (marcusdean.adams@gmail.com)"
print ""
raw_input("Press Enter to continue...")
print ""

#Prompts for the type of wipe to be executed, and sets variables accordingly.
print "What type of wipe would you like to perform? "
print ""
print "1) Overwrite all sectors with zeros (Faster, less secure)"
print "2) Overwrite all sectors with random data (Slower, more secure)"
print ""
style=raw_input("Enter a number: ")
if style=="1":
    wipe="dd if=/dev/zero of="
elif style=="2":
    wipe="dd if=/dev/urandom of="
else:
    print "Invalid input, exiting program to avoid unwanted"
    print "damage to data."
    print ""
    raw_input("Press Enter to exit...")
    sys.exit("Exiting...")

#Displays partitions on all disks.
print ""
print "Displaying partition tables of all drives in 3 seconds..."
time.sleep(3)
os.system("su-to-root -c 'fdisk -l'")
print ""
print "Please choose a device to kill.  Remember if you want to"
print "wipe the whole drive and not just a partition, you can"
print "remove the number appended.  Example /dev/sdc1 becomes /dev/sdc ."
print ""
device=raw_input("Enter device: ")
print ""
count=input("How many times would you like to wipe the device? ")
print ""
print "Writing changes to disk.  All data on %s will be lost."%(device)
print ""
raw_input("Press Enter to continue, or Ctrl+C to exit: ")
print ""
lap=1
for i in range(count):
    print "Processing wipe count %s of %s..."%(lap, count)
    os.system((wipe + "%s")%(device))
    lap=lap+1
print ""
"Done!"

exit
