
import time
from pyfirmata import Arduino, util

board = Arduino('COM3')
it = util.Iterator(board)
it.start()

push_pin = board.get_pin('d:2:i')   
light_pin = board.get_pin('d:8:o')

push_pin.enable_reporting()

while True:
    if push_pin.read() == 1:
        light_pin.write(1)
    else:
        light_pin.write(0)
    time.sleep(0.05)





# import time
# from pyfirmata import Arduino, util

# board = Arduino('COM3')
# it = util.Iterator(board)
# it.start()

# push_pin = board.get_pin('d:2:i')   
# light_pin = board.get_pin('d:8:o')

# push_pin.enable_reporting()

# light_on = 0

# while True:
#     if push_pin.read() == 1 and light_on == 0:
#         light_pin.write(1)
#         light_on = 1
#     elif  push_pin.read() == 1 and light_on == 1:
#         light_pin.write(0)
#         light_on = 0
#     time.sleep(0.05)