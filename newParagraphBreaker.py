import sys
import re
import dictionaryHandler as syn
import string
import re
from ignore import IgnoreList
from dataManager import DataManager
from window import LookingGlass

class paragraphBreaker:
    with open("testingFileDream.txt",encoding="utf-8") as f:
        data = f.readlines()
    for x in data:
        #This is the string with no editing done
        print(x)
        loweredArray = x.lower()
        splitArray = re.findall(r"[\w']+", loweredArray)
        
        freqTable = DataManager.manager(["and","the","a","in","i","you"], splitArray)
        #This is what the word frequency table looks like
        print(freqTable)
        
        #Do we want to split this into a different class or function. That way one function breaks the paragraph which it then hands to the synonym checker
        
        
        wordsToReplace = []
        for y in freqTable:
            if freqTable.get(y) != 1:
                wordsToReplace.append(y)
        #Only words that appear more than once need to be considered
        print(wordsToReplace)
        for y in wordsToReplace:
            print("Synonyms for '" + y + "' are: ",syn.synonyms(y))