import re
from window import LookingGlass

class SlidingWindow:
    # wordlength = 6
    # minfreq = 1
    i = 0
    holder = []
    while i == 0:
        try:
            readfile = input("Please enter your file name: \n")
            winlength = int(input("How big do you want your window?\n"))
            #readfile = "testingFileDream.txt"
            #winlength = 50
            with open(readfile, "r", encoding="utf-8") as fp:
                line = fp.readline()
                while line:
                    qwe = line.replace('_'," ")
                    b = re.findall(r"\w+", qwe)
                    holder.extend(b)
                    line = fp.readline()
            i += 1
        except:
            print("This is no file with that name.\nPlease try again")

    print(holder)
    LookingGlass.wonderland(winlength, holder)
    """
    if len(sys.argv) < 4:
        if len(sys.argv) == 3:
            howmany = int(sys.argv[0])
            minlength = int(sys.argv[1])
            lastNWords = int(sys.argv[2])
            minfreq = 1
        elif len(sys.argv) == 2:
            howmany = int(sys.argv[0])
            minlength = int(sys.argv[1])
            lastNWords = 50
            minfreq = 1
        elif len(sys.argv) == 1:
            howmany = int(sys.argv[0])
            minlength = 3
            lastNWords = 50
            minfreq = 1
        elif len(sys.argv) == 0:
            howmany = 8
            minlength = 3
            lastNWords = 50
            minfreq = 1
    else:
        howmany = int(sys.argv[0])
        minlength = int(sys.argv[1])
        lastNWords = int(sys.argv[2])
        minfreq = int(sys.argv[3])

    """
