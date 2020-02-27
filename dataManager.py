import re
from ignore import IgnoreList

class DataManager:

    def manager(dodge):
        bullet = {}
        hail = []
        hydra = IgnoreList.ignoreDict(hail)

        for x in dodge:
            y = IgnoreList.ignoreWord(x, hydra)
            if y in bullet:
                bullet[y] = bullet[y]+1
            else:
                bullet[y] = 1
        return bullet

    def completeTable(q):
        cq = []
        for x in q :
            y = x.lower()
            cq.append(y)
        return cq
