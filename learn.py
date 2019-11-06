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
    
    rawInput = inputOptimize(rawInput)
    
    words = rawInput.split(" ")
    
    for i in range(len(words)-2):
        currentWord = words[i]
        secondWord = words[i + 1]
        nextWord = words[i + 2]
        
        #making the dict entry two words for better idk whats it called
        #natural-er sounder sentences?
        wordEntry = currentWord + " " + secondWord
        
        #checking if the current and next words are in the dictionary already
        if wordEntry in dictionary:
            if nextWord in dictionary[wordEntry]:
                dictionary[wordEntry][nextWord] = dictionary[wordEntry][nextWord] + 1
            else:
                dictionary[wordEntry][nextWord] = 1
        else:
            dictionary[wordEntry] = {nextWord: 1}
    
    return dictionary

def dumpDictionary(dfile, dictionary):
    file = open(dfile, "w")
    json.dump(dictionary, file)
    file.close()

def inputOptimize(raw):
    #makes the input text nicer so "father" and "father," aren't two different words
    #and crap like that
    raw = raw.lower()
    raw = raw.replace("\n\n", "\n")
    raw = raw.replace("\n", " ")
    raw = raw.replace("\"", "")
    raw = raw.replace("\\", "")
    raw = raw.replace(",", "")
    raw = raw.replace(".", "")
    raw = raw.replace("(", "")
    raw = raw.replace(")", "")
    
    return raw

main()








