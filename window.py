from ignore import IgnoreList
from dataManager import DataManager
import dictionaryHandler as syn
class LookingGlass:

    def wonderland(winlength, holder, printFreq, printArray, printText):
        q = []
        cq = DataManager.completeTable(holder)
        cnt = 0
        displayCnt = 0

        while len(q) < winlength:
            x = holder[cnt]
            y = x.lower()
            q.append(y)
            cnt += 1


        data = DataManager.manager([] ,q)
        print("First print instance")
        print("q: " + str(q))
        print("data: " + str(data))


        while cnt < len(holder):
            x = holder[cnt]
            y = x.lower()
            if len(q) == winlength:
                q.pop(0)
            q.append(y)
            cnt += 1

            displayCnt += 1
            data = DataManager.manager([], q)


            if displayCnt == winlength:
                print("second instance of printing")
                print(cnt)
                for argh in q:
                    print(argh)
                    print(syn.synonyms(argh))
                if printArray != None:
                    print(q)
                if printText !=None:
                    dumpstr = " "
                    print(dumpstr.join(q))
                if printFreq != None:
                    print(data)
                print("\n")
                displayCnt = 0

