from ignore import IgnoreList
from dataManager import DataManager

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
        #Put function to do something with data and q here

        """
        print(q)
        print(data)
        print("\n")
        """

        while cnt < len(holder):
            x = holder[cnt]
            y = x.lower()
            q.pop(0)
            q.append(y)
            cnt += 1
            data = DataManager.manager(il, q)
            #Put function to do something with data and q here
            """
            print(cnt)
            print(q)
            print(data)
            print("\n")
            """
