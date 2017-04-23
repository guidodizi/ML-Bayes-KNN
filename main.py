from __future__ import division
from parser_csv import *	
from random import shuffle
import time
#primero obtengo los intervalos y atributos
intervals, attributes, common_values = createIntervalsAttributes()
#eligo de que forma utilizar los unknown
not_ok = True
mode = input("Ingrese 0 para usar los 'unknown' como un posible valor mas del atributo\nIngrese 1 para preprocesar los 'unknown': ") 
while not_ok:
	if mode == 0:
		fix_unknown = False
		not_ok = False
	elif mode == 1:
		fix_unknown = True
		not_ok = False
	else:
		print "\nValor invalido\n"
		mode = input("Ingrese 0 para usar los 'unknown' como un posible valor mas del atributo\nIngrese 1 para preprocesar los 'unknown': ") 

#me creo el data
data = getData(intervals,attributes, common_values, fix_unknown)
#hago un shuffle del corpus
shuffle(data)
#divido el corpus en 4/5 y 1/5
index = int( len(data) / 5 ) 
#1/5
test_data = data[:index]
#4/5
train_data = data[index:] 


#PARTE B
#validacion cruzada, divido mi train data en 10 subconjuntos
size = int(len(train_data) / 10)
print "PARTE B\n"

totalCorrectPredictionsBayesian = 0
print "RESULTS BAYESIAN LEARNING:"
for i in range(0,10):

	#entreno con el train_data - el subocojunto 
	new_data = train_data[:i*size] + train_data[(i*size)+size:]
	#class with all data for bayesian learning
	bayesian = BayesianStruct(new_data)
	bayesian.processData()
	#evaluo con el subconjunto 
	testing_data = train_data[i*size:(i*size)+size]
	bayesian.evalData(testing_data)

	#evaluo con el subocojunto de train_data
	#PARA EL SUBCONJUNTO
	print "PARA EL SUBCOJUNTO QUE VA DE: " + str(i*size) + " a " + str((i*size)+size) 
	correctPredictionsBayesian = 0
	for item in testing_data:
		if item.probBayesian == item.y:
			correctPredictionsBayesian += 1
			totalCorrectPredictionsBayesian += 1
	print "Total cases: " + str(len(testing_data))
	print "Correct Predictions: " + str(correctPredictionsBayesian)
	print "Correctness percentage: " + str((correctPredictionsBayesian / len(testing_data)) * 100) + "%"
	print "------------------------------------------"

print "\nRESULTADO TOTAL CRUZAMIENTO DE TAMANIO 10: \n"
print "Total cases: " + str(len(train_data))
print "Correct Predictions: " + str(totalCorrectPredictionsBayesian)
print "Correctness percentage: " + str((totalCorrectPredictionsBayesian / len(train_data)) * 100) + "%"
print "------------------------------------------\n"

totalCorrectPredictionsKNN1 = 0
totalCorrectPredictionsKNN3 = 0
totalCorrectPredictionsKNN5 = 0
print "RESULTS KNN LEARNING:\n"
for i in range(0,10):

	#entreno con el train_data - el subocojunto 
	new_data = train_data[:i*size] + train_data[(i*size)+size:]
	start2 = time.clock() 

	knn = KNN(5, new_data)
	testing_data = train_data[i*size:(i*size)+size]
	knn.evalData(testing_data)	
	elapsed2 = time.clock()
	elapsed2 = elapsed2 - start2
	#evaluo con el subocojunto de train_data
	#PARA EL SUBCONJUNTO
	print "PARA EL SUBCOJUNTO QUE VA DE: " + str(i*size) + " a " + str((i*size)+size) 
	correctPredictionsKNN1 = 0
	correctPredictionsKNN3 = 0
	correctPredictionsKNN5 = 0
	for item in testing_data:
		if item.probKNN1 == item.y:
			correctPredictionsKNN1 += 1
			totalCorrectPredictionsKNN1 += 1
		if item.probKNN3 == item.y:
			correctPredictionsKNN3 += 1
			totalCorrectPredictionsKNN3 += 1
		if item.probKNN5 == item.y:
			correctPredictionsKNN5 += 1
			totalCorrectPredictionsKNN5 += 1
	print "Total cases: " + str(len(testing_data))
	print "For KNN1:"
	print "Correct Predictions: " + str(correctPredictionsKNN1)
	print "Correctness percentage: " + str((correctPredictionsKNN1 / len(testing_data)) * 100) + "%"
	print "For KNN3:"
	print "Correct Predictions: " + str(correctPredictionsKNN3)
	print "Correctness percentage: " + str((correctPredictionsKNN3 / len(testing_data)) * 100) + "%"
	print "For KNN5:"
	print "Correct Predictions: " + str(correctPredictionsKNN5)
	print "Correctness percentage: " + str((correctPredictionsKNN5 / len(testing_data)) * 100) + "%"
	print "Time spent in knn is: ", elapsed2
	print "------------------------------------------"

