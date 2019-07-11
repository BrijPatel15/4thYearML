import unittest
import sys
import pandas as pd
import MidiParser as midi
import EventByteConverter as eventConverter
from ByteConstTable import getByteFromNote, noteVals

class MidiParserTestCase(unittest.TestCase):

    
    def test_validate(self):

        GOOD_MIDI_PATH_1 = "../music/John_Denver_-_Take_Me_Home_Country_Roads.mid"
        GOOD_MIDI_PATH_2 = "../music/i_see_fire.mid"
        BAD_MIDI_PATH_1 = "../music/bad-John_Denver_-_Take_Me_Home_Country_Roads.mid"
        BAD_MIDI_PATH_2 = "../music/bad-guitar.mid"

        expected = True
        actual = midi.validate_file(GOOD_MIDI_PATH_1)
        print(GOOD_MIDI_PATH_1)
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))

        expected = True
        actual = midi.validate_file(GOOD_MIDI_PATH_2)
        print(GOOD_MIDI_PATH_2)
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)

        expected = False
        actual = midi.validate_file(BAD_MIDI_PATH_1)
        print(BAD_MIDI_PATH_1)
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)

        expected = False
        actual = midi.validate_file(BAD_MIDI_PATH_2)
        print(BAD_MIDI_PATH_2)
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)

    def test_EventConverter(self):
        test=[]
        test2 = []
        test3 = []
        test4 = []
        test5 = []
        test.append(dict(id=0,event="Note", name="C1"))
        test2.append(dict(id=1,event="Note", name=""))
        test3.append(dict(id=2,event="Chord", name=["C1", "B1"]))
        test4.append(dict(id=3,event="Chord", name=[]))
        test5.append(dict(id=4,event="fail", name=""))

        expected = True
        df = pd.DataFrame(test)
        goodEve = df.iloc[0]
        actual = eventConverter.validateValues(goodEve.loc["event"], goodEve.loc["name"])
        res = eventConverter.dataFrameToByteConverter(goodEve)
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)
        self.assertEqual(res[0], getByteFromNote("C1")[0])

        expected = True
        df2 = pd.DataFrame(test3)
        goodEveChord = df2.iloc[0]
        actual = eventConverter.validateValues(goodEveChord.loc["event"], goodEveChord.loc["name"])
        res = eventConverter.dataFrameToByteConverter(goodEveChord)
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)
        self.assertEqual(res[0], getByteFromNote("C1")[0])
        self.assertEqual(res[1], getByteFromNote("B1")[0])

        expected = False
        df3 = pd.DataFrame(test2)
        badEve = df3.iloc[0]
        actual = eventConverter.validateValues(badEve.loc["event"], badEve.loc["name"])
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)

        expected = False
        df4 = pd.DataFrame(test4)
        badChord = df4.iloc[0]
        actual = eventConverter.validateValues(badChord.loc["event"], badChord.loc["name"])
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)
        
        expected = False
        df5 = pd.DataFrame(test5)
        badOverAll = df5.iloc[0]
        actual = eventConverter.validateValues(badOverAll.loc["event"], badOverAll.loc["name"])
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)


    def test_parse(self):
        # self.fail('Not implemented yet.')
        print('Not implemented yet.')
    
