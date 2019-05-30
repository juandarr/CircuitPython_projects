import time
import board
import digitalio

led1 = digitalio.DigitalInOut(board.D3)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.D7)
led2.direction = digitalio.Direction.OUTPUT

led = [led1, led2]
ret = [0.1, 0.2]

def blinking(led, ret):
    led.value = True
    time.sleep(ret)
    led.value = False
    time.sleep(ret)

while True:
    for i in range(len(led)):
        blinking(led[i], ret[i])