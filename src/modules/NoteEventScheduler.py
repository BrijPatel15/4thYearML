#scheduler playground
import sched, time
import spidev
from EventByteConverter import dataFrameToByteConverter

def send_event(note=None):
    # print("Notes", time.time(), note) #change this to actually send something when implemented
    spi = spidev.SpiDev()
    messageToSend = dataFrameToByteConverter(note)
    resp = spi.xfer2([messageToSend])
    print(resp)
    
def schedule_events(df, s):
    if df.empty:
        raise Exception("No events provided.")
    s.enter(3,1,send_event, argument=('CLAP CLAP CLAP',))
    for index, row in df.head(n=len(df)).iterrows():
        time =row['timeOffset']
        note = row['name']
        s.enter(3+time, 1, send_event, argument=(row,))