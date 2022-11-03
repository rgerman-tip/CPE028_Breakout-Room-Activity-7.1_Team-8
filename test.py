import unittest
import backend as mg

class testMapQuest(unittest.TestCase):
    print('[Running Test Cases]\n')
    def test_conversion_MarikinaTondo(self):
        convert = mg.conversionFunc('Marikina','Tondo','down')
        self.assertIsNotNone(convert)
        print(f"[Check API Call Marikina To Tondo]")

    def test_conversion_ManilaBaguio(self):
        convert = mg.conversionFunc('Manila','Baguio','down')
        self.assertIsNotNone(convert)
        print(f"[Check API Call Manila To Baguio]")

    def test_conversion_TokyoKyoto(self):
        convert = mg.conversionFunc('Tokyo','Kyoto','down')
        self.assertIsNotNone(convert)
        print(f"[Check API Call Tokyo To Kyoto]")

    def test_conversion_NYLA_normal(self):
        convert = mg.conversionFunc('new york','los angeles','normal')
        self.assertIsNotNone(convert)
        print(f"[Check API Call Tokyo To Kyoto]")
    def test_conversion_NYLA_down(self):
        convert = mg.conversionFunc('new york','los angeles','down')
        self.assertIsNotNone(convert)
        print(f"[Check API Call Tokyo To Kyoto]")
