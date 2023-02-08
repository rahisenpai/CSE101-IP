import random
n=int(input('enter number: '))
finalstr=''
for i in range(n):
    abcd='file'+str(i+1)+'.txt'
    with open(abcd,'r') as f:
        d1=f.read()

    s=',.:;'
    #words
    d2=''
    for i in d1:
        if i not in s:
            d2+=i
    l=d2.split()
    towo=len(l)

    d3=''
    for i in range(len(d1)):
        if d1[i]=='.' and (d1[i-1].isalpha() or d1[i-1]==' '):
            d3+=d1[i]
        elif d1[i]=='.' and d1[i-1] in s:
            pass
        else:
            d3+=d1[i]
    l2=d3.split('.')
    if l2[-1]=='' or l2[-1]==' ':
        l2.pop()

    f4_1=0
    for i in range(len(d1)):
        if d1[i] in s and d1[i-1] in s and (d1[i+1]==' ' or d1[i+1].isalpha()):
            f4_1+=1

    f3_1=0
    for i in l2:
        x=i.count(s)
        i.split()
        if (len(i)-x)>35 and (len(i)-x)<5:
            f3_1+=1

    #frequencies
    d={}
    for i in l:
        i.lower()
        x=d.get(i,0)
        x+=1
        d[i]=x
    f2_1=sum(sorted(list(d.values()), reverse=True)[:5])

    f1=len(d)/towo
    f2=f2_1/towo
    f3=f3_1/len(l2)
    f4=f4_1/towo
    f5=1 if towo>750 else 0
    score = 4 + f1*6+f2*6-f3-f4-f5
    qt=''
    for q in range(5):
        qt+=str(l[random.randint(0,len(l)-1)])+' '
    ert=sorted(list(d.values()), reverse=True)[:5]
    af,c='',0
    for i in d:
        if d.get(i) in ert:
            if c<=4:
                af+=str(i)+' '
                c+=1
            else:
                break

    finalstr += abcd+'\nscore:'+str(score)+'\n'+af+'\n'+qt+'\n\n'

with open('scores.txt','w') as f1:
    f1.write(finalstr)
print('output saved in scores.txt')