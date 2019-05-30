import board
from pulseio import PWMOut
from digitalio import DigitalInOut, Direction, Pull
from adafruit_ble.uart import UARTServer
from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.color_packet import ColorPacket

r = PWMOut(board.RGB_LED_RED, duty_cycle=0)
g = PWMOut(board.RGB_LED_GREEN, duty_cycle=0)
b = PWMOut(board.RGB_LED_BLUE, duty_cycle=0)


uart_server = UARTServer()


while True:
    uart_server.start_advertising()
    while not uart_server.connected:
        pass

    while uart_server.connected:
        packet = Packet.from_stream(uart_server)
        if isinstance(packet, ColorPacket):
            print(packet.color)
            dc = [-257*c+65535 for c in packet.color]
            r.duty_cycle, g.duty_cycle, b.duty_cycle = dc