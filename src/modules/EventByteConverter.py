import MidiParser
from ByteConstTable import getByteFromNote, noteVals

def dataFrameToByteConverter(event):
    finalByteArray = bytearray()
    colVal = event.loc["event"]
    noteVal = event.loc["name"]
    assert(validateValues(colVal, noteVal)), "Event and Note values are not valid or are empty."
    if colVal is 'Note':
        finalByteArray.append(bytes(getByteFromNote(noteVal))[0] & 255)
    if colVal is 'Chord':
        for val in noteVal:
            finalByteArray.append(bytes(getByteFromNote(val))[0] & 127)
    return finalByteArray

def validateValues(eventVal, noteVal):
    isValid = False
    notFound = False
    acceptedEventVals = ["Note", "Chord"]
    if (eventVal and noteVal and eventVal in str(acceptedEventVals)):
        if (eventVal is 'Chord'):
            for val in noteVal:
                if val not in noteVals:
                    notFound = True
        if not notFound:
            isValid = True
    return isValid


events = MidiParser.parse_notes('../music/i_see_fire.mid')

for x in range(1, len(events.index)):
    dataFrameToByteConverter(events.iloc[x])
