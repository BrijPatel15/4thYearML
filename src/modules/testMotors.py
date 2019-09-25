import sys, os, sched, time
from EventByteConverter import dataFrameToByteConverter
import spidev

dir_path = os.path.dirname(os.path.realpath(__file__))
# MUSIC_PATH = "../../music/guitar.mid"

if len(sys.argv) == 1:
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
        time.sleep(0.5)
else:
    notes = sys.argv[1:]
    print("notes To send DEBUG:", notes)
    if len(notes) > 1: #Chord
        spi = spidev.SpiDev()
        for n in notes:
            messageToSend = dataFrameToByteConverter("Chord", n)
            print(messageToSend)
            spi.open(0,1)
            spi.max_speed_hz = 12000000
            spi.mode=0
            resp = spi.xfer2(messageToSend[0])
    else:
        messageToSend = dataFrameToByteConverter("Note", notes[0])
        print(messageToSend)
        spi.open(0,1)
        spi.max_speed_hz = 12000000
        spi.mode=0
        resp = spi.xfer2(messageToSend[0])
            
        