import sys
import re
import dictionaryHandler as syn
from ignore import IgnoreList
from dataManager import DataManager
from window import LookingGlass
import replace as repl
from output import WriteNewFile
from tracker import LoadingBar

class ParagraphBreaker:

        def __init__(self, file, ignoreList=None, shortcutList=None):
            global filename
            fileName = file

            with open(fileName, encoding="utf-8") as f:
                data = f.readlines()
            f.close()

            fileCtn = 1
            io = WriteNewFile.fileCreator(fileCtn)

            while True:
                try:
                    response = input('\nBreak down to sentences?\n').lower()
                    if response == 'yes':
                        break
                    elif response == 'no':
                        break
                    else:
                        print("\nPlease input yes or no ONLY\n")
                except ValueError:
                    print("\nError, yes or no ONLY\n")
            #I tried to make this flag system it's own method
            #But it needs to be in here.
            #It's so it can print out a sort of loading bar
            a = False
            b = False
            c = False
            d = False
            e = False
            f = False
            remainingTime = len(data)
            tracker = 0
            flagCnt = 1
            for x in data:
                #print(x)
                #print("\n")
                #This is where it prints out the progress.
                flag = LoadingBar.bar(tracker, remainingTime, a, b, c, d, e, f)
                if flag == True:
                    if flagCnt == 1:
                        a = True
                        flagCnt += 1
                    elif flagCnt == 2:
                        b = True
                        flagCnt += 1
                    elif flagCnt == 3:
                        c = True
                        flagCnt += 1
                    elif flagCnt == 4:
                        d = True
                        flagCnt += 1
                    elif flagCnt == 5:
                        e = True
                        flagCnt += 1
                    elif flagCnt == 6:
                        f = True
                        flagCnt += 1
                loweredArray = x.lower()
                if response == 'yes':
                    sentences = loweredArray.split('.')
                    for y in sentences:
                        splitArray = re.findall(r"[\w']+", y)
                        freqTable = DataManager.manager(ignoreList, splitArray)
                        #print(freqTable)
                        #replaceEngine(freqTable) would replace this part of the code
                        wordsToReplace = []
                        for y in freqTable:
                            if freqTable.get(y) != 1:
                                wordsToReplace.append(y)
                        #print(wordsToReplace)
                        for y in wordsToReplace:
                            wordsToUse = syn.synonyms(y)
                            #print("\nSynonyms for '" + y + "' are: ",wordsToUse)
                            #print('\n')
                            x = repl.replace(y, x, wordsToUse)
                        #print("\nnew string: " + x+"\n")
                    tracker += 1
                    WriteNewFile.newFile(x, io)

                else:
                    splitArray = re.findall(r"[\w']+", loweredArray)
                    freqTable = DataManager.manager(ignoreList, splitArray)
                    #print(freqTable)
                    #replaceEngine(freqTable) would replace this part of the code
                    toReplace = self.replaceEngine(freqTable)
                    for j in toReplace:

                        wordsToUse = syn.synonyms(j)
                        #print ("\nsynonyms for " + j +" are ", wordsToUse)
                        #print("\n")
                        x = repl.replace(j, x, wordsToUse)
                    #print("\nnew string: " + x+"\n")
                    tracker += 1
                    WriteNewFile.newFile(x, io)
            LoadingBar.bar(tracker, remainingTime, a, b, c, d, e, f)
            io.close()

#unfinished shortcut manager. The basic structure is pretty basic
        def shortcutMaker(self, shortcutMap, replaceString):
            for x in replaceString:
                for y in shortcutMap:
                    x.replace(y, replaceString, shortcutMap[y])


        def replaceEngine(self, freqTable):
            wordsToReplace = []
            for y in freqTable:
                if freqTable.get(y) != 1:
                    wordsToReplace.append(y)
            #print(wordsToReplace)
            return wordsToReplace
