import sys
import re
import dictionaryHandler as syn
from window import LookingGlass

class SlidingWindow:

    outputFreq = None
    outputArray = None
    outputText = None
    if '-a' in sys.argv:
        outputArray = True
    if '-f' in sys.argv:
        outputFreq = True
    if '-t' in sys.argv:
        outputText = True

    while True:
        try:
            #readfile = input("Please enter your file name: \n")
            holder = []
            readfile = "testingFileDream.txt"
            winlength = int(input("\nHow big do you want your window?\n"))
            #winlength = 15
            with open(readfile, "r", encoding="utf-8") as fp:
                line = fp.readline()
                while line:
                    qwe = line.replace('_'," ")
                    b = re.findall(r"\w+", qwe)
                    holder.extend(b)
                    line = fp.readline()
                fp.close()
            if winlength <= len(holder):
                break
            else:
                pez = winlength-len(holder)
                print("\nWindow is too big, by "+str(pez)+" number of words. \nPlease input a smaller window\n")
        except FileNotFoundError:
            print("\nThis is no file with that name.\nPlease try again\n")
        except ValueError:
            print("\nThis isn't a number, please input a number for the window.\n")
    LookingGlass.wonderland(winlength, holder, outputFreq, outputArray, outputText)
