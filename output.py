class WriteNewFile:
    def fileCreator():
        fileCtn = 1
        while True:
            try:
                file = "editedFile"
                if fileCtn > 1:
                    file = file+str(fileCtn)
                f = open(file,"x")
                f.close()
                f = open(file, "a")
                break
            except FileExistsError:
                fileCtn += 1
        return f

    def newFile(line, io):
        if not line:
            b = 2
        else:
            io.write(line)
        return
