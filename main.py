from __future__ import division
from parser_csv import *	
from random import shuffle
	
#primero obtengo los intervalos y atributos
intervals, attributes = createIntervalsAttributes()
#me creo el data
data = getData(intervals,attributes)
#hago un shuffle del corpus
shuffle(data)
#divido el corpus en 4/5 y 1/5
index = int( len(data) / 5 ) 
#1/5
test_data = data[:index]
#4/5
train_data = data[index:] 

#class with all data for bayesian learning
bayesian = BayesianStruct(train_data)

bayesian.processData()

bayesian.evalData(test_data)

correctPredictions = 0
for item in train_data:
	if item.prob == item.y:
		correctPredictions += 1
print "RESULTS BAYESIAN LEARNING:"
print "Total cases: " + str(len(train_data))
print "Correct Predictions: " + str(correctPredictions)
print "Correctness percentage: " + str((correctPredictions / len(train_data)) * 100) + "%"



knn = KNN(3, train_data)
knn.evalData(test_data)

correctPredictions = 0
for item in train_data:
	if item.prob == item.y:
		correctPredictions += 1
print "RESULTS KNN - 3:"
print "Total cases: " + str(len(train_data))
print "Correct Predictions: " + str(correctPredictions)
print "Correctness percentage: " + str((correctPredictions / len(train_data)) * 100) + "%"
