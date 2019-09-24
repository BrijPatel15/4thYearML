from ByteConstTable import getByteFromNote, noteVals

def dataFrameToByteConverter(name, event):
    finalByteArray = bytearray()
    assert(validateValues(event, name)), "Event and Note values are not valid or are empty."
    if event is 'Note':
        finalByteArray.append(bytes(getByteFromNote(name))[0] & 255)
    if event is 'Chord':
        finalByteArray.append(bytes(getByteFromNote(name))[0] & 127)
    return finalByteArray

def validateValues(eventVal, noteVal):
    isValid = False
    notFound = False
    acceptedEventVals = ["Note", "Chord"]
    if (eventVal in str(acceptedEventVals)):
        if noteVal not in noteVals:
            notFound = True
        if not notFound:
            isValid = True
    return isValid


def motorToByte(motorNum, steps): #To enable test mode send 255 and to disable send 0; after 255 all the byte values will be taken as is
    finalByteArray = bytearray()
    assert(int(motorNum) > 0 and int(steps) > 0), "Must have motor number and steps"
    finalByteArray.append(motorNum & 255)
    finalByteArray.append(steps & 255)
    return finalByteArray


# events = MidiParser.parse_notes('../music/i_see_fire.mid')

# for x in range(0, len(events.index)):
#     dataFrameToByteConverter(events.iloc[x])
