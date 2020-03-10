from ignore import IgnoreList
from dataManager import DataManager
from overUsedWord import FindingWord

class LookingGlass:

    def wonderland(winlength, holder):
        q = []
        cq = DataManager.completeTable(holder)
        cnt = 0
        hail = []
        il = IgnoreList.ignoreDict(hail)

        while len(q) < winlength:
            x = holder[cnt]
            y = x.lower()
            q.append(y)
            cnt += 1

        data = DataManager.manager(il, q)
        FindingWord.comparing(q, data, cnt, cq)

        '''
        print(q)
        print(data)
        print("\n")
        '''

        while cnt < len(holder):
            x = holder[cnt]
            y = x.lower()
            if len(q) == winlength:
                q.pop(0)
            q.append(y)
            cnt += 1
            data = DataManager.manager(il, q)
            if len(q) == winlength:
                FindingWord.comparing(q, data, cnt, cq)
            '''
            print(cnt)
            print(q)
            print(data)
            print("\n")
            '''
        print("\nDone")
        FindingWord.editedDraft(cq)
