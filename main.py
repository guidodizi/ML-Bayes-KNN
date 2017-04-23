from __future__ import division
from parser_csv import *	
from random import shuffle
import time
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
testing_data = test_data
print len(testing_data)
#class with all data for bayesian learning
bayesian = BayesianStruct(train_data)

bayesian.processData()

bayesian.evalData(testing_data)

correctPredictionsBayesian = 0
for item in testing_data:
	#print "GUESS: " + item.probBayesian
	#print "TRUTH: " + item.y
	if item.probBayesian == item.y:
		correctPredictionsBayesian += 1
print "RESULTS BAYESIAN LEARNING:"
print "Total cases: " + str(len(testing_data))
print "Correct Predictions: " + str(correctPredictionsBayesian)
print "Correctness percentage: " + str((correctPredictionsBayesian / len(testing_data)) * 100) + "%"

start2 = time.clock() 

knn = KNN(5, train_data)
knn.evalData(testing_data)

elapsed2 = time.clock()
elapsed2 = elapsed2 - start2

correctPredictionsKNN1 = 0
for item in testing_data:
	#print "GUESS: " + item.probKNN1
	#print "TRUTH: " + item.y
	if item.probKNN1 == item.y:
		correctPredictionsKNN1 += 1

print "RESULTS KNN - 1:"
print "Total cases: " + str(len(testing_data))
print "Correct Predictions: " + str(correctPredictionsKNN1)
print "Correctness percentage: " + str((correctPredictionsKNN1 / len(testing_data)) * 100) + "%"

correctPredictionsKNN3 = 0
for item in testing_data:
	#print "GUESS: " + item.probKNN3
	#print "TRUTH: " + item.y
	if item.probKNN3 == item.y:
		correctPredictionsKNN3 += 1

print "RESULTS KNN - 3:"
print "Total cases: " + str(len(testing_data))
print "Correct Predictions: " + str(correctPredictionsKNN3)
print "Correctness percentage: " + str((correctPredictionsKNN3 / len(testing_data)) * 100) + "%"

correctPredictionsKNN5 = 0
for item in testing_data:
	#print "GUESS: " + item.probKNN5
	#print "TRUTH: " + item.y
	if item.probKNN5 == item.y:
		correctPredictionsKNN5 += 1

print "RESULTS KNN - 5:"
print "Total cases: " + str(len(testing_data))
print "Correct Predictions: " + str(correctPredictionsKNN5)
print "Correctness percentage: " + str((correctPredictionsKNN5 / len(testing_data)) * 100) + "%"

print "Time spent in knn is: ", elapsed2
