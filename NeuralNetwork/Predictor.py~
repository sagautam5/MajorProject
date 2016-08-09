from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.xml.networkreader import NetworkReader
from pybrain.structure import TanhLayer, SigmoidLayer
'''Result Normalizer'''
def Normalize(C):
    if C[0]>C[1]:
        return [1,0]
    else:
        return [0,1]

'''Final Result Along with Confusion Matrix'''
def Confusion(a,b,c,d):
    print '\n\t\t\tConfusion matrix\n'
    print '\t\t\t Target Values\n'
    print 'Prediction \t Positive(0) \t Neagative(1)\n'
    print 'Positive(0) \t   ',a,'\t\t','  ',b
    print 'Negative(1) \t   ',c,'\t\t','  ',d
    print '\n'
    
    Accuracy =(float) (a+d)/(a+b+c+d)*100
    Sensitivity = (float)(a)/(a+c)*100
    Specificity = (float)(d)/(b+d)*100
    print 'Accuracy : ' , Accuracy
    print 'Sensitivity : ' , Sensitivity
    print 'Specificity : ' , Specificity
    print '\n'



nets = buildNetwork(3,2,2,2,bias = True,hiddenclass=TanhLayer)
nets = NetworkReader.readFrom('filename.xml') 

n1 = 25
n2 = 28
X = []
y = []
yp = []
for i in range(0,n1):
    filename = '../Resource/TestData/Demented/Nearest/Image'+str(i)+'.txt'
    f = open(filename)
    Data = f.read().split()
    
    for p in range(len(Data)):
        d = float(Data[p])
	X.append(d)
    y.append(0)
    y.append(1)
    m = nets.activate(X)
    print m
    P = Normalize(m)    
    yp.append(P)
    #print xt
    #print yt
    del X[:]  

for j in range(0,n2):
    filename = '../Resource/TestData/NotDemented/Nearest/Image'+str(j)+'.txt'
    f = open(filename)
    Data = f.read().split()
    
    for p in range(len(Data)):
        d = float(Data[p])
	X.append(d)
    y.append(1)
    y.append(0)
    m = nets.activate(X)
    print m
    P = Normalize(m)
    yp.append(P)
    #print xt
    #print yt
    del X[:]
    #print nets.activate([0,0])

a = 0
b = 0
c = 0
d = 0
target = []
for i in range(25):
    target.append([0,1])
for j in range(28):
    target.append([1,0])
#print '\nTarget_Val :', target
#print 'Prediction :', yp
for z in range(53):
    if yp[z]==[0,1] and target[z]==[0,1]:
        a = a+1
    if yp[z]==[0,1] and target[z]==[1,0]:
        b = b+1
    if yp[z]==[1,0] and target[z]==[0,1]:
        c = c+1
    if yp[z]==[1,0] and target[z]==[1,0]:
        d = d+1
Confusion(a,b,c,d)
