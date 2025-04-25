#studpick
import pickle
nos=int(input("Enter How Many Student Details U Have:"))
if(nos<=0):
    print("Invalid Input")
else:
    with open("STUDET.info","ab")as fp:
        for i in range(1,nos+1):
            try:
                print("----------------------")
                print("Enter {} Student Details:".format(i))
                print("-----------------------")
                sno=int(input("Enter Student number:"))
                sname=input("Enter Student Name:")
                marks=float(input("Enter Student Marks:"))
                lst=list()
                lst.append(sno)
                lst.append(sname)
                lst.append(marks)
                pickle.dump(lst,f)
                print("-----------------------")
                print("-----------------------")
                print("{} Studdent data saved Sucessfull in File:".format(i))
            except ValueError:
                print("Don't Enter Specal Symbols/ Alphabets For MArks And student no")
            except Exception:
                print("OOOPs....")
            
