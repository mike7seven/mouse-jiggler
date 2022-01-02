# mouse-jiggler
Mouse Jiggler for Raspberry Pi Pico Using CircuitPython
All credit goes to @talaexe on TikTok https://www.tiktok.com/@talaexe/video/7045424803938979078?sender_device=pc&sender_web_id=7048238389116880390&is_from_webapp=v1&is_copy_url=0

# Requirements
1. A Windows, Mac or Linux computer
2. Raspberry Pi Pico (Can be purchased at ww.amazon.com or if you have a local www.microcenter.com)
3. USB-A to Micro USB Cable 
4. Circuit Python - https://circuitpython.org/
5. Thonny IDE - https://thonny.org/

# Setup and software installation
1. Go to this url https://circuitpython.org/downloads and select the Raspberry Pi Pico board. 
2. Click on the Download UF2 button. Remember where you downloaded this file you won't use it until later. 
3. Download the IDE from https://thonny.org/ and select the version for your operating system.
4. Download and install the Thonny IDE from https://thonny.org/. Be sure to select the version for operating system. 
5. Open the Thonny IDE. 

# Setup the Raspberry Pico Pi to use Circuit Python
1. Plug the Raspberry Pi Pico into your computer. 
2. The Pico should show up as a drive on your computer. Open the Pico drive. 
3. Find the location where you downloaded the Circuit Python UF2 file and drag it to the Pico drive. 
4. This will install the Circuit Python software on the Pico Pi and then reboot the Pico Pi. 
5. Once rebooted the Pico Pi drive should be renamed to CIRCUITPY. 

# Get the mouse jiggler working
1. Copy the code from the main.py file here in Github. Then paste it into the Thonny IDE. 
2. Go to run, then select interpreter, make sure you have Circuit Python selected and ensure the Pico is selected under the port. 
3. Select tools, then manage packages, search for Adafruit HID. Select the adafruit_hid package. Note: the package may be named similar
4. Click the green go button and watch your mouse move. 
5. Save the program file to your local computer. Click file, then save as main.py in your location of choice. 

# Prepare the Pico Pi to run this program as soon as it plugged into a computer
1. Click file, choose the Pico Pi, then save as code.py
2. Properly eject or unmount the Pico Pi drive. 
3. Plug into computer where you want the Pico Pi to act as a mouse.



# Other learning resources and references
https://circuitpython.org/ \
https://circuitpython.org/downloads \
https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html \
https://learn.adafruit.com/circuitpython-essentials \
https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython-programming-basics \
