'''
Created on 1 Mar 2014

@author: Dominic
'''
import unittest
import card


class TestBasicInfo(unittest.TestCase):

    def setUp(self):
        self.testCard = card.Princess()

    def testBasicInfo(self):
        info = self.testCard.basic_info()
        self.assertTrue(type(info) is str)
        self.assertEqual(len(info), 35)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()