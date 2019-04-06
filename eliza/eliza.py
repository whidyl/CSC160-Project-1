from random import random, choice
from string import punctuation

evades = ["Please tell me more.", "Many of my patients tell me the same thing.", "Please continue."]
qualifiers = ["Why do you say that ", "You seem to think that ", "Can you explain why "]
history = []
replacements = {"my":"your", "i":"you", "mine":"yours", "me":"you", "we":"ya'll", "us":"ya'll", "our":"your guys's", "ours":"your guys's", "i'm":"you're", "you're":"I am", "you are": "I am" }
responseCounter = 0

def response(userInput):
    """ Returns a response given the following probabilities:
    25% chance to return a random evade
    25%  chance to use a random qualifier combined with a random past input (after 3 inputs from user)
    50% chance to use a random qualifier combined with the user's input"""
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
    wordList[0] = wordList[0].lower()
    for i, word in enumerate(wordList):
        if word.lower() in replacements:
            wordList[i] = replacements[word]
    # make sure the response is formated with a question mark as the last punctuation.
    if wordList[-1][-1] in punctuation:
        wordList[-1] = wordList[-1][:-1] + "?"
    else:
        wordList.append("?")
    modifiedString = ' '.join(wordList)
    history.append(modifiedString)
    return modifiedString
