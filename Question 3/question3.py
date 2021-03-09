from sklearn.neural_network import MLPRegressor
def readData(filename):                       #read data
    file=open(filename)
    data=file.readlines()[1:]
    res=[]
    for i in data:
        tmp=i.strip().split()                 #split data
        res.append([float(i) for i in tmp])   #convert to float
    return res
data=readData('train_data.txt')
test=readData('test_data.txt')

truth=[i[0] for i in readData('train_truth.txt')]
#dimension reduction
#create new classifier
reg=MLPRegressor(hidden_layer_sizes=(4,4))
#train
reg.fit(data,truth)

#print result
file=open('test_predicted.txt',mode='w')
file.write('y\n')
file.write(str(list(reg.predict(test))).replace(', ','\n')[1:-1])
file.close()