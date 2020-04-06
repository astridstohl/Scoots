#import evdev
#evdev code source: https://core-electronics.com.au/tutorials/using-usb-and-bluetooth-controllers-with-python.html
from pyfirmata import Arduino, util
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event2')
board = Arduino('/dev/ttyACM0')
#button code variables (change to suit your device)

bBtn = 305
xBtn = 307


#prints out device info at start
print(gamepad)

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1: #if same event value is needed group the inputs together.
            if event.code == bBtn:
                print("I DID IT!!")
                board.digital[13].write(1)
            elif event.code == xBtn:
                print("I DID IT!!")
                board.digital[13].write(1)
        elif event.value == 0:
            if event.code == bBtn:
                print("I DIDN'T DID IT!!")
                board.digital[13].write(0)
            if event.code == xBtn:
                print("I DIDN'T DID IT!!")
                board.digital[13].write(0)
