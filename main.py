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

index_testing = 10
testing_data = test_data[:index_testing]
print len(testing_data)
#class with all data for bayesian learning
bayesian = BayesianStruct(train_data)

bayesian.processData()


bayesian.evalData(testing_data)

correctPredictionsBayesian = 0
for item in testing_data:
	print "GUESS: " + item.probBayesian
	print "TRUTH: " + item.y
	if item.probBayesian == item.y:
		correctPredictionsBayesian += 1
print "RESULTS BAYESIAN LEARNING:"
print "Total cases: " + str(len(testing_data))
print "Correct Predictions: " + str(correctPredictionsBayesian)
print "Correctness percentage: " + str((correctPredictionsBayesian / len(testing_data)) * 100) + "%"



knn = KNN(3, train_data)
knn.evalData(testing_data)

correctPredictionsKNN = 0
for item in testing_data:
	print "GUESS: " + item.probBayesian
	print "TRUTH: " + item.y
	if item.probKNN == item.y:
		correctPredictionsKNN += 1
print "RESULTS KNN - 3:"
print "Total cases: " + str(len(testing_data))
print "Correct Predictions: " + str(correctPredictionsKNN)
print "Correctness percentage: " + str((correctPredictionsKNN / len(testing_data)) * 100) + "%"
