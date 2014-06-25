#Foreword
Although the average consumer is friendly with paper shredders, there isn't an easy equivalent in the digital world that works as simply as a shredder.

I want to change that, and make it easy for the average person to have access to the same data erasing security that governments and security analysts use and suggest others use. The fact that there is not a 1-button wipe function on external hard drives means most people do not remove personal data from drives before recycling or reselling their outdated hardware.

pi-shred prerequisites
=======================
- raspberry pi model b (model a not available for manual install procedure)
- 4 gb sd card
- PiFace control and display add-on board
- usb to sata adapter (if wiping SATA drives)
- 5v@2.1a micro-usb power supply
- HDMI cable and usb keyboard (Manual install only)

Manual installation instructions
================================
- Follow setup instructions for Raspian installation to SD card
- Enable network connectivity on the raspberry pi
- Follow setup instructions to configure PiFace interface: http://www.piface.org.uk/guides/setting_up_pifacecad/
- git clone this repository to /home/pi/pi-shred/ and run setup.sh (not yet available!)
- Enjoy!

3D printed case designs
=======================
We are interested in developing a case for this project that incorporates a SATA dock. If you are interested in assisting with this project, email pishred at aj dot cm
