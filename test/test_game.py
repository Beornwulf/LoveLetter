'''
Created on 1 Mar 2014

@author: Dominic
'''
import unittest, game


class Test(unittest.TestCase):


    def setUp(self):
        self.testGame = game.Game(4)


    def testSize(self):
        self.assertEqual(len(self.testGame.playerList), 4)
    
    def testNames(self):
        i = 0
        while i < len(self.testGame.playerList): 
            self.assertEqual(self.testGame.playerList[(i)].name, ("Player " + str(i + 1)))
            i += 1


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()