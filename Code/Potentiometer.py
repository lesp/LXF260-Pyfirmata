from pyfirmata import Arduino, util
from time import sleep
board = Arduino('/dev/ttyUSB0')
led = 12
it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
while True:
    value = board.analog[0].read()
    print(value)
    if value == None:
        value = 0
    elif value > 0.05:
        board.digital[led].write(1)
        sleep(value)
        board.digital[led].write(0)
        sleep(value)
    else:
        board.digital[led].write(0)
