from pyfirmata import Arduino, util
from time import sleep
board = Arduino('/dev/ttyUSB0')
led = 12
while True:
    board.digital[led].write(1)
    sleep(0.2)
    board.digital[led].write(0)
    sleep(0.2)
