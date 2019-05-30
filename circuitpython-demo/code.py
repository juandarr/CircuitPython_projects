import time
import board
import digitalio

led1 = digitalio.DigitalInOut(board.D3)
led1.direction = digitalio.Direction.OUTPUT

while True:
    led1.value = True
    time.sleep(0.5)
    led1.value = False
    time.sleep(0.5)
