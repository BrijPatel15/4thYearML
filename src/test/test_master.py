import unittest
from test_midi_parser import MidiParserTestCase
from test_scheduler import SchedulerTestCase
def master_suite():
    suite = unittest.TestSuite()
    suite.addTest(MidiParserTestCase('test_validate'))
    suite.addTest(MidiParserTestCase('test_parse'))
    suite.addTest(MidiParserTestCase('test_EventConverter'))
    return suite
