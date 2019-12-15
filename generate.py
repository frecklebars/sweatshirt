import sys
import json
import os.path
import random

def main():
    dictionaryFile = readArguments()
    dictionary = loadDictionary(dictionaryFile)
    
    lastWords = "~~~~~~~ ~~~~~" #weird word that doesnt exist
    
    verselines = random.randint(3, 6)
    for verseline in range(verselines):
        generatedText = ""
        
        length = random.randint(5, 10)
        
        for i in range(length):
            word, status = generateWord(lastWords, dictionary)
            #status is 1 if only one word needs replacing or 2 if both (ex. first time you need to replace both ~~~~~s)
            generatedText = generatedText + " " + word
            if status == 1:
                try:
                    lastWords = lastWords.split()[1] + " " + word
                except:
                    continue
            if status == 2:
                lastWords = word
            
        print(generatedText)
    
def readArguments():
    #defaults
    dictionaryFile = "dictionary.json"
    
    arguments = len(sys.argv)-1 #getting the number of arguments passed in the command line
    
    #checking for dictionary
    if arguments >= 1:
        dictionaryFile = sys.argv[1]
    
    return dictionaryFile

def loadDictionary(dfile):
    #checking if the dictionary exists
    if not os.path.exists(dfile):
        #raise error
        exit("no dictionary found")
        
    #read the existing dictionary
    file = open(dfile, "r", encoding="utf-8")
    dictionary = json.load(file)
    file.close()
    
    return dictionary

def generateWord(lastWords, dictionary):
    if lastWords in dictionary:
        #pick random from its dictionary entries
        newDict = dictionary[lastWords]
        return getNextWord(newDict), 1
    else:
        #pick a new word randomly
        word = getRandWord(dictionary)
        return word, 2

def getNextWord(dictionary):
    total = 0
    for word in dictionary:
        total = total + dictionary[word]
    
    randpick = random.randint(1, total)
    currentpick = 0
    
    #picking a random word by checking if the random nr we chose
    #is smaller than the current sum of the word's frequency
    
    #idk really how to explain this better honestly
    for word in dictionary:
        currentpick = currentpick + dictionary[word]
        if currentpick >= randpick:
            return word
        
def getRandWord(dictionary):
    return random.choice(list(dictionary.keys()))

main()























