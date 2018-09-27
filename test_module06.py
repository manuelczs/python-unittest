# Running without unittest.main()

import unittest

class TestCase07(unittest.TestCase):

  def test_case01(self):
    self.assertTrue("PYTHON".isupper())
    print('\nIn test_case01()')

# without if __name__ == '__main__' we don't get
# output in the console
# The only way to run this module is to use Python
# iterpreter with the -m unittest option and the
# module name, as follows: pytho3 -m unittest test_module06
