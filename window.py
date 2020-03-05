from ignore import IgnoreList
from dataManager import DataManager

class LookingGlass:

    def wonderland(winlength, holder):
        q = []
        cq = DataManager.completeTable(holder)
        cnt = 0

        while len(q) < winlength:
            x = holder[cnt]
            y = x.lower()
            q.append(y)
            cnt += 1

        data = DataManager.manager(q)
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
            data = DataManager.manager(q)
            """
            print(cnt)
            print(q)
            print(data)
            print("\n")
            """
