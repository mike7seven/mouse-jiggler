# This line will import the CircuitPython USB HID library from Adafruit.
import usb_hid
# This line will use the CircuitPython USB HID library from Adafruit and tell the Raspberry Pi Pico to act like a mouse.
from adafruit_hid.mouse import Mouse
# This will import the CircuitPython time library
import time
# We are declaring a varible here called mouse. 
mouse = Mouse(usb_hid. devices)
# The below "while True" statement uses the mouse variable and tells the screen pointer to move on the X axis 200 pixels back and forth as if it were being controlled by a real mouse.
# The "time.sleep" is telling the cursor to pause for 1 second before moving again. 
while True:
    mouse.move (x=200)
    time. sleep(1)
    mouse.move(x=-200)
    time.sleep(1)
    
# To do: Add an end statement or a statement to tell the program to run a certain amount of time then end. Otherwise the program will run until the Pico is disconnected.
