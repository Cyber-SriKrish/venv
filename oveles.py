print("enter text:")
t=(str(x) for x in input())
for v in t:
    if(v=="a")or(v=="e")or(v=="i")or(v=="o")or(v=="u"):
        continue
    else:
        print("\n--------consonant's in Text-----------")
        print(v)
