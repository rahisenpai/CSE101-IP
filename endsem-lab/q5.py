s=input('enter: ')
check=False
cl,cu,cd,cs=0,0,0,0
if len(s)>=8:
    for i in s:
        if i>='a' and i<='z':
            cl+=1
        if i>='A' and i<='Z':
            cu+=1
        if i>='0' and i<='9':
            cd+=1
        if i in '@#$%&':
            cs+=1
    if cs>0 and cl>0 and cd>0 and cu>0:
        check=True
print(check)