#
try:
    with open("writeline().py")as s:
        print("initial pos of s=",s.tell())
        sk=s.read(5)
        print(sk)
        print("present pos of s=",s.tell())
        sk=s.read(10)
        print(sk)
        sk=s.read()
        print(sk)
        print("present pos of s=",s.tell())
        print("-"*50)
        s.seek(0)
        print("initial pos of s=",s.tell())
        sk=s.read(100)
        print(sk)
        print("present pos of s=",s.tell())
except FileNotFoundError:
    print("try again")
