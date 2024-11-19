def a(n):
    b=1
    for i in range(1,n+1):
        for j in range(i):
            print(b,end=' ')
            b+=1
        print()
c=int(input().strip())
a(c)
