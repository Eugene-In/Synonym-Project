import re
import operator
from ignore import IgnoreList

class DataManager:

    def manager(il, q):
        
        data = {}
        print(type(data))

        for x in q:
            y = IgnoreList.ignoreWord(x, il)
            if y != None:
                if y in data:
                    data[y] = data[y]+1
                else:
                    data[y] = 1
        return dict( sorted(data.items(), key=operator.itemgetter(1),reverse=True))

    def completeTable(q):
        cq = []
        for x in q :
            y = x.lower()
            cq.append(y)
        return cq
