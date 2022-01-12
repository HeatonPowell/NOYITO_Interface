import time
import serial

s = serial.Serial(port='COM2', baudrate=9600, timeout=.1)
if s.isOpen():
    s.close()
s.open()
s.isOpen()
#time.sleep(1)
#print(s.baudrate)

packetOpen1 = bytearray()
packetOpen1.append(0xA0)
packetOpen1.append(0x01)
packetOpen1.append(0x01)
packetOpen1.append(0xA2)

packetClose1 = bytearray()
packetClose1.append(0xA0)
packetClose1.append(0x01)
packetClose1.append(0x00)
packetClose1.append(0xA1)

packetOpen2 = bytearray()
packetOpen2.append(0xA0)
packetOpen2.append(0x02)
packetOpen2.append(0x01)
packetOpen2.append(0xA3)

packetClose2 = bytearray()
packetClose2.append(0xA0)
packetClose2.append(0x02)
packetClose2.append(0x00)
packetClose2.append(0xA2)

packetStatus = bytearray()
packetStatus.append(0xFF)

s.write(packetOpen1)
time.sleep(1)
s.write(packetClose1)
time.sleep(1)
#s.write(packetOpen2)
#s.write(packetClose2)
s.write(packetStatus)
print(s.read(255))
s.close()