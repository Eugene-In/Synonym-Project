import sys
import re
import dictionaryHandler as syn
import newParagraphBreaker

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
        


    p1 = newParagraphBreaker.ParagraphBreaker("testingFileDream.txt")
