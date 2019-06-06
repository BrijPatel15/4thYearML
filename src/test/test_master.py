import unittest
from test_midi_parser import MidiParserTestCase

def master_suite():
    suite = unittest.TestSuite()
    suite.addTest(MidiParserTestCase('test_validate'))
    suite.addTest(MidiParserTestCase('test_parse'))
    return suite
