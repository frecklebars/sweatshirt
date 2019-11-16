import sys
import json
import os.path
import random

def main():
    dictionaryFile, length = readArguments()
    dictionary = loadDictionary(dictionaryFile)
    
    lastWords = "~~~~~~ ~~~~~" #weird word that doesnt exist
    generatedText = ""
    
    for i in range(length):
        word, status = generateWord(lastWords, dictionary)
        #status is 1 if only one word needs replacing or 2 if both (ex. first time you need to replace both ~~~~~s)
        generatedText = generatedText + " " + word
        if status == 1:
            lastWords = lastWords.split()[1] + " " + word
        if status == 2:
            lastWords = word
        
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
    file = open(dfile, "r", encoding="utf-8")
    dictionary = json.load(file)
    file.close()
    
    return dictionary

def generateWord(lastWords, dictionary):
    if lastWords in dictionary:
        #pick random from its dictionary entries
        newDict = dictionary[lastWords]
        return random.choice(list(newDict.keys())), 1 #TO DO - actually pick based on count not just randomly
    else:
        #pick a new word randomly
        print("[debug]: rand!"+lastWords)
        word = getRandWord(dictionary)
        return word, 2

def getRandWord(dictionary):
    word = random.choice(list(dictionary.keys()))
    
    return word

main()























