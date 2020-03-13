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
        print(x)
        loweredArray = x.lower()
        splitArray = re.findall(r"[\w']+", loweredArray)
        
        freqTable = DataManager.manager(["and","the","a"], splitArray)
        print(freqTable)
        