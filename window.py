from ignore import IgnoreList
from dataManager import DataManager

class LookingGlass:

    def wonderland(winlength, holder):
        q = []
        cnt = 0
        while len(q) < winlength:
            x = holder[cnt]
            y = x.lower()
            '''
            x2 = IgnoreList.ignoreList(x)
            if x2 == "":
                print("")
            else:
                q.append(x2)
                cnt += 1
                print(cnt)
             '''
            q.append(y)
            cnt += 1
            print(cnt)
        data = DataManager.manager(q)
        print(q)
        print(data)
        while cnt < len(holder):
            q.pop(0)
            x = holder[cnt]
            y = x.lower()
            '''
            x2 = IgnoreList.ignoreList(x)
            if x2 == "":
                print("")
            else:
                q.append(x2)
                cnt += 1
                print(cnt)
                print(q)
            '''
            q.append(y)
            cnt += 1
            data = DataManager.manager(q)
            print(cnt)
            print(q)
            print(data)
