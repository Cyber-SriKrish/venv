from collections import defaultdict
test_list = str(input("ENTER:"))
print("The original list is : " + str(test_list))
res = defaultdict(set)
for idx, ele in enumerate(test_list):
    for sub in ele.split():
        res[sub].add(idx + 1)
res = {key: list(val) for key, val in res.items()} 
print("The mapped dictionary : " + str(res))
