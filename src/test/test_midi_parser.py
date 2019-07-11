import unittest
import sys
import pandas as pd
import MidiParser as midi
import EventByteConverter as eventConverter
from ByteConstTable import *

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
        goodEvent = pd.DataFrame(dict(event="Note", name="C1"))
        badEvent = pd.DataFrame(dict(event="Note", name="fail"))
        goodChord = pd.DataFrame(dict(event="Chord", name=["C1", "B1"]))
        badChord = pd.DataFrame(dict(event="Chord", name=[]))
        badOverAll = pd.DataFrame(dict(event="fail" name="fail"))

        expected = True
        actual = validateValues(goodEvent.loc["event"], goodEvent.loc["name"])
        res = eventConverter.dataFrameToByteConverter(goodEvent)
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)
        self.assertEqual(res[0], getByteFromNote("C1")[0])

        expected = True
        actual = validateValues(goodChord.loc["event"], goodChord.loc["name"])
        res = eventConverter.dataFrameToByteConverter(goodChord)
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)
        self.assertEqual(res[0], getByteFromNote("C1")[0])
        self.assertEqual(res[1], getByteFromNote("B1")[0])

        expected = False
        actual = validateValues(badEvent.loc["event"], badEvent.loc["name"])
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)

        expected = False
        actual = validateValues(badChord.loc["event"], badChord.loc["name"])
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)
        
        expected = False
        actual = validateValues(badOverAll.loc["event"], badOverAll.loc["name"])
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)


    def test_parse(self):
        # self.fail('Not implemented yet.')
        print('Not implemented yet.')
    
