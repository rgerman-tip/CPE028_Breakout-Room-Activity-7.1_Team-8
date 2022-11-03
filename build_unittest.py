import unittest
from mapquest_gui import *

class TestInput(unittest.TestCase):
    def executeApp(self):
        app = MapQuest()
        self.assertEqual(app.build(), self.screen)

if __name__ == '__main__':
    unittest.main()
