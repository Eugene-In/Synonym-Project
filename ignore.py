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
    if (not(word in finalIL)):
        return word
    '''
    To be put in main.py if we want to use ignoreList: Matthew
    while True:
            try:
                response = int(input("\nDo you want to ignore any word?:\n (Yes/1, No/2)\n"))
                if response == 1:
                    fp = open(r"ignoreList.txt", "w", encoding="utf-8")
                    fp.write(input("\nPlease input words you don't want\nPut a space between each word.\n"))
                    fp.close()
                    break
                elif response == 2:
                    fp = open(r"ignoreList.txt", "w", encoding="utf-8")
                    fp.write("")
                    fp.close()
                    break
                else:
                    print("\nPlease input 1 or 2 for the ignore list.")
            except ValueError:
                print("\nPlease input 1 or 2 for the ignore list.")
    '''
