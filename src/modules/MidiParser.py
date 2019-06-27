import os
import sys
import logging
from music21 import converter, instrument, tempo
import pandas as pd

logger = logging.getLogger('flask.app')
# Need a standard in terms of representing the events as a structure.
# It will be a list of dict. List of events (events being, a note, rest, or a chord)
# So parse_midi_events will return the following
# [ {...}, {...}], where {...}, can be any note, rest, or chord event (so it can be put in a Pandas dataframe)
# see python notebook for more detials, or if you wanna play around with this
def parse_notes(path):
    id=0 #unique id for the py dict 
    midiFile = converter.parse(path)
    instr = instrument.Guitar
    instrument_notes = []
    bpm = get_tempo(path)
    startTime=0
    for part in instrument.partitionByInstrument(midiFile):
        if isinstance(part.getInstrument(), instr):
            for events in part.notes:
                if getattr(events,'isNote', None) and events.isNote:
                    instrument_notes.append(dict(id=id,event="Note",name=events.nameWithOctave, quarterLength=events.duration.quarterLength, timeOffset=startTime,part=part.partName))
                    startTime+=get_duration_seconds(bpm,events.duration.quarterLength ) # offset the time based on note duration
                if getattr(events,'isChord', None) and events.isChord: # if its a chord get the group of notes 
                    chord_notes = [] 
                    for c in events._notes:
                        chord_notes.append(c.nameWithOctave)
                    instrument_notes.append(dict(id=id,event="Chord", name=chord_notes, quarterLength=events._notes[0].duration.quarterLength, timeOffset=startTime,part=part.partName))
                    startTime+=get_duration_seconds(bpm,events.duration.quarterLength )
                id+=1
    return pd.DataFrame(instrument_notes)

def validate_file(fileName):
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

def get_tempo(path):
    midiFile = converter.parse(path)
    instr = instrument.Guitar
    bpm= tempo.MetronomeMark
    for part in instrument.partitionByInstrument(midiFile):
        if isinstance(part.getInstrument(), instr):
            for events in part:
                if isinstance(events, bpm):
                    return events.getQuarterBPM()

def get_duration_seconds(bpm, quarterLength):
    #convert bpm -> hz
    freq = 1/(bpm/60)
    return ((freq)*(quarterLength/4))/(1/4) #1 beat is a quarter note.

# print(parse_midi_events("../../music/John_Denver_-_Take_Me_Home_Country_Roads.mid"))
# print(validateMidi('John_Denver_-_Take_Me_Home_Country_Roads.mid'))
