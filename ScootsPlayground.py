from pyfirmata import Arduino, util # Imports arduino important libraries. (research later for better decription.)
import time #Allows for time based functions such as time.sleep(timeinseconds)

board = Arduino('COM7') # Defines which port the Arduino board is connected to.
i = 1
while True:
    board.digital[5].write(1)
    board.digital[4].write(1) # places digital pin 4 on the arduino board into the ON (1) state.
    time.sleep(1)               # Delays the execution of the code by 1 second.
    board.digital[5].write(0)
    board.digital[4].write(0)
    time.sleep(1)
    #board.digital[7].write(1)
    #time.sleep(2)
    #board.digital[7].write(0)
    print( "revolution: " + str(i))
    i += 1
