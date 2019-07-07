import MidiParser

def dataFrameToByteConverter(event):
    acceptedValues = ["event", "name"]
    for val in acceptedValues:
        assert(val in str(event.columns.values))
    finalByte = b'\xFF'
    for value in acceptedValues:
        rowVal = event.at[0,value]
        if rowVal is 'Note':
            finalByte = finalByte[0] & b'\x4F'[0]
        if rowVal is 'Chord':
            finalByte = finalByte[0] & b'\x2F'[0]
        else:
            finalByte = finalByte[0] & getByteFromNote(rowVal)
    return finalByte
        
def getByteFromNote(note):
    noteVals = {
    }
    return noteVals.get(note)

events = MidiParser.parse_notes('/music/John_Denver_-_Take_Me_Home_Country_Roads.mid')
for event in events:
    dataFrameToByteConverter(event)
