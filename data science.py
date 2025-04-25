lang="PYTHON"    #global varialble
def learnDatasci(sname):#formal parameters
    crs1="DATA SCIENCE"  #local variable
    print("{} want TO LEARN {} , but that need {} programming lang".format(sname,crs1,lang))
def learnML(sname):
    crs2="MACHINE LEARNING"
    print("{} want TO LEARN {} , but that need {} programming lang".format(sname,crs2,lang))
def learnDL(sname):
    crs3="DEEP LEARNING"
    print("{} want TO LEARN {} , but that need {} programming lang".format(sname,crs3,lang))
    "print(crs2,sname1)" # invalid here, formal para's and local par's had no scope in another function
#call(s)
learnDatasci("RISE")
learnML("ROAR")           #argument values
learnDL("REVOLT")
