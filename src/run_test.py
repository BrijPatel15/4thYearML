import unittest
import sys
sys.path.append("test/")
sys.path.append("modules/")
from test_master import master_suite

runner = unittest.TextTestRunner()
ret = not runner.run(master_suite()).wasSuccessful()
sys.exit(ret)
