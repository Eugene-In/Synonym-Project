import nltk 
from nltk.corpus import wordnet

import requests
from bs4 import BeautifulSoup

#######I may not need these imports##########



###All handlers need to go into the same file me thinks. That way they can cross reference


shortcutDict = {}





def setShortcuts(pairToSplit):
    values = pairToSplit.split(":")
    keyToAdd = values[0]
    valueToAdd = values[1]
    shortcutDict[keyToAdd] = valueToAdd
    
    

def checkWord(wordToCheck):
    if wordToCheck in shortcutDict:
        return shortcutDict[wordToCheck]
    else:
        return None
        

"""        
def replaceWord(wordToCheck):
    if checkWord(wordToCheck) != None
        
"""

