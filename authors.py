name=str(input("Enter Author's Name:"))
if(name.casefold()=="russom"):
    print("Father Of Python")
else:
    if(name.casefold()=="gosling"):
        print("Father Of Java")
    if(name.casefold()=="ritche"):
        print("Father Of C")
    if(name.casefold()=="oliphant"):
        print("Father Of Numpy")
    else:
        print("He Is Nothing But Learner")
print("|"*80)
