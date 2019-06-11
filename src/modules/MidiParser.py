import os
import sys
from music21 import *

def parse_midi_events(path):
    midiFile = converter.parse(path)
    instr = instrument.Guitar
    instrument_notes = []
    for part in instrument.partitionByInstrument(midiFile):
        if isinstance(part.getInstrument(), instr):
            for events in part:
                for event in events.contextSites():
                    if event[0] is part:
                        offset = event[1]
                    if getattr(events, 'isRest', None) and events.isRest:
                        instrument_notes.append(dict(name="Rest", beat=events.duration.type, quarterLength=events.duration.quarterLength, timeOffset=offset))
                    if getattr(events, 'isNote', None) and events.isNote:
                        instrument_notes.append(dict(name=events.nameWithOctave, beat=events.duration.type, quarterLength=events.duration.quarterLength, timeOffset=offset))
                    if getattr(events, 'isChord', None) and events.isChord:
                        chord = []
                        for x in events._notes:
                            chord.append(dict(name=x.nameWithOctave, beat=x.duration.type, quarterLength=x.duration.quarterLength, timeOffset=offset))
                        instrument_notes.append(chord)
    return instrument_notes

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

# print(parse_midi_events("../../music/John_Denver_-_Take_Me_Home_Country_Roads.mid"))
# print(validateMidi('John_Denver_-_Take_Me_Home_Country_Roads.mid'))
