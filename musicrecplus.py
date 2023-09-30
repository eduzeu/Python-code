'''
Created on: November 2022
Authors: Daniel Fong, Eduardo Hernandez, Samuel Preston
I pledge my honor that I have abided by the Stevens Honor System.
'''

import os


def loadUsers(fileName):
    '''creates the txt file'''
    if os.path.exists('musicrecplus.txt'):
        PREF_FILE = open('musicrecplus.txt', 'r')
    else:
        open('musicrecplus.txt', 'x')
        PREF_FILE = open('musicrecplus.txt', 'r')
    with open(fileName, 'r') as file:
         userDict = {}
         for line in file:
             [userName, bands] = line.strip().split(':')
             bandList = bands.split(',') 
             bandList.sort()
             userDict[userName] = bandList
         file.close()
         return userDict


def getPreferences(userName, userMap):
    '''gives user input and loops until they enter empty string to store their
        preferences'''
    
    newPref = ''
    if userName in userMap:
        prefs = userMap[userName]
    #    print('Welcome back, ', userName)
    #    prefsUpdated = input('Please enter another artist or band that you like or press enter:  \n')
    else:
        prefs = []
        newPref = input('Please enter artist that you like (Press enter to finish):\n ')

    while newPref != '':
         prefs.append(newPref.strip().title())
         newPref = input('Please enter another artist you' \

                         ' like, or just press enter to see your' \
                         ' recommendations: ' )
         
    prefs.sort()
    return prefs

def getRecommendations(currUser, prefs, userMap):
     '''Gets the recommendations for the user'''
     bestUser = findBestUser(currUser, prefs, userMap)
     if bestUser == None:
        return ['No recommendations available at this time ']
     recommendations = drop(prefs, userMap[bestUser])
     x = 0
    
     while x < len(recommendations):
         if not recommendations[x]== None:
             print(recommendations[x]+'\n')
             x+=1
         else:
             x+=1
             pass
     return ''


def findBestUser(currUser, prefs, userMap):
    '''Finds the best matching user for the current user'''
    bestUser = None
    bestScore = 0
    for user in userMap.keys():
         if user[-1] != '$':
             score = numMatches(prefs, userMap[user])
             if score > bestScore and currUser != user:
                 bestScore = score
                 bestUser = user
    return bestUser

def drop(list1, list2):
    '''Merges two list, eliminating any duplicates'''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    while j < len(list2):
        list3.append(list2[j])
        j += 1
    return list3

def numMatches(list1, list2):
    '''returns the number of elements that match between the lists given.'''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches = matches + 1
            i = i + 1
            j = j + 1
        elif list1[i] < list2[j]:
            i = i + 1
        else:
            j = j + 1
    return matches

def saveUserPreferences(userName, prefs, userMap, fileName):
    '''saves the preferences that the user has by writing the in the txt file'''
    userMap[userName] = prefs
    file = open(fileName, 'w')
    for user in userMap:
        toSave = str(user) + ':' + ','.join(userMap[user]) + '\n'
        file.write(toSave)
    file.close()

def userWithMostLikes(userMap):
    '''returns the user with most likes by counting them in the dictionary'''
    try:
        bestUser = None
        bestScore = 0
        for user in userMap.keys():
             if user[-1] != '$':
                 score =  len(userMap[user])
                 if score > bestScore:
                     bestScore = score
                     bestUser = user
        return bestUser

    except:
        print('Sorry, no user found')
    return ''
    
def artistList(userMap):
    '''Returns a list of artists, filtered so every artist only appears once.'''
    finalartistlist = []
    initialartistlist = []
    for user in userMap:
        initialartistlist += userMap[user]
    for artist in initialartistlist:
        if artist not in finalartistlist:
            finalartistlist += [artist]
    return finalartistlist

def listToDict(lst):
    '''Converts the list of artist to a dictionary showing zero matches'''
    artistDict = {}
    for i in lst:
        artistDict[i] = 0
    return artistDict

def mostPopular(file):
    '''returns the most popular artist in the given group of users in the file.
Does this by taking the dictionary of artists and counting how many likes each
artist has and then determining which artist has the most amount of likes'''
    
    artDict = listToDict(artistList(loadUsers(file)))
    userMap = loadUsers(file)
    for user in userMap:
        for artist in userMap[user]:
            if user[-1] != '$':
                artDict[artist] += 1
    name = ''
    numberoflikes = 0
    if not artDict == {}:
        artDict = sorted(artDict.items(), key=lambda item: item[1], reverse = True)
        if len(artDict) >= 3:
            return artDict[0][0]+'\n'+artDict[1][0]+'\n'+artDict[2][0] +'\n'+artDict[3][0]
        if len(artDict) == 2:
            return artDict[0][0]+'\n'+artDict[1][0] +'\n'+artDict[2][0]
        if len(artDict) == 1:
            return 'Sorry, no artists found' 

    return ''

def howPopular(file):
    '''Returns the number of users who like the most popular artist.''' 
    artDict = listToDict(artistList(loadUsers(file)))
    userMap = loadUsers(file)
    for user in userMap:
        for artist in userMap[user]:
            artDict[artist] += 1
    x = 0
    for artist in list(artDict.keys()):
        
        if artDict[artist] > x:
            x = artDict[artist] 
    return x


def main():
     '''main function with all the initial prompts'''
          
     print('Welcome to group 6 music recommender system!')
     userMap = loadUsers('musicrecplus.txt')
     name = input('Please enter your name(put a $ symbol after your name if you wish your' \
                  ' preferences to remain private):\n').title()

     def main2():
         print('\nHello,', name)

         userListOptions =  ['e', 'r', 'p', 'h', 'm', 'q']
             
         while True:
             print('\nEnter a letter to choose an option:\n')
             userSelection = input('e - Enter preferences \nr - Get recommendations \np - Show most popular artists' \
                                   '\nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit \n')
                  

             if userSelection == userListOptions[0]:
                 prefs = getPreferences(name, userMap)
                 saveUserPreferences(name, prefs, userMap, 'musicrecplus.txt')
                       
             if userSelection == userListOptions[1]:
                 try:
                     print('Based on your favorite artists and previous similar selections, we think that you might like: \n') 
                     print(getRecommendations(name, userMap[name], userMap))
                 except:
                     print("We can't recommend if you have not entered any preference\nPlease enter your preferences first:")

             if userSelection == userListOptions[2]:
                 print(mostPopular('musicrecplus.txt'))

             if userSelection == userListOptions[3]:
                 print(howPopular('musicrecplus.txt'))

             if userSelection == userListOptions[4]:
                 print(userWithMostLikes(userMap))

             if userSelection == userListOptions[5]:
                 print('\nThank you for using the recommender. Bye!')
                 break 

             if userSelection not in userListOptions: 
                 print('Not valid input')

     if name not in userMap:
         prefs = getPreferences(name, userMap)
         saveUserPreferences(name, prefs, userMap, 'musicrecplus.txt')
         getPreferences(name, userMap)
         return main2()
     else:
         prefs = getPreferences(name, userMap)
         saveUserPreferences(name, prefs, userMap, 'musicrecplus.txt')
         main2()
             

          
if __name__ == '__main__': main() 
