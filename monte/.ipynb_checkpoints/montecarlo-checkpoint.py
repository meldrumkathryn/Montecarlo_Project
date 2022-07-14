import numpy as np
import pandas as pd
import random


# Shortcuts:

six_faces = [1, 2, 3, 4, 5, 6]


class die:
    
    '''
    A die has N sides, or “faces”, and W weights, and can be rolled to select a face
    '''
    
    def __init__(self,faces):
        
        '''
        purpose: create instance of class die
        param: <array> of faces on die
        return: None
        '''
        
        weights = [1.0 for x in faces] # Create default weights
        
        #die attributes
        self.faces = faces
        self.weights = weights
        self.__fwdf__ = pd.DataFrame(self.weights, index=self.faces)
        self.__fwdf__.columns = ['Weight']
        self.__fwdf__.index.name = 'Faces'
        
    def change_weight(self, face, weight):
        
        '''
        purpose: change weight given to a face of die in roll
        param1: <string, int, float> face to weight
        param2: <int or float> weight to be given to face 
        return: None
        '''
        
        # must be existing face and numeric weight
        if face in self.faces: 
            if type(weight)==float or type(weight)==int:
                i = self.faces.index(face)
                self.weights[i] = float(weight)
                self.__fwdf__ = pd.DataFrame(self.weights, index=self.faces)
                self.__fwdf__.columns = ['Weight']
                self.__fwdf__.index.name = 'Faces'
            else:
                return 'Weight must be entered as float or int'
        else: 
            return 'Face does not exist on this die'
            
    def roll_die(self, rolls=1):
        
        '''
        purpose: return a random face of die with condiseration to weights
        param: <int >number of rolls 
        return: <list> face values
        '''
        
        # random.choices pulls sample with replacement
        return random.choices(self.faces, weights=self.weights, k=rolls)
    
    def display(self):
        
        '''
        purpose: user can see faces and weights of die instance
        return: dataframe
        '''
        
        # allows users to access private face weight dataframe
        return self.__fwdf__


class game: 
    
    '''
    A game consists of rolling of one or more dice of the same list of faces one or more times
    '''
    
    # Default dice
    die1 = die(six_faces)
    die2 = die(six_faces)
    die3 = die(six_faces)
    die4 = die(six_faces)
    die5 = die(six_faces)
    die6 = die(six_faces)
    die_list = [die1,die2,die3,die4,die5,die6]
    
    __playdf__ = pd.DataFrame()# Empty data frame to be filled with game results and global amongst functions
    
    def __init__(self, die_list=die_list, __playdf__=__playdf__):
        
        '''
        purpose: create and isntance of a game
        param: <list of class die> , must have same number of faces
        return: None
        '''
        
        #attributes
        for die in die_list:
            self.die=die
        self.die_list=die_list
        self.__playdf__=__playdf__
        
    def play(self, n=100):
        
        '''
        purpose: roll each die in game a number of times and imput face values into global dataframe
        param: <int> number of rolls
        return: None
        '''
        
        #for each die, roll a certain amount of times and add to dictionary, create private dataframe when all dice have been rolled
        data = {}
        count=1
        for die in self.die_list:
            data["Die "+str(count)] = [die.roll_die()[0] for i in range(n)]
            count+=1
        self.__playdf__ = pd.DataFrame(data, index = range(1, n+1))
    
    def show_rolls(self, wide=True):
        
        '''
        purpose: display results of play function to user
        param: <bool> indicating wide or narrow, defaults to wide
        return: dataframe 
        '''
        
        # allow user to access private play dataframe
        if wide==True: 
            return self.__playdf__
        if wide == False:
            return self.__playdf__.stack()
        else:
            print('Expected argument: True or False')


