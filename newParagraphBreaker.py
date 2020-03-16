import sys
import re
import dictionaryHandler as syn
import string
from ignore import IgnoreList
from dataManager import DataManager
from window import LookingGlass

class paragraphBreaker:
    document = []
    window = int(input("Window Size:\n"))
    with open("testingFileDream.txt",encoding="utf-8") as fp:
        line = fp.readline()
        while line:
            qwe = line.replace('_'," ")
            b = re.findall(r"\w+", qwe)
            document.extend(b)
            line = fp.readline()
        fp.close()
    print(document)

    if len(document) < window:
        window = len(document)

    cnt = 0
    lcnt = 0
    data = []
    para = []
    for x in document:
        if cnt < window:
            para.append(x)
            cnt += 1
            lcnt += 1

        if lcnt == len(document):
            data.append(para)
            cnt = 0
        else:
            data.append(para)
            cnt = 0
            lcnt += 1

    for x in data:
        cnt += 1
        print("Run #"+str(cnt)+"\n")
        freqTable = DataManager.manager(["and","the","a","in","i","you"], x)
        #This is what the word frequency table looks like
        print("\n")
        print(freqTable)

        #Do we want to split this into a different class or function. That way one function breaks the paragraph which it then hands to the synonym checker


        wordsToReplace = []
        for y in freqTable:
            if freqTable.get(y) != 1:
                wordsToReplace.append(y)
        #Only words that appear more than once need to be considered
        print(wordsToReplace)
        for y in wordsToReplace:
            print("\n")
            print("Synonyms for '" + y + "' are: ",syn.synonyms(y))
