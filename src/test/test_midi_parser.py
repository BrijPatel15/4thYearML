import unittest
import sys
import MidiParser as midi

class MidiParserTestCase(unittest.TestCase):

    
    def test_validate(self):

        GOOD_MIDI_PATH_1 = "../music/John_Denver_-_Take_Me_Home_Country_Roads.mid"
        GOOD_MIDI_PATH_2 = "../music/guitar.mid"
        BAD_MIDI_PATH_1 = "../music/bad-John_Denver_-_Take_Me_Home_Country_Roads.mid"
        BAD_MIDI_PATH_2 = "../music/bad-guitar.mid"

        expected = True
        actual = midi.validate_midi(GOOD_MIDI_PATH_1)
        print(GOOD_MIDI_PATH_1)
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))

        expected = True
        actual = midi.validate_midi(GOOD_MIDI_PATH_2)
        print(GOOD_MIDI_PATH_2)
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)

        expected = False
        actual = midi.validate_midi(BAD_MIDI_PATH_1)
        print(BAD_MIDI_PATH_1)
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)

        expected = False
        actual = midi.validate_midi(BAD_MIDI_PATH_2)
        print(BAD_MIDI_PATH_2)
        print("Expected: "+ str(expected) + " ==> Actual: "+str(actual))
        self.assertEqual(expected, actual)


    def test_parse(self):
        self.fail('Not implemented yet.')
    
