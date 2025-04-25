#ex
def stmarks(rno,sname,cls,**marks):
    totm=0
    print("|"*50)
    print("\tROLLNUMBER \tNAME \tCLASS")
    print("\t{},      \t{},\t{}".format(rno,sname,cls))
    print("|"*50)
    for sn,sm in marks.items():
        print("{}----->{}".format(sn,sm))
        totm=totm+sm
    else:
        print("|"*50)
        print("TOTAL MARKS:{}".format(totm))

#
stmarks(10,"SK","X",maths=77,science=88,social=66,hindi=88,english=70,telugu=99)
stmarks(10,"SK","XII",maths=99,Physics=70,chemistry=60)
stmarks(10,"SK","B.TECH",cpp=59,python=70,AI=68)
