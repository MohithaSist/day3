a=list(map(int,input().split()))
for i in range(0,len(a)):
    m=1
    for j in range(0,len(a)):
        if i!=j:
            m=m*a[j]
    print(m)
