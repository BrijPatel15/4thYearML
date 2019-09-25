import sys, os, sched, time
from MidiParser import parse_notes, validate_file
import spidev
dir_path = os.path.dirname(os.path.realpath(__file__))
# MUSIC_PATH = "../../music/guitar.mid"
spi = spidev.SpiDev()
for i in range(100):
    byteArr = bytearray()
    byteArr.append(i)
    #print(int.from_bytes(byteArr[0], "big"))
    spi.open(0,1)
    spi.max_speed_hz = 12000000
    spi.mode=0
    resp = spi.xfer2([byteArr[0]])
    print(i)
    time.sleep(5)