print "\nRESULTADO TOTAL CRUZAMIENTO DE TAMANIO 10: \n"
print "Total cases: " + str(len(train_data))
print "For KNN1:"
print "Correct Predictions: " + str(totalCorrectPredictionsKNN1)
print "Correctness percentage: " + str((totalCorrectPredictionsKNN1 / len(train_data)) * 100) + "%"
print "For KNN3:"
print "Correct Predictions: " + str(totalCorrectPredictionsKNN3)
print "Correctness percentage: " + str((totalCorrectPredictionsKNN3 / len(train_data)) * 100) + "%"
print "For KNN5:"
print "Correct Predictions: " + str(totalCorrectPredictionsKNN5)
print "Correctness percentage: " + str((totalCorrectPredictionsKNN5 / len(train_data)) * 100) + "%"
print "------------------------------------------"

## PARTE C!!!!!
# index_testing = 10
# testing_data = test_data
# print len(testing_data)
# bayesian = BayesianStruct(train_data)

# bayesian.processData()

# bayesian.evalData(testing_data)

# correctPredictionsBayesian = 0
# for item in testing_data:
# 	#print "GUESS: " + item.probBayesian
# 	#print "TRUTH: " + item.y
# 	if item.probBayesian == item.y:
# 		correctPredictionsBayesian += 1
# print "RESULTS BAYESIAN LEARNING:"
# print "Total cases: " + str(len(testing_data))
# print "Correct Predictions: " + str(correctPredictionsBayesian)
# print "Correctness percentage: " + str((correctPredictionsBayesian / len(testing_data)) * 100) + "%"

# start2 = time.clock() 

# knn = KNN(5, train_data)
# knn.evalData(testing_data)

# elapsed2 = time.clock()
# elapsed2 = elapsed2 - start2

# correctPredictionsKNN1 = 0
# for item in testing_data:
# 	#print "GUESS: " + item.probKNN1
# 	#print "TRUTH: " + item.y
# 	if item.probKNN1 == item.y:
# 		correctPredictionsKNN1 += 1

# print "RESULTS KNN - 1:"
# print "Total cases: " + str(len(testing_data))
# print "Correct Predictions: " + str(correctPredictionsKNN1)
# print "Correctness percentage: " + str((correctPredictionsKNN1 / len(testing_data)) * 100) + "%"

# correctPredictionsKNN3 = 0
# for item in testing_data:
# 	#print "GUESS: " + item.probKNN3
# 	#print "TRUTH: " + item.y
# 	if item.probKNN3 == item.y:
# 		correctPredictionsKNN3 += 1

# print "RESULTS KNN - 3:"
# print "Total cases: " + str(len(testing_data))
# print "Correct Predictions: " + str(correctPredictionsKNN3)
# print "Correctness percentage: " + str((correctPredictionsKNN3 / len(testing_data)) * 100) + "%"

# correctPredictionsKNN5 = 0
# for item in testing_data:
# 	#print "GUESS: " + item.probKNN5
# 	#print "TRUTH: " + item.y
# 	if item.probKNN5 == item.y:
# 		correctPredictionsKNN5 += 1

# print "RESULTS KNN - 5:"
# print "Total cases: " + str(len(testing_data))
# print "Correct Predictions: " + str(correctPredictionsKNN5)
# print "Correctness percentage: " + str((correctPredictionsKNN5 / len(testing_data)) * 100) + "%"

# print "Time spent in knn is: ", elapsed2
