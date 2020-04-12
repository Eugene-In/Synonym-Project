from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import newParagraphBreaker

defaultIgnore = ["and","the","a","in","i","you","of","to", "with", "is", "be", "in", "as", "have", "that", "this"]
finalAddress = None

def main():
    def runGUI(*argss):
        global defaultIgnore
        global finalAddress
        try:
            if(finalAddress == None):
                value = str(fileToUse.get())
            else:
                value = finalAddress
            ignore = wordsToIgnore.get()
            if(ignore != ''):
                finalIgnore = defaultIgnore + ignore.split()
            else:
                finalIgnore = defaultIgnore
            newParagraphBreaker.ParagraphBreaker(value, ignoreList = finalIgnore, shortcutList = None, response=sentances.get())
        except ValueError:
            pass


    root = Tk()
    root.title("Synonym checker")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    fileToUse = StringVar()
    wordsToIgnore = StringVar()
    wordsToShortcut = StringVar()
    sentances = IntVar()

    def UploadAction(event=None):
        global finalAddress 
        finalAddress = str(filedialog.askopenfilename())


    def checkVariable(event=None):
        print("fileToUse:", fileToUse)
        print("finalAddress",finalAddress)

    file_entry = ttk.Entry(mainframe, width=15, textvariable=fileToUse)
    file_entry.grid(column=2, row=1, sticky=(W, E))

    ignore_entry = ttk.Entry(mainframe, width=15, textvariable=wordsToIgnore)
    ignore_entry.grid(column=2, row=2, sticky=(W, E))

    ignore_entry = ttk.Entry(mainframe, width=15, textvariable=wordsToShortcut)
    ignore_entry.grid(column=2, row=3, sticky=(W, E))

    ttk.Label(mainframe, text="File to fix").grid(column=1, row=1, sticky=W)
    ttk.Label(mainframe, text="Words to ignore").grid(column=1, row=2, sticky=W)
    ttk.Label(mainframe, text="Shortcuts to use").grid(column=1, row=3, sticky=W)
    ttk.Label(mainframe, text="Break into sentences").grid(column=1, row=4, sticky=W)
    
    ttk.Radiobutton(mainframe, text="Yes",variable=sentances,value=1).grid(column=2, row=4, sticky=E)
    ttk.Radiobutton(mainframe, text="No",variable=sentances,value=0).grid(column=2, row=4, sticky=W)




    ttk.Button(mainframe, text="Run", command=runGUI).grid(column=3, row=5, sticky=W)
    ttk.Button(mainframe, text='Open', command=UploadAction).grid(column=3, row=1, sticky=E)
    ttk.Button(mainframe, text='Check', command=checkVariable).grid(column=1, row=5, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
    file_entry.focus()
    root.bind('<Return>', None)

    root.mainloop()
main()