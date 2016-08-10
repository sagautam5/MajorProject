import math
import jpype
from jpype import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.xml.networkreader import NetworkReader
from pybrain.structure import TanhLayer, SigmoidLayer

'''Result Normalizer'''
def Normalize(output):
    if output[0]>output[1]:
        return [1,0]
    else:
        return [0,1]

'''Measurement of Euclidean Distance between Feature Vectors '''
def edistance(feature1,feature2):
    dist = 0
    for i in range(len(feature1)):
        dist = dist+(feature1[i]-feature2[i])*(feature1[i]-feature2[i])
    dist = math.sqrt(dist)
    return dist

'''Assigning Majority Class Label to the label of New Instance'''
def getLabel(Labels):
    count1 = 0
    for x in range(len(Labels)):
        if Labels[x]==1:
            count1 = count1+1
    count0 = len(Labels)-count1

    if count1>count0:
        label = 1
    else:
        label = 0
    return label

""" Acessing java class Dementia from package Feature Extraction 
to calculate Feature Vector"""
Action = raw_input("Training Feature Extraction Yes or No  ??")
startJVM(jpype.getDefaultJVMPath());
myPackage = JPackage('FeatureExtraction').org.classes #Location of Dementia.class
Dementia = myPackage.Dementia                         # Dementia.class file acess

if Action == "Yes":
    Dementia.System("Train")                          #static function System(...) call
Source = raw_input("Enter Test Image File Location:")
String = Dementia.System("Test",Source)               #static function System(....,....) call
Features = [float(x) for x in String.split()]         # we get feature vector as string so to get numeric 
                                                      # spliting is required.

''' Best Approximated Value of Nearest Neighbours'''
K = 7

demented_file_no = 75
nondemented_file_no = 107

# List of Training Data of type [(_,_,_),_]
Train = []
# List of Test Data of type [(_,_,_),_]

predicted = []
actual_val = []
for i in range(0,demented_file_no):
    filename = 'Resource/TrainData/Demented/Nearest/Image'+str(i)+'.txt'
    Data = [float(x) for x in open(filename).read().split()]
    data_sample = (tuple(Data),0)
    Train.append(data_sample)

for j in range(0,nondemented_file_no):
    filename = 'Resource/TrainData/NotDemented/Nearest/Image'+str(j)+'.txt'
    Data = [float(x) for x in open(filename).read().split()]
    data_sample = (tuple(Data),1)
    Train.append(data_sample)

test_Feature = tuple(Features)
dist_vector = [1.0e+15]*K
labe_vector = [1]*K

'''KNN alorithm to test the new instances'''


for Feature,Label in Train:
    dist = edistance(Feature,test_Feature)
    for L in range(K):
        if dist<dist_vector[L]:
            dist_vector[L] = dist
            labe_vector[L] = Label
            break
#Assignment of majority label to label of test feature vector
newLabel = getLabel(labe_vector) 
if  newLabel==0:
    print "KNN Model: Dementia Positive"
if  newLabel==1:
    print "KNN Model: Dementia Negative"

#Network Initialization...
nets = buildNetwork(3,2,2,2,bias = True,hiddenclass=TanhLayer)

#Assigning Weights to the Neural Network from xml file
nets = NetworkReader.readFrom('filename.xml') 

#get output of the Neural Netwok
network_Result = nets.activate(Features) 
#get final result from output
prediction = Normalize(network_Result)

if(prediction==[0,1]):
    print "Neural Network: Dementia Positive"
if(prediction==[1,0]):
    print "Neural Network: Dementia Negative"

