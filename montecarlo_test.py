import unittest
from montecarlo import *

class montecarlotest(unittest.TestCase):
    
    # Die Class Tests
    
    def test_1_change_weight(self): 
        testcase = die(['H', 'T'])
        testcase.change_weight('H', 5)
        self.assertTrue(testcase.weights == [5.0, 1.0])
    
    def test_2_roll_die(self):
        testcase = die(['H', 'T'])
        rolls = testcase.roll_die(5)
        test = True
        for each in rolls:
            if each not in testcase.faces:
                test = False
        condition1 = test == True 
        condition2 = (len(rolls) == 5) 
        self.assertTrue(condition1 and condition2)
    
    def test_3_display(self):
        testcase = die(['H', 'T'])
        testcase.change_weight('H', 5)
        df = testcase.display()
        self.assertTrue(list(df['Weight']) == testcase.weights)
    
    # Game Class Tests
    
    def test_4_play(self):
        testcase = game()
        testcase.play(100)
        self.assertTrue(len(testcase.__playdf__)==100)
    
    def test_5_show_rolls(self):
        testcase = game()
        testcase.play(100)
        df = testcase.show_rolls()
        self.assertTrue(len(df)==100)
    
    # Analyzer Class Tests
    
    def test_6_jackpot(self):
        game1 = game()
        game1.play(100)
        testcase = analyzer(game1)
        x = testcase.jackpot()
        self.assertTrue(x == len(testcase.jpdf))
        
    def test_7_sequence(self):
        game2 = game()
        game2.play(100)
        testcase = analyzer(game2)
        x = testcase.sequence()
        condition1 = (len(testcase.sdf) == len(x))
        condition2 = len(x) <= 100
        self.assertTrue(condition1 and condition2) 
        
    def test_8_combo(self):
        game3 = game()
        game3.play(100)
        testcase = analyzer(game3)
        x = testcase.combo()
        condition1 = (len(testcase.cdf) == len(x))
        condition2 = len(x) <= 100
        self.assertTrue(condition1 and condition2)  
        
    def test_9_counts(self):
        game4 = game()
        game4.play(100)
        testcase = analyzer(game4)
        df = testcase.counts()
        self.assertTrue(len(df)==100)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
        