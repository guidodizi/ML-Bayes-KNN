# -*- encoding: utf-8 -*-
from parser_csv import *	
from random import shuffle
	
#primero obtengo los intervalos y atributos
intervals, attributes = createIntervalsAttributes()
#me creo el data
data = getData(intervals,attributes)
#hago un shuffle del corpus
shuffle(data)
#divido el coprus en 4/5 y 1/5
index = ( len(data) / 5 ) 
#1/5
test_data = data[:index]
#4/5
train_data = data[index:] 

#class with all data for bayesian learning
struct = Struct(train_data)
struct.processData()

