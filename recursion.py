 
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here        

def giveChange(amount,listCoins):
    '''takes an amount, and a list of coins. if the values of the list are greater than the amount, then the recursive function
    will remove them and continue to evaluate the rest of the list. For the values that are less than the amount, it will create
    the useit and loseit conditions, and finally, the function will return a list whose first item is the minimum number of coins
    and whose second item is a list of the coins in that optimal solution.'''
    if amount == 0: 
        return [0,[]]
    elif listCoins == []: 
        return [float('inf'),[]]
    elif listCoins[0] > amount:
        return  giveChange(amount,listCoins[1:])
    else:
        useit = giveChange(amount-listCoins[0],listCoins)
        storeUseit = [useit[0]+1, useit[1] + [listCoins[0]]]
        loseit = giveChange(amount,listCoins[1:])
        if loseit[0] < storeUseit[0]:
            return loseit
        else:
            return storeUseit
        
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    wordsWithScores = list(map(lambda word: [word, scoreHelper(scores, word)], dct))
    return wordsWithScores

def letterScore(letter, scorelist):
    '''returns the scrabble score of a single letter'''
    if letter == scorelist[0][0]: 
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])

def scoreHelper(scores, word):
    '''helper function for wordswithscore'''
    if word=='' or scores == []:
         return 0
    else:
        return letterScore(word[0], scores)+ scoreHelper(scores, word[1:])
         
    

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    ''' takes an element n and a list L and returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if n == 0 or L == []:
        return []
    else:
        return [L[0]] + take(n-1,L[1:]) 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''takes an element n and a list L and Returns the list L[n:], assuming L is a list and n is at least 0.'''
 # your code goes here
    if n == 0:
        return L
    elif  L == []:
        return []
    else:
        return drop(n-1, L[1:]) 
