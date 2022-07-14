import unittest
from monte.montecarlo import *

class montecarlotest(unittest.TestCase):
    
    # Die Class Tests
    
    def test_1_change_weight(self): 
        '''
        purpose: tests change_weight function for if the correct weight was changed to the correct value 
        '''
        testcase = die(['H', 'T'])
        testcase.change_weight('H', 5)
        self.assertTrue(testcase.weights == [5.0, 1.0])
        
    def test_1a_change_weight(self):
        '''
        purpose: tests change_weight funciton for if it only accepts ints/floats as the new weight values and only accepts current face as face argument
        '''
        testcase = die(['H', 'T'])
        condition1 = (testcase.change_weight('H', 'hi')==('Weight must be entered as float or int'))
        condition2 = (testcase.change_weight('L',4)==('Face does not exist on this die'))
        self.assertTrue(condition1 and condition2)
    
    def test_2_roll_die(self):
        '''
        purpose: tests roll_die function to make sure that faces returned on roll exist and the right number of faces are returned
        '''
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
        '''
        purpose: tests display function to see if the dataframe produced contains the correct weight values 
        '''
        testcase = die(['H', 'T'])
        testcase.change_weight('H', 5)
        df = testcase.display()
        self.assertTrue(list(df['Weight']) == testcase.weights)
    
    # Game Class Tests
    
    def test_4_play(self):
        '''
        purpose: tests play function to make sure that it creates a dataframe of the correct length (correct number of rolls are returned) and that the dataframe contains a number of columns equal to number of dice in game
        '''
        testcase = game()
        testcase.play(100)
        condition1 = len(testcase.__playdf__)==100
        condition2 = len(testcase.__playdf__.columns)==len(testcase.die_list)
        self.assertTrue(condition1 and condition2)
    
    def test_5_show_rolls(self):
        '''
        purpose: tests show_rolls function to make sure that it returns a dataframe of the correct length (correct number of rolls are returned) and that the dataframe contains a number of columns equal to number of dice in game
        '''
        testcase = game()
        testcase.play(100)
        df = testcase.show_rolls()
        condition1 = len(df)==100
        condition2 = len(df.columns)==len(testcase.die_list)
        self.assertTrue(condition1 and condition2)
    
    # Analyzer Class Tests
    
    def test_6_jackpot(self):
        '''
        purpose: tests jackpot function to make sure it returns a the number of jackpots as equal to the length of the created jackpot dataframe
        '''
        game1 = game()
        game1.play(100)
        testcase = analyzer(game1)
        x = testcase.jackpot()
        self.assertTrue(x == len(testcase.jpdf))
        
    def test_7_sequence(self):
        '''
        purpose: tests sequence function to see if it returns the correctly-dimensioned dataframe for both freqeuncy mode and multiindex mode
        '''
        game2 = game()
        game2.play(100)
        testcase = analyzer(game2)
        x = testcase.sequence()
        condition1 = (len(testcase.sdf) == len(x))
        condition2 = len(x.columns)== len(testcase.sdf.columns)
        y = testcase.sequence(freq=True)
        condition3 = (len(testcase.freq_sdf) == len(y))
        condition4 = len(y.columns)== len(testcase.freq_sdf .columns)
        self.assertTrue(condition1 and condition2 and condition3 and condition4) 
    
    def test_8_combo(self):
        '''
        purpose: tests combo function to see if it returns the correctly-dimensioned dataframe for both freqeuncy mode and multiindex mode
        '''
        game3 = game()
        game3.play(100)
        testcase = analyzer(game3)
        x = testcase.combo()
        condition1 = (len(testcase.cdf) == len(x))
        condition2 = len(x.columns)== len(testcase.cdf.columns)
        y = testcase.combo(freq=True)
        condition3 = (len(testcase.freq_cdf) == len(y))
        condition4 = len(y.columns)== len(testcase.freq_cdf.columns)
        self.assertTrue(condition1 and condition2 and condition3 and condition4) 
        
    def test_9_counts(self):
        '''
        purpose: tests if the counts function returns a dataframe of the correct dimensions
        '''
        game4 = game()
        game4.play(100)
        testcase = analyzer(game4)
        df = testcase.counts()
        condition1 = (len(df)==100)
        self.assertTrue(condition1)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
        