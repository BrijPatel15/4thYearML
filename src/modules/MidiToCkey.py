# http://nickkellyresearch.com/python-script-transpose-midi-files-c-minor/
import music21
#converting everything into the key of C major or A minor
# major conversions
majors = dict([(“A-“, 4),(“G#”, 4),(“A”, 3),(“A#”, 2),(“B-“, 2),(“B”, 1),(“C”, 0),(“C#”, -1),(“D-“, -1),(“D”, -2),(“D#”, -3),(“E-“, -3),(“E”, -4),(“F”, -5),(“F#”, 6),(“G-“, 6),(“G”, 5)])
minors = dict([(“G#”, 1), (“A-“, 1),(“A”, 0),(“A#”, -1),(“B-“, -1),(“B”, -2),(“C”, -3),(“C#”, -4),(“D-“, -4),(“D”, -5),(“D#”, 6),(“E-“, 6),(“E”, 5),(“F”, 4),(“F#”, 3),(“G-“, 3),(“G”, 2)])

def note_detect(file):
    score = music21.converter.parse(file)
    key = score.analyze('key')

    if key.mode == "major":
            halfSteps = majors[key.tonic.name]
    elif key.mode == "minor":
            halfSteps = minors[key.tonic.name]
        newscore = score.transpose(halfSteps)
        key = newscore.analyze('key')
    print key.tonic.name, key.mode
        newFileName = "C_" + file
        newscore.write('midi',newFileName)
