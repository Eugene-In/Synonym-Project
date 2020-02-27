class IgnoreList: 

  def ignoreList(yes):
    il = open(r"ignoreList.txt","r")
    contain = il.readline()
    hail = contain.split()
    hydra = []
    for x in hail:
        x.lower()
        hydra.append(x)
        
    if yes in hydra:
      provide = ""
      return provide
    else:
      return yes