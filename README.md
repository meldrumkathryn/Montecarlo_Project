# DS5100_Final

# METADATA:

Montecarlo package

Author: Kate Meldrum

Author email: kmm4ap@virginia.edu

# MANIFEST:
1) montecarlo.py: contains code for classes and method
2) montecarlo_test.py: contains code for unittesting montecarlo.py
3) montecarlo_test_results.txt: contains the results of the unittesting
4) montecarlo_demo.ipynb: A jupyter notebook that contains a walkthrough of methods and attributes
5) sgb_words.txt: contains five letter words published by scrabble for example in demo
6) scrab.py: converts sgb_words.txt to list varible to be used in example in demo
7) README.md: this readme file
8) LICENSE.md: license, type MIT


# CLASSES AND METHODS: 

## 1) install/import code

install package in terminal using the following code within directory where the package is downloaded: 

! pip install -e .

install classes to workspace using

from monte.montecarlo import *

## 2) Creating a Die:

To create a die, pass in a list of faces you would like your die to have to the die class, faces can be int, float, bool, or string class, and the die can have any number of faces:

die_object = die([1,2,3,4,5,6])

docstring: 
        purpose: create instance of class die
        param: <list> of faces on die
        return: None

atributes:
        die_object.faces = a list of faces belonging to the die object 
        
        die_object.weights = a list of weights corresponding to die object faces


## 3) Change die weight:

Use the change_weight function which takes two arguments; the face value to be changed and the weight to change it to. For example, to weight the '1' face of the die we just created by a factor of 3 we would use the code: 

die_object.change_weight(1, 3)
    
docstring:
        purpose: change weight given to a face of die in roll 
        param1: <string, int, float> face to weight 
        param2: <int or float> weight to be given to face 
        return: None

  In practice, weighting a face by a factor of 3 means that die becomes 3 times more likely to be rolled than a face with a weight of 1.     
        
## 4) Roll a die: 

To roll a die, we use the roll_die function and pass in the number of times we want a die to be rolled. For example, this code will ouput a randomized list of 4 face values in our die object:

die_object.roll_die(4)
    
docstring: 
        purpose: return a random face of die with condiseration to weights
        param: <int >number of rolls 
        return: <list> face values

## 5) Display the current faces and weights of a die object:

The current faces and weights of our die object can be shown using the display function, this returns a dataframe with index of die faces and values of face weights:

die_object.display()
    
docstring:
        purpose: user can see faces and weights of die instance
        return: dataframe

## 6) Creating a game:

To create a game class object, simply pass in a list of dice to be involved in the game into the game class. If no dice are passed in the game will default to having 6 standard dice (faces 1-6), but if we wanted to play a game with two of our custom die objects this is what we would use:

game_object = game([die_object,die_object])
    
docstring: 
        purpose: create and isntance of a game
        param: <list of class die> , all dice must have same number of faces
        return: None

atributes:
        game_object.die_object = references the die with name die_object within game object, this allows you to (for example) display the properites of the die or change it's weight after the game object is created. 
        game_object.die_list = the original list of dice passed into the game object 

## 7) Play a game:

Playing a game means rolling all game dice a certain number of times. We can do this by passing a number of times to be rolled to the play function. This defaults to 100 if a value is not entered:

game_object.play(20)
    
docstring:
        purpose: roll each die in game a number of times and imput face values into global dataframe
        param: <int> number of rolls
        return: None

## 8) Show the rolls

After calling the play function, in order to see the results, call the show_rolls function. This has an optional boolean argument (wide= True) or (wide= False) to produce a wide or narrow dataframe, respectively:

game_object.show_rolls(wide = True)
    
docstring:
        purpose: display results of play function to user
        param: <bool> indicating wide or narrow, defaults to wide
        return: dataframe 

## 9) Create an analyzer class

To create an analyzer class, pass a game into the analyzer function

analyzer_object = analyzer(game_object)
    
docstring:
        purpose: create and instance of analyzer class
        param: instance of class game
        return: None
    
attributes:
        self.game = game object passed in
        self.data_type = shows the data type of the faces of dice rolled in game.play
        self.jpdf = dataframe of jackpots
        self.freq_sdf = frequency oriented dataframe of sequences
        self.sdf = sequence oriented dataframe of sequences
        self.freq_cdf = frequency oriented dataframe of combinations
        self.cdf = combination oriented dataframe of combinations
        self.countsdf = dataframe of the face counts of each roll
        
    

**If no game object is passed a default analyzer object will be created with a default game (as discribed above) that was played with 100 rolls. 

**Note that if you pass your own game object to analyzer and haven't played a game with that game many of the analyzer functions won't work as they depend on a dataframe of play results. 

## 10) Find jackpots

A jackpot is when all dice roll to have the same face. The number of jackpots in a game can be found by running the jackpot function on our analyzer object: 

analyzer_object.jackpot()

A dataframe of all jackpot rolls (roll number, roll) can be accessed as an atribute called jpdf

analyzer_object.jpdf

docstring:
        purpose: counts the number of rolls in game all dices showed an identical face
        return: <int> number of occurances

## 11) Find unique sequences

Two dataframes of unique sequences can be accessed using the montecarlo package. A dataframe that has each term of a roll sequence represented as a multiindex and frequency represented in a data column can be produced with the following:

analyzer_object.sequence(freq = False)

A dataframe that has an index of each sequence, a column containing roll numbers with this sequence, and column containing the total number of rolls with this sequence can be accessed as such:

analyzer_object.sequence(freq = True)

as the argument suggests, this dataframe is sorted by frequence from greatest to least and is helpful when trying to see the most frequently rolled sequences. 
    
docstring:
        purpose: method to compute the number of distinct sequences of faces rolled
        param: freq=True/False to sort by frequency or not, defaults to false
        return: dataframe

## 12) Find unique combinations

Similarly to the sequence the combo function can be used to create the same two formats of dataframe, but without taking account of which dice rolled which face. These two dataframes can be similarly displayed with the following code:

analyzer_object.combo(freq = False)
analyzer_object.combo(freq = True)

docstring:
        purpose: method to compute a dataframe of distinct combinations of faces rolled
        param: freq = True/False to sort by frequency or not, defaults to false
        return: dataframe

## 13) Find counts of faces in each roll

We can represent each roll as a list of the frequency of each face using the counts function. This will produce a frequency dataframe, for example a roll from dice with faces [1,2,3,4,5,6] that contained [1,4,1,4,3] would be represented as [2,0,1,2,0,0].

This dataframe is produced with the following code:

analyzer_object.counts()
    
docstring:
        purpose: method to compute how many times a given face is rolled in each event
        return: dataframe
