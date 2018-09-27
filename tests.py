import unittest
import inspect

class TestClass01(unittest.TestCase):

  def test_case01(self):
    my_str = "ASHWIN"
    my_int = 999
    self.assertTrue(isinstance(my_str, str))
    self.assertTrue(isinstance(my_int, int))

  def test_case02(self):
    my_pi = 3.14
    self.assertTrue(isinstance(my_pi, float))

if __name__ == '__main__':
  unittest.main()
