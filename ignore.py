import re

class IgnoreList:

  def ignoreDict(il):
    with open(r"ignoreList.txt", "r", encoding="utf-8") as fp:
        contain = fp.readline()
        while contain:
            qwe = contain.replace('_'," ")
            b = re.findall(r"\w+", qwe)
            il.extend(b)
            contain = fp.readline()
    fp.close()

    finalIL = []
    for x in il:
        y = x.lower()
        finalIL.append(y)
    return finalIL

  def ignoreWord(word, finalIL):
    if word in finalIL:
      provide = "Ignored word: program Synonym checker"
      return provide
    else:
      return word
