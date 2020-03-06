def getByteFromNote(note):
    return noteVals.get(note)[0]


def getNotesOnString(string):
    notesOnString = []
    for key, value in noteVals.items():
        for v in value:
            if v == string:
                notesOnString.append(key)


def getNoteString(note):
    for key, value in noteVals.items():
        if key == note:
            return noteVals[key][1]


def getNoteCanPlay(note):
    for key, value in noteVals.items():
        if key == note:
            return noteVals[key][2]


def findEqualNote(note, string):
    whitelist = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ#')
    basicNote = ''.join(filter(whitelist.__contains__, note))
    for key, value in noteVals.items():
        if basicNote in key and value[1] != string and value[2] is True:
            return key, value[1]


# first 2 and last 4
# Layout [byte representation, string, canPlay]
noteVals = {
    "E1": [b'\x01', 1, False],
    "F1": [b'\x02', 1, False],
    "F#1": [b'\x03', 1, True],
    "G1": [b'\x04', 1, True],
    "G#1": [b'\x05', 1, True],
    "A1": [b'\x06', 1, True],
    "A#1": [b'\x07', 1, True],
    "B1": [b'\x08', 1, True],
    "C1": [b'\x09', 1, True],
    "C#1": [b'\x0A', 1, False],
    "D1": [b'\x0B', 1, False],
    "D#1": [b'\x0C', 1, False],
    "E2": [b'\x0D', 1, False],
    "B2": [b'\x0E', 2, False],
    "C2": [b'\x0F', 2, False],
    "C#2": [b'\x10', 2, True],
    "D2": [b'\x11', 2, True],
    "D#2": [b'\x12', 2, True],
    "E3": [b'\x13', 2, True],
    "F2": [b'\x14', 2, True],
    "F#2": [b'\x15', 2, True],
    "G2": [b'\x16', 2, True],
    "G#2": [b'\x17', 2, False],
    "A2": [b'\x18', 2, False],
    "A#2": [b'\x19', 2, False],
    "B3": [b'\x1A', 2, False],
    "G3": [b'\x1B', 3, False],
    "G#3": [b'\x1C', 3, False],
    "A3": [b'\x1D', 3, True],
    "A#3": [b'\x1E', 3, True],
    "B4": [b'\x1F', 3, True],
    "C3": [b'\x20', 3, True],
    "C#3": [b'\x21', 3, True],
    "D3": [b'\x22', 3, True],
    "D#3": [b'\x23', 3, True],
    "E4": [b'\x24', 3, False],
    "F3": [b'\x25', 3, False],
    "F#3": [b'\x26', 3, False],
    "G-1": [b'\x27', 3, False],
    "D4": [b'\x28', 4, False],
    "D#4": [b'\x29', 4, False],
    "E5": [b'\x2A', 4, True],
    "F-1": [b'\x2B', 4, True],
    "F#4": [b'\x2C', 4, True],
    "G-2": [b'\x2D', 4, True],
    "G#4": [b'\x2E', 4, True],
    "A-1": [b'\x2F', 4, True],
    "A#4": [b'\x30', 4, True],
    "B-1": [b'\x31', 4, False],
    "C4": [b'\x32', 4, False],
    "C#4": [b'\x33', 4, False],
    "D5": [b'\x34', 4, False],
    "A5": [b'\x35', 5, False],
    "A#5": [b'\x36', 5, False],
    "B6": [b'\x37', 5, True],
    "C5": [b'\x38', 5, True],
    "C#5": [b'\x39', 5, True],
    "D6": [b'\x3A', 5, True],
    "D#5": [b'\x3B', 5, True],
    "E6": [b'\x3C', 5, True],
    "F5": [b'\x3D', 5, True],
    "F#5": [b'\x3E', 5, False],
    "G6": [b'\x3F', 5, False],
    "G#5": [b'\x40', 5, False],
    "A-2": [b'\x41', 5, False],
    "E7": [b'\x42', 6, False],
    "F6": [b'\x43', 6, False],
    "F#6": [b'\x44', 6, True],
    "G7": [b'\x45', 6, True],
    "G#6": [b'\x46', 6, True],
    "A7": [b'\x47', 6, True],
    "A#6": [b'\x48', 6, True],
    "B7": [b'\x49', 6, True],
    "C6": [b'\x4A', 6, True],
    "C#6": [b'\x4B', 6, False],
    "D7": [b'\x4C', 6, False],
    "D#6": [b'\x4D', 6, False],
    "E8": [b'\x4E', 6, False]
}
