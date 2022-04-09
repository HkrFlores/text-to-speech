import unittest
from multiplefunctions import saveToText

class MyTestCase(unittest.TestCase):
    def testSaveToText(self):
        text = "This is a test text to save in file" \
               " continue with multi lines"
        filepath = 'text/testcase.txt'
        savedfile = saveToText(text, filepath)
        if savedfile:
            with open(filepath) as filetoread:
                textinfile = filetoread.readline()

        print(textinfile)
#        self.assertEqual(savedfile, true)  # add assertion here
        self.assertEqual(text, textinfile)


if __name__ == '__main__':
    unittest.main()
