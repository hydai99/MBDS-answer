def color(L,color:dict):
    keys=sorted(color.keys(),key=lambda x:color[x],reverse=True)   #Sort first
    lst=[]                                           #Then put it in the array
    for i in keys:
        for j in range(color[i]):
            lst.append(i)
    mp=[0]*len(lst)
    j=0
    x=0
    y=0
    t=False
    
    #For each interval, place the same color in mp
    for i in lst:
        mp[j]=i
        if L%2==1:
            j=(j+2)%len(mp)
        else:
            x=j%L
            y=j//L
            if t==False:
                if x==L-2 and y%2==0:
                    j+=3
                elif x==L-1 and y%2==1:
                    j+=1
                else:
                    j=j+2
            else:
                if x==L-1 and y%2==0:
                    j+=1
                elif x==L-2 and y%2==1:
                    j+=3
                else:
                    j=j+2
            if j>=len(mp):
                j=1
                t=True
            j=j%len(mp)
            '''
            1010
            0101
            1010
            0101
            '''

    #Then place the elements in mp in the two-dimensional list
    res=[]
    for i in range(L):
        tmp=[]
        for j in range(L):
            tmp.append(mp[i*L+j])
        res.append(tmp)
    return res


file=open('output_question_5_1 (write the grid configuration (bead placement) for part 1)',mode='w')
res=color(5,{'R':12,'B':13})
for i in res:
    file.write(' '.join(i)+'\n')
file.close()


file=open('output_question_5_2 (write the grid configuration (bead placement) for part 2)',mode='w')
res=color(64,{'R':139,'B':1451,'G':977,'W':1072,'Y':457})
for i in res:
    file.write(' '.join(i)+'\n')
file.close()