class analyzer:
    '''
    takes the results of a single game and computes various descriptive statistical properties about it
    '''
    
    game = game()
    game.play()
    
    
    def __init__(self, game=game): 
        '''
        purpose: create and instance of analyzer class
        param: instance of class game
        return: None
        '''
        
        #attributes
        self.game = game
        self.data_type = type(game.show_rolls().iloc[1,1])
        self.jpdf = pd.DataFrame()
                              
    def jackpot(self):
        '''
        purpose: counts the number of rolls in game all dices showed an identical face
        return: <int> number of occurances
        '''
        
        #creates public dataframe, returns length
        df = self.game.show_rolls(True)
        rolls_lst = []
        count = 1
        for i in range(len(df)):
            rolls_lst.append(list(df.iloc[i,:]))
        for roll in rolls_lst:
            if len(set(roll))==1:
                self.jpdf[count]=roll
            count += 1
        self.jpdf = self.jpdf.T
        self.jpdf.index.name = 'Roll #'
        return len(self.jpdf)
    
    def sequence(self, freq=False):
        
        '''
        purpose: method to compute the number of distinct sequences of faces rolled
        param: freq = True/False to sort by frequency or not
        return: dataframe
        '''
        
        df = self.game.show_rolls(True) 
        rolls_lst = []
        
        # Get a list of list of row values
        for i in range(len(df)):   
            rolls_lst.append(list(df.iloc[i,:]))
        
        # Create frequency sorted dataframe    
        if freq == True:
            rolls_dict = {}
            count = 1
            for roll in rolls_lst:
                roll = ''.join([str(i) for i in roll])
                if roll in rolls_dict:
                    rolls_dict[roll][0].append(count)
                    rolls_dict[roll][1] += 1
                if roll not in rolls_dict:
                    rolls_dict[roll] = [[count], 1]
                count += 1

            freq_sdf = pd.DataFrame(rolls_dict).T
            freq_sdf.columns = ['Roll #s', 'Total Frequency']
            freq_sdf.index.name = 'Sequences'
            freq_sdf = freq_sdf.sort_values(by = ['Total Frequency'], ascending = False)
            self.freq_sdf = freq_sdf 
            return self.freq_sdf
        
        # Sequence sorted dataframe with multi-index
        if freq == False: 
            sdf = pd.DataFrame(df.value_counts())
            sdf.columns=['Frequency']
            sdf.index.name = 'Face Values'
            self.sdf = sdf
            return sdf
        
    def combo(self, freq = False):
        
        '''
        purpose: method to compute a dataframe of distinct combinations of faces rolled
        param: freq = True/False to sort by frequency or not
        return: dataframe
        ''' 
        
        df = self.game.show_rolls(True) 
        rolls_lst = []
        
        # Get a list of list of values
        for i in range(len(df)):   
            rolls_lst.append(list(df.iloc[i,:]))
        
        # Create frequency sorted dataframe
        if freq ==True:
            rolls_dict = {}
            count = 1
            for roll in rolls_lst:
                roll = ''.join([str(i) for i in sorted(roll)])
                if roll in rolls_dict:
                    rolls_dict[roll][0].append(count)
                    rolls_dict[roll][1] += 1
                if roll not in rolls_dict:
                    rolls_dict[roll] = [[count], 1]
                count += 1
        
            freq_cdf = pd.DataFrame(rolls_dict).T
            freq_cdf.columns = ['Roll #s', 'Total Frequency']
            freq_cdf.index.name = 'Combination'
            freq_cdf = freq_cdf.sort_values(by = ['Total Frequency'], ascending = False)
            self.freq_cdf = freq_cdf
            return self.freq_cdf
        
        # combo-sorted dataframe with multi-index
        if freq == False: 
            dct = {}
            for i in range(len(rolls_lst)):
                dct[i+1] = sorted(rolls_lst[i])
            dfsorted = pd.DataFrame(dct).T
            cdf = pd.DataFrame(dfsorted.value_counts())
            cdf.columns=['Frequency']
            cdf.index.name = 'Face Values'
            self.cdf = cdf
            return cdf
            
        
    def counts(self):
        
        '''
        purpose: method to compute how many times a given face is rolled in each event
        return: dataframe
        '''
        
        df = self.game.show_rolls(True) 
        rolls_lst = []
        counts_dct = {}
        unique_vals = []
        
        # Get a list of list of values
        for i in range(len(df)):   
            rolls_lst.append(list(df.iloc[i,:]))
    
        # Get a list of all unique values, sort it
        for x in rolls_lst:
            for i in x:
                if i not in unique_vals:
                    unique_vals.append(i)
        unique_vals.sort()
        
        #Iterate through each roll and count how many of each unique val, make a dict of roll counts
        y = 1
        for x in rolls_lst: 
            count = [0 for i in unique_vals]
            for i in x:
                count[unique_vals.index(i)] += 1
            counts_dct[y] = count
            y += 1
            
        # make dataframe
        countsdf = pd.DataFrame(counts_dct).T
        countsdf.columns = unique_vals
        self.countsdf = countsdf
        return self.countsdf