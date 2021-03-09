# mathematical equation: 
#(x1,x2,x3...xk)=(N%L1,(N//L1)%L2,(N//(L1*L2))%L3....(N//(L1*L2*...Lk-1))%Lk)

def c1(n, L1, L2):
    return (n % L1, n // L1)
def c2(x1, x2, L1, L2):
    return x1 + x2 * L1
def c3(x: list, L: list):
    N = 0
    for i in range(len(x)):
        tmp = x[i]
        if i == 0:
            pass
        else:
            for j in L[:i]:
                tmp *= j
        N += tmp
    return N
def c4(N,L:list):
    #(x1,x2,x3...xk)=(N%L1,(N//L1)%L2,(N//(L1*L2))%L3....(N//(L1*L2*...Lk-1))%Lk)
    res=[]
    for i in range(len(L)):
        t=N
        for j in L[:i]:
            t//=j
        res.append(t%L[i])
    return res
def readData(filename):
    file=open(filename)
    data=file.readlines()[1:]
    res=[]
    for i in data:
        #Split data
        tmp=i.strip().split()
        #Convert to float
        res.append([int(i) for i in tmp])
    return res

file=open('output_index_7_2.txt',mode='w')
file.write('index\n')
data=readData('input_coordinates_7_2.txt')
for i in data:
    file.write(f'{c3(i,(4, 8, 5, 9, 6, 7))}\n')
file.close()
file=open('output_coordinates_7_2.txt',mode='w')
data=readData('input_index_7_2.txt')
file.write('   '.join([f'x{i}' for i in range(1,7)])+'\n')
for i in data:
    text='    '.join([str(j) for j in c4(*i,(4, 8, 5, 9, 6, 7))])
    file.write(f'{text}\n')