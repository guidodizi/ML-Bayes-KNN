# -*- encoding: utf-8 -*-
from parser_csv import *	
from random import shuffle
from prueba import *
	
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
#divido el coprus en 4/5 y 1/5
index = ( len(data) / 5 ) 
#1/5
test_data = data[:index]
#4/5
train_data = data[index:] 

#PARTE B
#validacion cruzada, divido mi train data en 10 subconjuntos
size = len(train_data) / 10
train_data_sub = []
print "PARTE B\n"

total_sum = 0
total_good = 0
for i in range(0,10):

	#entreno con el train_data - el subocojunto 
	node = Node()
	new_data = train_data[:i*size] + train_data[(i*size)+size:]
	
	id3Algorthm(new_data,attributes[:-1],node,"")

	#evaluo con el subocojunto de train_data
	#PARA EL SUBCONJUNTO
	print "PARA EL SUBCOJUNTO QUE VA DE: " + str(i*size) + " a " + str((i*size)+size) 
	total = 0
	good = 0
	for z in train_data[i*size:(i*size)+size]:
		if node.eval(z):
			good += 1
		total += 1
	total_good += good
	total_sum += total
	print "RESULTADO PRUEBA: \n Correctos: " + str(good) + "\n Total: " + str(total) + "\n Porcentaje acierto: " + str((good * 100) / total)  + "%"
	print "------------------------------------------"

print "\nRESULTADO TOTAL CRUZAMIENTO DE TAMANIO 10: \n Correctos: " + str(total_good) + "\n Total: " + str(total_sum) + "\n Porcentaje acierto: " + str((total_good * 100) / total_sum)  + "%"
print "------------------------------------------"
#PARTE C
print "\n PARTE C \n"
#entreno con el train data
node = Node()
id3Algorthm(train_data,attributes[:-1],node,"")
#evaluo con el test_data
for t in test_data:	
	if node.eval(t):
		good += 1
	total += 1

print "RESULTADO PRUEBA: \n Correctos: " + str(good) + "\n Total: " + str(total) + "\n Porcentaje acierto: " + str((good * 100) / total)  + "%"
print "------------------------------------------"

