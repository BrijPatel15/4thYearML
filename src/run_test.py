import unittest
import sys
sys.path.append("test/")
sys.path.append("modules/")
from test_master import master_suite

runner = unittest.TextTestRunner()
runner.run(master_suite())