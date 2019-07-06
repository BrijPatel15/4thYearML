import music21
import MidiParser 

def dataFrameToByteConverter(events):
    totalRows = len(events.index)
    finalByteArray = bytearray()
    acceptedValues = ["event", "name"]
    for val in acceptedValues:
        assert(val in str(events.columns.values))

    for x in range(1, totalRows):
        for value in acceptedValues:
            finalByte = b'\xFF'
            rowVal = events.ix[x, value]
            if rowVal is 'Note':
                finalByte = finalByte[0] & b'\x4F'[0]
            if rowVal is 'Chord':
                finalByte = finalByte[0] & b'\x2F'[0]
            else:
                finalByte = finalByte[0] & getByteFromNote(rowVal)
            finalByteArray.append(finalByte)
    return finalByteArray
        
def getByteFromNote(note):
    noteVals = {

    }
    return noteVals.get(note)

dataFrameToByteConverter(MidiParser.parse_notes('../music/John_Denver_-_Take_Me_Home_Country_Roads.mid'))