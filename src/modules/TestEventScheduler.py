#scheduler playground
import sched, time
import spidev
from EventByteConverter import dataFrameToByteConverter

def send_event(name=None, event=None, iterator=None):
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
    
def schedule_events(df, s):
    if df.empty:
        raise Exception("No events provided.")
    s.enter(3,1,send_event, argument=('CLAP CLAP CLAP',))
    iterator = 1
    for index, row in df.head(n=len(df)).iterrows():
        times =row['timeOffset']
        name = row['name']
        event = row['event']
        s.enter(3+times, 1, send_event, argument=(name,event,iterator))
        iterator = iterator + 1
