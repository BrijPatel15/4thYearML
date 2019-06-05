import os 
import sys 
from music21 import *


def validateMidi(fileName):
    path = os.path.abspath(fileName)
    if os.path.exists(path):
        print (path)

    isValid = True
    try:
        c = converter.Converter()
        c.parseFile(path)
        stream = c.stream
        if (stream.duration is None or stream.elements is None or
            stream.flat is None or stream.notes is None or
            stream.notesAndRests is None or stream.parts is None or
            stream.pitches is None or stream.secondsMap is None):
            isValid = False;
    except:
        isValid = False

    return isValid

validateMidi('/home/brij/Desktop/4thYearProj/4thYearML/src/midiParser/John_Denver_-_Take_Me_Home_Country_Roads.mid')



