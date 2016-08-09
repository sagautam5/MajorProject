from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.xml.networkreader import NetworkReader
from pybrain.structure import TanhLayer, SigmoidLayer
'''Result Normalizer'''
def Normalize(output):
    if output<0:
        return int(-1)
    elif output>=0:
        return int(1)

'''Final Result Along with Confusion Matrix'''
def Confusion(TP,FP,FN,TN):
    print '\n\t\t\tConfusion matrix\n'
    print '\t\t\t Target Values\n'
    print 'Prediction \t Positive(0) \t Neagative(1)\n'
    print 'Positive(0) \t   ',TP,'\t\t','  ',FP
    print 'Negative(1) \t   ',FN,'\t\t','  ',TN
    print '\n'
    
    Accuracy =(float) (TP+TN)/(TP+FP+FN+TN)*100
    Sensitivity = (float)(TP)/(TP+FP)*100
    Specificity = (float)(TN)/(TN+FN)*100
    print 'Accuracy : ' , Accuracy
    print 'Sensitivity : ' , Sensitivity
    print 'Specificity : ' , Specificity
    print '\n'



nets = buildNetwork(3,2,2,1,bias = True,hiddenclass=TanhLayer)
nets = NetworkReader.readFrom('filename.xml') 

demented_test_files = 25
nondemented_test_files = 28
X = []
y = []
yp = []
for i in range(0,demented_test_files):
    filename = '../Resource/TestData/Demented/Nearest/Image'+str(i)+'.txt'
    f = open(filename)
    Data = f.read().split()
    
    for p in range(len(Data)):
        data = float(Data[p])
	X.append(data)
    y.append(-1)
    m = nets.activate(X)
    print m
    P = Normalize(m)    
    yp.append(P)
    #print xt
    #print yt
    del X[:]  

for j in range(0,nondemented_test_files):
    filename = '../Resource/TestData/NotDemented/Nearest/Image'+str(j)+'.txt'
    f = open(filename)
    Data = f.read().split()
    
    for p in range(len(Data)):
        data = float(Data[p])
	X.append(data)
    y.append(1)
    m = nets.activate(X)
    print m
    P = Normalize(m)
    yp.append(P)
    #print xt
    #print yt
    del X[:]
    #print nets.activate([0,0])

TP = 0
FN = 0
FP = 0
TN = 0
print '\nTarget_Val :', y
print 'Prediction :', yp
for z in range(len(y)):
    if yp[z]==-1 and y[z]==-1:
        TP = TP+1
    if yp[z]==-1 and y[z]==1:
        FN = FN+1
    if yp[z]==1 and y[z]==-1:
        FP = FP+1
    if yp[z]==1 and y[z]==1:
        TN = TN+1
Confusion(TP,FP,FN,TN)
