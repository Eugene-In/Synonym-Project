import re
from ignore import IgnoreList

class DataManager:

    def manager(il, q):
        data = {}

        for x in q:
            y = IgnoreList.ignoreWord(x, il)
            if y in data:
                data[y] = data[y]+1
            else:
                data[y] = 1
        return data

    def completeTable(q):
        cq = []
        for x in q :
            y = x.lower()
            cq.append(y)
        return cq
