import os
import sys
from music21 import *


def parse_midi_events(path):
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
  return all_instruments

def validate_midi(fileName):
    path = os.path.abspath(fileName)
    isValid = True
    try:
        c = converter.Converter()
        c.parseFile(path)
        stream = c.stream
        if (stream.duration is None or stream.elements is None or
            stream.flat is None or stream.notes is None or
            stream.notesAndRests is None or stream.parts is None or
            stream.pitches is None or stream.secondsMap is None):
            isValid = False
    except:
        isValid = False

    return isValid

# print(parse_events("John_Denver_-_Take_Me_Home_Country_Roads.mid"))
# print(validateMidi('John_Denver_-_Take_Me_Home_Country_Roads.mid'))