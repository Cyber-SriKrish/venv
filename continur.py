s="PYTHON"
for x in s:
    print(x)
print("="*50)
for x in s:
    if(x=="H"):
        break
    print(x)
else:
    print("for loop else with break")
print("----------------continue-------------------")
for x in s:
    if(x=="Y") or (x=="O"):
        continue
    print(x)
else:
    print("else loop with continue")
