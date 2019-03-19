n=int(input())
arr=[]
for i in range(0,n):
    s=list(map(str,input().split()))
    if(s[0]=="insert"):
        pos=int(s[1])
        val=int(s[2])
        if(pos>=len(arr)):
            arr.append(val)
        else:
            arr.insert(pos,val)
    elif(s[0]=="print"):
        print(arr)
    elif(s[0]=="remove"):
        for j in range(0,len(arr)):
            if(arr[j]==int(s[1])):
                arr.remove(arr[j])
                break
    elif(s[0]=="append"):
        arr.append(int(s[1]))
    elif(s[0]=="sort"):
        arr.sort()
    elif(s[0]=="pop"):
        arr.pop()
    elif(s[0]=="reverse"):
        arr.reverse()
