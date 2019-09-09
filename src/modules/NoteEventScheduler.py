#scheduler playground
import sched, time
import spidev
from EventByteConverter import dataFrameToByteConverter

def send_event(name=None, event=None):
    spi = spidev.SpiDev()
    if (name !='CLAP CLAP CLAP'): #only send real notes not fake syncing ones
        spi.open(0,1)
        spi.max_speed_hz = 500000
        spi.mode=0
        if event is 'Note':
                messageToSend = dataFrameToByteConverter(name, event)
                resp = spi.xfer2([messageToSend[0]])
        if event is 'Chord':
                for val in name:
                        messageToSend = dataFrameToByteConverter(val, event)
                        for messages in messageToSend:
                                resp = spi.xfer2([messages])
                                print(resp)
        spi.close() #Added this change bc the docs recommend it we can remove it.
    
def schedule_events(df, s):
    if df.empty:
        raise Exception("No events provided.")
    s.enter(3,1,send_event, argument=('CLAP CLAP CLAP',))
    for index, row in df.head(n=len(df)).iterrows():
        times =row['timeOffset']
        name = row['name']
        event = row['event']
        s.enter(3+times, 1, send_event, argument=(name,event))