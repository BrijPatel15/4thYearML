import music21
import MidiParser 

def dataFrameToByteConverter(events):
    totalRows = len(events.index)
    finalByteArray = bytearray()
    acceptedValues = ["event", "name"]
    for val in acceptedValues:
        assert(val in str(events.columns.values))
    for x in range(1, totalRows):
        colVal = events.ix[x, "event"]
        noteVal = events.ix[x, "name"]
        if colVal is 'Note':
            finalByteArray.append(int.from_bytes(b'\x08', "big"))
            finalByteArray.append(bytes(getByteFromNote(noteVal))[0])
        if colVal is 'Chord':
            finalByteArray.append(int.from_bytes(b'\x04', "big"))
            for val in noteVal:
                finalByteArray.append(bytes(getByteFromNote(val))[0])
    return finalByteArray
        
def getByteFromNote(note):
    noteVals = {
        "E1" : b'\x01',
        "F1" : b'\x02',
        "F#1": b'\x03',
        "G1" : b'\x04',
        "G#1": b'\x05',
        "A1" : b'\x06',
        "A#1": b'\x07',
        "B1" : b'\x08',
        "C1" : b'\x09',
        "C#1": b'\x0A',
        "D1" : b'\x0B',
        "D#1": b'\x0C',
        "E2" : b'\x0D',
        "B2" : b'\x0E',
        "C2" : b'\x0F',
        "C#2": b'\x10',
        "D2" : b'\x11',
        "D#2": b'\x12',
        "E3" : b'\x13',
        "F2" : b'\x14',
        "F#2": b'\x15',
        "G2" : b'\x16',
        "G#2": b'\x17',
        "A2" : b'\x18',
        "A#2": b'\x19',
        "B3" : b'\x1A',
        "G3" : b'\x1B',
        "G#3": b'\x1C',
        "A3" : b'\x1D',
        "A#3": b'\x1E',
        "B4" : b'\x1F',
        "C3" : b'\x20',
        "C#3": b'\x21',
        "D3" : b'\x22',
        "D#3": b'\x23',
        "E4" : b'\x24',
        "F3" : b'\x25',
        "F#3": b'\x26',
        "G-1" : b'\x27',
        "D4" : b'\x28',
        "D#4": b'\x29',
        "E5" : b'\x2A',
        "F-1" : b'\x2B',
        "F#4": b'\x2C',
        "G-2" : b'\x2D',
        "G#4": b'\x2E',
        "A-1" : b'\x2F',
        "A#4": b'\x30',
        "B-1" : b'\x31',
        "C4" : b'\x32',
        "C#4": b'\x33',
        "D5" : b'\x34',
        "A5" : b'\x35',
        "A#5": b'\x36',
        "B6" : b'\x37',
        "C5" : b'\x38',
        "C#5": b'\x39',
        "D6" : b'\x3A',
        "D#5": b'\x3B',
        "E6" : b'\x3C',
        "F5" : b'\x3D',
        "F#5": b'\x3E',
        "G6" : b'\x3F',
        "G#5": b'\x40',
        "A-2" : b'\x41',
        "E7" : b'\x42',
        "F6" : b'\x43',
        "F#6": b'\x44',
        "G7" : b'\x45',
        "G#6": b'\x46',
        "A7" : b'\x47',
        "A#6": b'\x48',
        "B7" : b'\x49',
        "C6" : b'\x4A',
        "C#6": b'\x4B',
        "D7" : b'\x4C',
        "D#6": b'\x4D',
        "E8" : b'\x4E'
    }
    return noteVals.get(note)

dataFrameToByteConverter(MidiParser.parse_notes('../music/John_Denver_-_Take_Me_Home_Country_Roads.mid'))