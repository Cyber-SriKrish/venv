#
try:
    with open("write().py")as s:
        sk=s.read()
        print(sk)
except FileNotFoundError:
    print("try again")
