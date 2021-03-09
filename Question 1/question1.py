def find1(w,h,s):
    x=1
    y=1
    cur=-1
    res=''
    if s<cur+(h-y+1)*(y+h)//2+(w-x)*y or s>cur+(h-y+1)*(y+h)//2+(w-x)*h:#Out of range
        return 'NOT EXIST'
    while x!=w or y!=h:
        #intermediate value
        b=cur+(h-y+1)*(y+h)//2+(w-x)*(y+1)
        cur+=y
        if s<=b:      #If less than, move right
            res+='R'
            x+=1
        else:         #If greater than, move down
            res+='D'
            y+=1
    return res

file=open('output_question_1',mode='w')
q=[(9,9,65),(9,9,72),(9,9,90),(9,9,110),(90000,100000,87127231192),(90000,100000,5994891682)]
for i in q:
    file.write(f'{i[-1]} {find1(*i)}\n')
file.close()