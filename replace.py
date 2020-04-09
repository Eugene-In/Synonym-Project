import re

# Takes a word and a string. Replaces all occurrences of word
# in string with elements from synonymList except the first.
# replace(...) returns a string containing all changes.
def replace(word, string, synonymList):
    if synonymList != None:
        new_list = string.split(" ")
        my_list = []
        cap_list = []
        cap = len(synonymList)-1
        seen = False
        lowercase = ""
        #Deals with empty spaces in the list
        for a in new_list:
            if a == "":
                b = a
            else:
                cap_list.append(a)
                lowercase = a.lower()
                my_list.append(lowercase)

        synonymListCounter = 0
        for i in range(0, len(my_list)):
            hold = my_list[i]
            symbols = re.findall(r"[\w']+|[.,!?;:]", hold)
            if seen and symbols[0] == word:
                updater = synonymList[synonymListCounter]
                if len(symbols) > 1:
                     updater+= symbols[1]
                my_list[i] = updater
                print("\nreplacing " + word + " with " + my_list[i]+'\n')
                synonymListCounter += 1
                # in the case that we reach the maximum amount of synonyms
                # loop to the begining by setting the counter back to 0
                if synonymListCounter > cap:
                    synonymListCounter = 0
            if not seen and symbols[0] == word:
                seen = True
        ctn = 0
        for i in my_list:
            j = i[0]
            k = cap_list[ctn][0]
            if j.isupper() != k.isupper():
                my_list[ctn] = my_list[ctn].capitalize()
            ctn += 1
        return " ".join(my_list)
    return string
'''
#Test I Used
string = "we got fast cars, and fast: boats and Fast girls and fast?"
synonymList=["speedy", "quick"]
print(string)
print(replace("fast", string, synonymList))
'''
