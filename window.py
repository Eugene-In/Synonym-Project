'''
Our first version with a sliding wondow before switching over to reading the files by lines.

from ignore import IgnoreList
from dataManager import DataManager
import dictionaryHandler as syn
class LookingGlass:

    def wonderland(winlength, holder, printFreq, printArray, printText):
        q = []
        cq = DataManager.completeTable(holder)
        cnt = 0
        #For ignoreList
        #hail = []
        #il = IgnoreList.ignoreDict(hail)
        displayCnt = -1

        while len(q) < winlength:
            x = holder[cnt]
            y = x.lower()
            q.append(y)
            displayCnt += 1
            cnt += 1

        #Empty array in manager is for ignoreList
        data = DataManager.manager([] ,q)
        print("First print instance")
        print("q: " + str(q))
        print("data: " + str(data))


        while cnt < len(holder):
            x = holder[cnt]
            y = x.lower()
            q.pop(0)
            q.append(y)
            cnt += 1
            displayCnt += 1

            if cnt == len(cq):
                displayCnt = winlength

            if displayCnt == winlength:
                #Empty array in manager is for ignoreList
                data = DataManager.manager([], q)
                print("\nsecond instance of printing")
                print(str(cnt)+"\n")
                for argh in q:
                    #print(argh)
                    #print(syn.synonyms(argh))
                    syn.synonyms(argh)
                if printArray != None:
                    print(q)
                    print('\n')
                if printText !=None:
                    dumpstr = " "
                    print(dumpstr.join(q))
                    print('\n')
                if printFreq != None:
                    print(data)
                print("\n")
                displayCnt = 0

        print("done")
'''
