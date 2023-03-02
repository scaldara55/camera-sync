import pynmea2
import serial
import io

ser = serial.Serial()
ser.port = '/dev/tty.usbmodem23401'
ser.baudrate = 9600
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.bytesize = serial.EIGHTBITS
ser.timeout = 1

ser.open()

sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

line = sio.readline()
print(line)
print(type(line))
msg = pynmea2.parse(line)
print(msg)

line = sio.readline()
print(line)
print(type(line))
msg = pynmea2.parse(line)
print(msg)

ser.close()
