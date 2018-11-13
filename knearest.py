#ML Asg 3
import csv
import math
import operator
import sys

#handling input
userInput = sys.argv[1:]
kVal = int(userInput[1])
lVal = userInput[3]

'''
Load CSV files into 2d lists where each
row is an instance
'''
def loadDataset():
 	trainSet = []
 	train = open('knn_train.csv')
 	trainLines = csv.reader(train)
 	trainData = list(trainLines)

 	testSet = []
 	test = open('knn_test.csv')
 	testLines = csv.reader(test)
 	testData = list(testLines)

 	for i in range(len(trainData)):
 		trainSet.append(trainData[i])

 	for i in range(len(testData)):
 		testSet.append(testData[i])

 	return testSet, trainSet


'''
Distance Functions
'''
#------------------------------------------------------
def eucledianDistance(d1,d2,length):
	distance = 0
	for x in range(length):
		d1Val = float(d1[x])
		d2Val = float(d2[x])
		distance += pow((d1Val - d2Val), 2)
	return math.sqrt(distance)

def L1Distance(d1,d2,length):
	distance = 0
	for x in range(1,length):
		d1Val = float(d1[x])
		d2Val = float(d2[x])
		distance += math.fabs(d1Val-d2Val)
	return distance

def maxNormDistance(d1,d2,length):
	distance = 0
	maxVal = 0
	for x in range(length):
		d1Val = float(d1[x])
		d2Val = float(d2[x])
		defVal = math.fabs(d1Val-d2Val)
		if(defVal > maxVal):
			maxVal = defVal
	return maxVal
#------------------------------------------------------


'''
Helper function to pull label from an instance
'''
def labelReceiver(d1,length):
    labelVal = float(d1[length])
    return labelVal


'''
the KNN algorithm,
We pull all distances when comparing our training set
to an instance of our testset.
We then sort and pull iterate for k instances
and put the distance as well as the label into a list and return that
'''
def getNeighbors(tSet, tInstance, k):
	distances = [] #need this to get k distances
	labels = []    #stores the label for a specific neighbor
	length = len(tInstance)-1
	for i in range(1,len(tSet)):
		if(lVal == "L1"):
			d = L1Distance(tSet[i],tInstance,length)
		elif(lVal == "L2"):
			d = eucledianDistance(tSet[i],tInstance,length)
		elif(lVal == "Linf"):
			d = maxNormDistance(tSet[i],tInstance,length)
		else:
			print("Use either L1, L2, or Linf as input")
			return 0

		distances.append(d)
		labelVal = labelReceiver(tSet[i],length)
		labels.append(labelVal)

	neighborList = list(zip(distances,labels))
	neighborList.sort()
	neighbors = []
	for val in range(k):
		neighbors.append(neighborList[val])
	return neighbors

'''
Function to make our prediction
'''
def makePrediction(tSet, tInstance, k):
	preList = getNeighbors(tSet, tInstance, k)
	prediction = 0
	for i,j in preList:
		prediction = prediction + int(j)

	if(prediction >= 1):
		label = 1
	elif(prediction < 1):
		label = -1


	print(label)

#load our data
testData , trainData = loadDataset()

#Run our function for every instance of our test data
for i in range(1,len(testData)):
	print("Test Instance",i)
	makePrediction(trainData, testData[i], kVal)
