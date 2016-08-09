from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer, SigmoidLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.xml.networkwriter import NetworkWriter

n1 = 75
n2 = 107
X = []
y = []

net = buildNetwork(3,2,2,2,bias = True,hiddenclass=TanhLayer)
DataSet = SupervisedDataSet(3, 2)
print net
for x in range(8):
    for i in range(0,n1):
        filename = '../Resource/TrainData/Demented/Nearest/Image'+str(i)+'.txt'
        f = open(filename)
        Data = f.read().split()
    
        for p in range(len(Data)):
            d = float(Data[p])
            X.append(d)
        y.append(0)
        y.append(1)
        xt = tuple(X)
        yt = tuple(y)
        #print xt
        #print yt
        DataSet.addSample(xt,yt)
        #print "Successfully read Demented Image",i
        del X[:]
        del y[:]

    for j in range(0,n2):
        filename = '../Resource/TrainData/NotDemented/Nearest/Image'+str(j)+'.txt'
        f = open(filename)
        Data = f.read().split()
    
        for p in range(len(Data)):
            d = float(Data[p])
            X.append(d)
        y.append(1)
        y.append(0)
        xt = tuple(X)
        yt = tuple(y)
        #print xt
        #print yt
        DataSet.addSample(xt,yt)
        #print "Successfully read NotDemented Image",j
        del X[:]
        del y[:]
#print DataSet
trainer = BackpropTrainer(net, DataSet, learningrate=0.001, momentum=0.99)
trainer.trainUntilConvergence(verbose=True,continueEpochs=10)

NetworkWriter.writeToFile(net, 'filename.xml')
