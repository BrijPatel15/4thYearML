#scheduler playground
import sched, time


def send_event(note=None):
    print("Notes", time.time(), note) #change this to actually send something when implemented
    
def schedule_events(df, s):
    if df.empty:
        raise Exception("No events provided.")
    s.enter(3,1,send_event, argument=('CLAP CLAP CLAP',))
    for index, row in df.head(n=len(df)).iterrows():
        time =row['timeOffset']
        note = row['name']
        s.enter(3+time, 1, send_event, argument=(note,))