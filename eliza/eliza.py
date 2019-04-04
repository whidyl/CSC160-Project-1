from random import random, choice

evades = ["Please tell me more.", "Many of my patients tell me the same thing.", "Please continue."]
qualifiers = ["Why do you say that ", "You seem to think that ", "Can you explain why "]
history = []
replacements = {"my":"your", "i":"you", "mine":"yours", "me":"you", "we":"ya'll", "us":"ya'll", "our":"your guys's", "ours":"your guys's", "i'm":"you're" }
responseCounter = 0

def response(userInput):
    """ Respods with: 25% chance to evade, 25%  chance to use past message history, 50% chance to use qualifiers"""
    global responseCounter
    responseCounter += 1
    rand = random()*100
    if rand > 75:
        return choice(evades)
    if (responseCounter > 3) and (rand > 50):
        return "Earlier you said that " + choice(history).lower()
    return choice(qualifiers) + modifyString(userInput).lower() 
    
    

def modifyString(string):
    """ Replaces first-person words in @param string with applicable second-person words. """
    wordList = string.split(" ")
    for i, word in enumerate(wordList):
        if word.lower() in replacements:
            wordList[i] = replacements[word.lower()]
    modifiedString = ' '.join(wordList)
    history.append(modifiedString)
    return modifiedString
