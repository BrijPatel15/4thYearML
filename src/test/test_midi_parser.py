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
        test=dict(id=0,event="Note", name="C1")
        test2=dict(id=1,event="Note", name="")
        test3=dict(id=2,event="Chord", name=["C1", "B1"])
        test4=dict(id=3,event="Chord", name=[])
        test5=dict(id=4,event="fail", name="")

        expected = True
        actual = eventConverter.validateValues(test['event'], test['name'])
        res = eventConverter.dataFrameToByteConverter(test['name'], test['event'])
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)
        self.assertEqual(res[0], getByteFromNote("C1")[0])

        expected = True
        actual = eventConverter.validateValues(test3["event"], test3["name"])
        res = eventConverter.dataFrameToByteConverter(test3['name'], test3['event'])
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)
        self.assertEqual(res[0], getByteFromNote("C1")[0])
        self.assertEqual(res[1], getByteFromNote("B1")[0])

        expected = False
        actual = eventConverter.validateValues(test2["event"], test2["name"])
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)

        expected = False
        actual = eventConverter.validateValues(test4["event"], test4["name"])
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)
        
        expected = False
        actual = eventConverter.validateValues(test5["event"], test5["name"])
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)


    def test_parse(self):
        # self.fail('Not implemented yet.')
        print('Not implemented yet.')
    
