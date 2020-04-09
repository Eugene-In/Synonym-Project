class LoadingBar:
    def bar(rise, run, tenFlag, twentyfiveFlag, fiftyFlag, seventyfiveFlag, eigthyfiveFlag, nintyfiveFlag):
        if rise == 0:
            l = "p"
            return False
        else:
            jared = float(rise/run)
            if jared == 1:
                print('100% Complete')
            elif jared >= 0.95 and nintyfiveFlag == False:
                print("95% Complete")
                return True
            elif jared >= 0.85 and eigthyfiveFlag == False:
                print('85% Complete')
                return True
            elif jared >= 0.75 and seventyfiveFlag == False:
                print('75% Complete')
                return True
            elif jared >= 0.5 and fiftyFlag == False:
                print('50% Complete')
                return True
            elif jared >= 0.25 and twentyfiveFlag == False:
                print('25% Complete')
                return True
            elif jared >= 0.1 and tenFlag == False:
                print('10% Complete')
                return True
