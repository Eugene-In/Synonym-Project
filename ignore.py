import re

class IgnoreList:

  def ignoreDict(hail):
    with open(r"ignoreList.txt", "r", encoding="utf-8") as fp:
        contain = fp.readline()
        while contain:
            qwe = contain.replace('_'," ")
            b = re.findall(r"\w+", qwe)
            hail.extend(b)
            contain = fp.readline()
    fp.close()

    hydra = []
    for x in hail:
        y = x.lower()
        hydra.append(y)
    return hydra

  def ignoreWord(yes, hydra):
    if yes in hydra:
      provide = "Ignored word: program Synonym checker"
      return provide
    else:
      return yes
