#Explain:
#Traverse the array from top to bottom and left to right.
#For each uncolored element with a value of 1 in the array, 
#use a Depth-First-Search to color all elements connected to it

def read(filename):
    #read data
    file=open(filename)
    res=[]
    data=file.readlines()
    for i in data:
        res.append([int(i) for i in i.strip().split()])
    return res
mat=read('input_question_4')
rel=[]                            #access matrix (If it is 1, it means it has been accessed)
for i in range(len(mat)):
    tmp=[]
    for j in range(len(mat[0])):
        tmp.append(0)
    rel.append(tmp)
color=1
def dfs(start):
    #Depth-First-Search
    rel[start[1]][start[0]]=color
    dirs=[[0,1],[1,0],[-1,0],[0,-1]]
    for dir in dirs:
        y=dir[1]+start[1]
        x=dir[0]+start[0]
        if y>=0 and x>=0 and y<len(rel) and x<len(rel[0]) and rel[y][x]==0 and mat[y][x]==1:
            dfs([x,y])
for j in range(len(mat[0])):
    for i in range(len(mat)):
        if rel[i][j]==0 and mat[i][j]==1:         #not accessed and equal to 1
            dfs([j,i])
            color+=1                              #color type + 1
file=open('output_question_4',mode='w')

for i in rel:
    file.write(' '.join([str(j) for j in i])+'\n')
file.close()