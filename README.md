#Foreword
Although the average consumer is familiar with paper shredders, most people don't know how to achieve the equivalent goal in the digital world. This project is designed to implement a 1-touch secure wipe in a consumer friendly package!

pi-shred manual install prerequisites
=======================
- Raspberry Pi Model B
- 4GB SD Card
- PiFace control and display add-on board
- USB to SATA Adapter (if wiping SATA drives, can be used for USB externals without this)
- 1 Amp 5 Volt MicroUSB power supply
- HDMI cable
- USB Keyboard

Auto-installation instructions
==============================
- These will be added at a later date, and with them we will add support for the low-price Raspberry Pi (Model A)!

Manual installation instructions
================================
- Follow setup instructions for Raspian installation to SD card
- Enable network connectivity on the raspberry pi
- Follow setup instructions to configure PiFace interface: http://www.piface.org.uk/guides/setting_up_pifacecad/
- Run this command from terminal on the RaspPi: `cd ~; git clone git@github.com:andrewpurkett/pi-shred.git`
- Append "sudo python3 /home/pi/pi-shred/PiShred.py" to /etc/rc.local using vim or nano
- Reboot your pi with `sudo reboot`, unplug your keyboard, ethernet cable or wireless dongle, and HDMI cable
- Enjoy!

3D printed case designs
=======================
- We are in need of a case design for this project that incorporates a low-cost popular SATA dock. If you are interested in assisting with this project, email pi dot shred at aj dot cm to find out more about how you can help.
