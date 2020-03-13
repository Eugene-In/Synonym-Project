import sys
import re
import dictionaryHandler as syn
from ignore import IgnoreList
from dataManager import DataManager
from window import LookingGlass

class paragraphBreaker:
    with open("testingFileDream.txt",encoding="utf-8") as f:
        data = f.readlines()
    for x in data:
        print(x)
        splitArray = x.split()
        freqTable = DataManager.manager([], splitArray)
        print(freqTable)