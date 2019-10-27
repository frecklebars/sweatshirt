import sys
import json
import os.path

def main():
    dictionaryFile, inputFile = readArguments()
    dictionary = loadDictionary(dictionaryFile)
    
    if inputFile:
        print("NOTICE: reading from file is still work in progress\nunexpected or unwanted results may occur")
        #read data from file
        file = open(inputFile, "r")
        rawInput = file.read()
        dictionary = learn(dictionary, rawInput)
        dumpDictionary(dictionaryFile, dictionary)
    else:
        #read data from console input
        while True:
            rawInput = input(">> ")
            
            #if nothing was entered, stop
            if rawInput == "":
                break
            
            dictionary = learn(dictionary, rawInput)
            dumpDictionary(dictionaryFile, dictionary)
    
def readArguments():
    #defaults
    dictionaryFile = "dictionary.json"
    inputFile = ""
    
    arguments = len(sys.argv)-1 #getting the number of arguments passed in the command line
    
    #checking for dictionary
    if arguments >= 1:
        dictionaryFile = sys.argv[1]
    if arguments >= 2:
        inputFile = sys.argv[2]
    
    return dictionaryFile, inputFile

def loadDictionary(dfile):
    #checking if the dictionary exists
    if not os.path.exists(dfile):
        #if it doesnt we just make one
        file = open(dfile, "w")
        json.dump({}, file)
        file.close()
        
    #read the existing dictionary
    file = open(dfile, "r")
    dictionary = json.load(file)
    file.close()
    
    return dictionary

def learn(dictionary, rawInput):
    #splitting the read strings in words
    rawInput = rawInput.replace("\n\n", "\n")
    rawInput = rawInput.replace("\n", " ")
    words = rawInput.split(" ")
    for i in range(len(words)-1):
        currentWord = words[i]
        nextWord = words[i + 1]
        
        #checking if the current and next words are in the dictionary already
        if currentWord in dictionary:
            if nextWord in dictionary[currentWord]:
                dictionary[currentWord][nextWord] = dictionary[currentWord][nextWord] + 1
            else:
                dictionary[currentWord][nextWord] = 1
        else:
            dictionary[currentWord] = {nextWord: 1}
    
    return dictionary

def dumpDictionary(dfile, dictionary):
    file = open(dfile, "w")
    json.dump(dictionary, file)
    file.close()

main()