import os
import sys
from music21 import *

fn = sys.argv[1]
path = os.path.abspath(fn)
if os.path.exists(path):
    print (path)

midiFile = converter.parse(path)
all_instruments = []
for part in midiFile.parts:
  instrument = []
  print(part.partName)
  for event in part:
    for y in event.contextSites():
      if y[0] is part:
        offset = y[1]
    if getattr(event, 'isNote', None) and event.isNote:
      instrument.append(dict(name=event.nameWithOctave, beat=event.quarterLength, timeOffset=offset))
    if getattr(event, 'isRest', None) and event.isRest:
      instrument.append(dict(name="Rest", beat=event.quarterLength, timeOffset=offset))
  all_instruments.append(instrument)

# To view all notes
#print(all_instruments)
