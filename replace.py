#import sys
#import re
#import dictionaryHandler as syn
#from ignore import IgnoreList
#from dataManager import DataManager
#from window import LookingGlass
#Not quite sure what imports I shoud be using
def replace(word, string, synonymList):
# Takes a word and a string. Replaces all occurrences of word
# in string with elements from synonymList except the first.
# replace(...) returns a string containing all changes.
def replace(word, string, synonymList):
    my_list = string.split(" ")
    seen = False
    cap = len(synonymList)-1
    synonymListCounter = 0
    for i in range(0, len(my_list)):
        if seen and my_list[i] == word:
            my_list[i] = synonymList[synonymListCounter]
            synonymListCounter += 1
            # in the case that we reach the maximum amount of synonyms
            # loop to the begining by setting the counter back to 0
            if synonymListCounter > cap:
                synonymListCounter = 0
        if not seen and my_list[i] == word:
            seen = True
    return " ".join(my_list)
'''
Test I Used
string = "we got fast cars and fast boats and fast girls and fast dogs"
synonymList=["speedy", "quick"]
print(string)
print(replace("fast", string, synonymList))
'''
