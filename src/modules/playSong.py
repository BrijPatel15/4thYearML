import sys, os, sched, time
from MidiParser import parse_notes, validate_file
from NoteEventScheduler import schedule_events
dir_path = os.path.dirname(os.path.realpath(__file__))
# MUSIC_PATH = "../../music/guitar.mid"
if (len(sys.argv)<2):
    MUSIC_PATH = "../music/guitar.mid"
    dir_path = dir_path+MUSIC_PATH
else:
    MUSIC_PATH = sys.argv[1]
    dir_path = dir_path+MUSIC_PATH

validate_file(MUSIC_PATH)
events = parse_notes(MUSIC_PATH)

s =sched.scheduler(time.time, time.sleep)
schedule_events(events, s)
s.run()


