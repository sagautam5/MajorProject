import math

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
    count0 = len(X)-count1

    if count1>count0:
        label = 1
    else:
        label = 0
    return label

'''Final Result Along with Confusion Matrix'''
def Confusion(TP,FP,FN,TN):
    '''print '\n\t\t\tConfusion matrix\n'
    print '\t\t\t Target Values\n'
    print 'Prediction \t Positive(0) \t Neagative(1)\n'
    print 'Positive(0) \t   ',a,'\t\t','  ',b
    print 'Negative(1) \t   ',c,'\t\t','  ',d
    print '\n'
    '''
    Accuracy =(float) (TP+TN)/(TP+FP+FN+TN)*100
    Sensitivity = (float)(TP)/(TP+FP)*100
    Specificity = (float)(TN)/(TN+FN)*100
    print 'K = ',K,'Accuracy = ' , Accuracy,'%',' Sensitivity = ',Sensitivity,'%',' Specificity = ',Specificity,'%'
    ''' print 'Sensitivity : ' , Sensitivity
    print 'Specificity : ' , Specificity
    print '\n'''

''' Best Approximated Value of Nearest Neighbours'''

demented_train_files = 75
nondemented_train_files = 107

demented_test_files = 25
nondemented_test_files = 28

# List of Training Data of type [(_,_,_),_]
Train = []
# List of Test Data of type [(_,_,_),_]
Test = []
predicted = []
actual_val = []
for i in range(0,demented_train_files):
    filename = '../Resource/TrainData/Demented/Nearest/Image'+str(i)+'.txt'
    Data = [float(x) for x in open(filename).read().split()]
    data_sample = (tuple(Data),0)
    Train.append(data_sample)

for j in range(0,nondemented_train_files):
    filename = '../Resource/TrainData/NotDemented/Nearest/Image'+str(j)+'.txt'
    Data = [float(x) for x in open(filename).read().split()]
    data_sample = (tuple(Data),1)
    Train.append(data_sample)

for k in range(0,demented_test_files):
    filename = '../Resource/TestData/Demented/Nearest/Image'+str(k)+'.txt'
    Data = [float(x) for x in open(filename).read().split()]
    data_sample = (tuple(Data),0)
    Test.append(data_sample)
    actual_val.append(0)

for l in range(0,nondemented_test_files):
    filename = '../Resource/TestData/NotDemented/Nearest/Image'+str(l)+'.txt'
    Data = [float(x) for x in open(filename).read().split()]
    data_sample = (tuple(Data),1) 
    Test.append(data_sample)
    actual_val.append(1)

for K in range(1,182):
    dist_vector = [1.0e+15]*K
    labe_vector = [1]*K

    '''KNN alorithm to test the new instances'''

    for feature,label in Test:
        for Feature,Label in Train:
            dist = edistance(Feature,feature)
            for L in range(K):
                if dist<dist_vector[L]:
                    dist_vector[L] = dist
                    labe_vector[L] = Label
                    break
    
        newLabel = getLabel(labe_vector)
        predicted.append(newLabel)
    '''Classification Matrics Measurement'''
    TP = 0
    FN = 0
    FP = 0
    TN = 0

    #print '\nTarget_Value :',actual_val
    #print 'Prediction   :',predicted

    for z in range(len(predicted)):
        if predicted[z] == 0 and actual_val[z] == 0:
            TP = TP + 1
        if predicted[z] == 0 and actual_val[z] == 1:
            FN = FN + 1 
        if predicted[z] == 1 and actual_val[z] == 0:
            FP = FP + 1
        if predicted[z] == 1 and actual_val[z] == 1:
            TN = TN + 1

    Confusion(TP,FP,FN,TN)
    del predicted[:]
