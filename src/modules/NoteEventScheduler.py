# scheduler playground
import sched, time
import spidev
from EventByteConverter import dataFrameToByteConverter
from ByteConstTable import getByteFromNote, findEqualNote, getNoteString, getNoteCanPlay


def send_event(name=None, event=None, iterator=None):
    spi = spidev.SpiDev()
    if (name != 'CLAP CLAP CLAP'):  # only send real notes not fake syncing ones
        spi.open(0, 1)
        spi.max_speed_hz = 500000
        spi.mode = 0
        if event is 'Note':
            messageToSend = dataFrameToByteConverter(name, event)
            resp = spi.xfer2([messageToSend[0]])
            print("Note: ", iterator)
            print("Byte sent is: ", messageToSend[0])
            print("Int Value is: ", int.from_bytes(messageToSend, "big"))
        if event is 'Chord':
            name = validateChord(name)
            for val in name:
                messageToSend = dataFrameToByteConverter(val, event)
                for messages in messageToSend:
                    resp = spi.xfer2([messages])
                    print("Note: ", iterator)
                    print("Byte sent is: ", messages)
                    print("Int Value is: ", int.from_bytes(messageToSend, "big"))
                    print(resp)
        spi.close()  # Added this change bc the docs recommend it we can remove it.


def validateChord(notes=None):
    stringsUsed = []
    finalNotes = []
    for note in notes:
        noteString = getNoteString(note)
        if (noteString not in stringsUsed and getNoteCanPlay(note)):
            stringsUsed.append(noteString)
            finalNotes.append(note)
        else:
            newNote, newString = findEqualNote(note, getNoteString(note))
            stringsUsed.append(newString)
            finalNotes.append(newNote)
    return finalNotes


def schedule_events(df, s):
    if df.empty:
        raise Exception("No events provided.")
    s.enter(3, 1, send_event, argument=('CLAP CLAP CLAP',))
    iterator = 1
    for index, row in df.head(n=len(df)).iterrows():
        times = row['timeOffset']
        name = row['name']
        event = row['event']
        s.enter(3 + times, 1, send_event, argument=(name, event, iterator))
        iterator = iterator + 1

#
# notes = ['E1', 'F1', 'C3']
# validateChord(notes=notes)
