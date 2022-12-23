def pattern(n):
    for i in range(1,n+1):
        #print("*"*i + (n-i)*2*" " + "*"*i)
        for j in range(i):
            print("*",end="")
        print(" "*2*(n-i),end="")
        for k in range(i):
           print("*",end="")
        print()

n = int(input('enter: '))
pattern(n)