def split(arr, n):
    arr.sort()
    count = 1
    for i in range(1, n):
        if(arr[i] - arr[i - 1] == 1):
            count = 2
            break
        
    print(count)
    
if __name__ == '__main__':
    arr=list(input("enter a array element with spaces:"))
    n=len(arr)
    split(arr, n)
