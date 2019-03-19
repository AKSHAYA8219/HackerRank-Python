n=int(input())
A=list(map(int,input().split()))
m=max(A)
while m in A : 
    A.remove(m)
print(max(A))
