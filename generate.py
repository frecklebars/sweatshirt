import sys
import json
import os.path
import random

def main():
    dictionaryFile, length = readArguments()
    dictionary = loadDictionary(dictionaryFile)
    
    lastWord = "~~~~~~~~~~~" #weird word that doesnt exist
    generatedText = ""
    
    for i in range(length):
        word = generateWord(lastWord, dictionary)
        generatedText = generatedText + " " + word
        lastWord = word
        
    print(generatedText)
    
def readArguments():
    #defaults
    dictionaryFile = "dictionary.json"
    length = 10
    
    arguments = len(sys.argv)-1 #getting the number of arguments passed in the command line
    
    #checking for dictionary
    if arguments >= 1:
        dictionaryFile = sys.argv[1]
    if arguments >= 2:
        length = int(sys.argv[2])
    
    return dictionaryFile, length

def loadDictionary(dfile):
    #checking if the dictionary exists
    if not os.path.exists(dfile):
        #raise error
        exit("no dictionary found")
        
    #read the existing dictionary
    file = open(dfile, "r")
    dictionary = json.load(file)
    file.close()
    
    return dictionary

def generateWord(lastWord, dictionary):
    if lastWord in dictionary:
        #pick random from its dictionary entries
        newDict = dictionary[lastWord]
        return random.choice(list(newDict.keys()))
    else:
        #pick a new word randomly
        word = getRandWord(dictionary)
        return word

def getRandWord(dictionary):
    randNum = random.randint(0, len(dictionary)-1)
    word = list(dictionary.keys())[randNum]
    
    return word

main()























