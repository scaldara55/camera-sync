import serial
from pynmea2.streamer import NMEAStream

ser = serial.Serial()
ser.port = '/dev/tty.usbmodem23401'
ser.baudrate = 9600
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.bytesize = serial.EIGHTBITS
ser.timeout = 1

ser.open()

sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))


while True:
    try:
        streamer = NMEAStream(sio)
        print(streamer.get_strings())
#        line = sio.readline()
#        msg = pynmea2.parse(line)



    except serial.SerialException as e:
        logger.error('Device error: {}'.format(e))
        break
    except pynmea2.ParseError as e:

        logger.error('Parse error: {}'.format(e))
    except UnicodeDecodeError as e:
        logger.error('UnicodeDecodeError error: {}'.format(e))
    continue


