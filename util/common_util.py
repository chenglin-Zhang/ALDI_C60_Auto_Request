import unittest

class CommonUtil(unittest.TestCase):

  def is_contain(self, str_one, str_two):
    message = "key is present in container."
    try:
      self.assertIn(str_one, str_two, message)
      return True
    except Exception as e:
      print(e)
      return False


