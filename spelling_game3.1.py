"""
Created on Fri Mar  2 15:39:47 2018
version 1.0

@author: jsilvey
"""
import random

spelling = {1:['acceptable','acceptible'], \
2:['accidentally','accidentaly'], \
3:['accommodate','accomodate'], \
4:['acquire','aquire'], \
5:['acquit','aquit'], \
6:['a lot','alot'], \
7:['amateur','amature']}

gamePoints = 0
gameState = True

def playRound():       
    def randomSequence(length):
        """
        Takes an int as argument for length of a range of values. 
        Returns a tuple of four randomly assigned and unique ints 
        from within the range.
        """
        def randomNum(length):
            a = random.uniform(1, length+1)
            return int(a)
        
        a = randomNum(length)
        b = randomNum(length)
        while a == b:
            b = randomNum(length)
        c = randomNum(length)
        while a == c or b == c:
            c = randomNum(length)
        d = randomNum(length)
        while a == d or b == d or c == d:
            d = randomNum(length)
        return (a, b, c, d)
    
    def initializeRound():    
        """
        Takes the master dict as an argument. Returns a dict of four randomly
        chosen words with a key signifying whether or not the word is spelled correctly.
        """
        thisRound = randomSequence(len(spelling))
        #thisRound takes the master dict as argument and returns a tuple of four randomly
        #selected non-repeating digits. These digits will be indexed into the
        #master dict to pull out four words.
        def randomWrongChoice():
            a = random.uniform(0, 2)
            return int(a)
  
        currentWords = {}
        #currentWords is the dict mapping four randomly chosen words to 0 if 
        #spelled correctly or to 1 if spelled incorrectly
        goodList = []
        badList = []
        for i in thisRound:
            a = randomWrongChoice()
            if a == 1 and a in currentWords:
                badList += [spelling[i][a]]
                currentWords[1] = badList
            elif a == 0 and a in currentWords:
                goodList += [spelling[i][a]]
                currentWords[0] = goodList
            else:
                currentWords[a] = spelling[i][a]
                if a == 0:
                    goodList += [currentWords[a]]
                elif a == 1:
                    badList += [currentWords[a]]
        mappingList = goodList + badList
        mappingKey = randomSequence(4)
        
        mappingDict = {}
        #a dict of four shuffled randomly-selected words, with some possible 
        #spelling errors
        for i in mappingKey:
            mappingDict[i] = mappingList[0]
            mappingList = mappingList[1:]
    
        print ('\n')
        print (mappingDict)
        print ('Please type the numbers of the words spelled incorrectly separated by a commas. \n')
        print ('If no words are spelled incorrectly, please enter "0": ')
        ans = input('----->')
        
        ans = ans.split(',')
        for digit in range(len(ans)):
            ans[digit] = int(ans[digit])
            
        pts = 0
        wordsRight = 0
        wordsMissed = len(badList)
        
        if ans[0] == 0:
            x = 1
            while x < 5:
                if mappingDict[x] in goodList:
                    pts += 5
                    x += 1
                else:
                    pts = 0
                    print ('Oops! Looks like you missed an error.')
                    x = 5
        else:
            y = (len(ans) - 1)
            while y > -1:
                if mappingDict[ans[y]] in badList:
                    print ('Points for correct guess: +5')
                    pts += 5
                    wordsRight += 1
                    y -= 1
                else:
                    print ('Incorrect guess.')
                    pts = 0
                    y = -1
            print ("Number of words missed: ", (wordsMissed - wordsRight))
                
                
        print ("Total points this round: ", pts)
        return pts
    
    return initializeRound()
    
def again():
    prompting = True
    while prompting:
        decision = input('Would you like to play again? Type "Y" or "N": ').upper()
        if decision == "Y":
            return True
        elif decision == "N":
            return False
        else:
            print ('Please enter a valid answer.')
            
    
while gameState:
    gamePoints += playRound()
    print ('Total points this game: ', gamePoints)
    game = again()
    if not game:
        gameState = False
        
