import re
from window import LookingGlass

class SlidingWindow:
    # wordlength = 6
    # minfreq = 1
    while True:
        try:
            while True:
                readfile = input("Please enter your file name: \n")
                #readfile = "testingFileDream.txt"
                winlength = int(input("\nHow big do you want your window?\n"))
                #winlength = 15
                holder = []

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
            break
        except FileNotFoundError:
            print("\nThis is no file with that name.\nPlease try again\n")
        except ValueError:
            print("\nThis isn't a number, please input a number for the window.\n")

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
    LookingGlass.wonderland(winlength, holder)
