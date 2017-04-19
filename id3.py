from math import log
import copy
from utils import *
	
#funcion que obtiene para un conjunto solo los que tiene los valores atribute = value
def getAttributeValues(attribute):
	if attribute == "age":
		return VALUES_AGE
	elif attribute == "job":
		return VALUES_JOB
	elif attribute == "marital":
		return VALUES_MARITAL
	elif attribute == "education":
		return VALUES_EDUCATION
	elif attribute == "default":
		return VALUES_DEFAULT
	elif attribute == "balance":
		return VALUES_BALANCE
	elif attribute == "housing":
		return VALUES_HOUSING
	elif attribute == "loan":
		return VALUES_LOAN
	elif attribute == "contact":
		return VALUES_CONTACT
	elif attribute == "day":
		return VALUES_DAY
	elif attribute == "month":
		return VALUES_MONTH
	elif attribute == "duration":
		return VALUES_DURATION
	elif attribute == "campaign":
		return VALUES_CAMPAIGN
	elif attribute == "pdays":
		return VALUES_PDAYS
	elif attribute == "previous":
		return VALUES_PREVIUOS
	elif attribute == "poutcome":
		return VALUES_POUTCOME
	

#funcion que obtiene para un conjunto solo los que tiene los valores atribute = value
def getDataAttributeValue(data,attribute,value):
	new_data = []
	for line in data:
		if getattr(line,attribute) == value:
			new_data.append(line)
	return new_data

#funcion que le paso un conjunto y me devuelve la cantidad de positivos y negativos
def getPositivesNegatives (data):
	#recorro el conjunto y sumo positivos y negativos
	positives = 0.0
	negatives = 0.0
	for line in data:
		#print line
		if line.y == "yes":
			positives += 1
		elif line.y == "no":
			negatives += 1
	
	return positives, negatives

#funcion que calcula la entropia, se le pasa la cantidad de positivos y negativos
def entropy(positives, negatives):

	total = float(positives + negatives)
	
	if positives == 0:
		entropy_positives = 0
	else:	
		entropy_positives = - ( positives / total ) * log ( ( positives / total ),2)

	if negatives == 0:
		entropy_negatives = 0
	else:
		entropy_negatives = - ( negatives / total ) * log ( (negatives / total ), 2 )
	
	return entropy_positives + entropy_negatives


#se calcula la ganancia, para un conjunto dado	
def gain(data,attribute):

	positives_data, negatives_data = getPositivesNegatives(data)
	total_data = positives_data + negatives_data
	
	gain = entropy(positives_data, negatives_data)
	#obterngo posibles
	attribute_values = getAttributeValues(attribute)

	for value in attribute_values:
		
		new_data = getDataAttributeValue(data,attribute,value)
	
		positives_new_data, negatives_new_data = getPositivesNegatives(new_data)
		total_new_data = positives_new_data + negatives_new_data
		
		entropy_new_data = entropy(positives_new_data, negatives_new_data)

		gain -= ( total_new_data / total_data ) * entropy_new_data
	
	return gain
	
def id3Algorthm (data,attributes,node,common_answer):

	if (not data) or (not attributes):
		#si no me queda data, tomo el valor mas comun del padre
		node.setInfo(common_answer)
	else:
		positives,negatives = getPositivesNegatives(data)
		if positives == 0:
			#es una hoja negativa
			node.setInfo("no")
		elif negatives == 0:
			#es una hoja positiva
			node.setInfo("yes")
		else:
			if positives >= negatives:
				moment_answer = "yes"
			else:
				moment_answer = "no"
			#sigo iterando, buscando un nuevo atributo
			best_gain = -1
			info_attribute = ""
			# calculo para todos los atributos su ganancia y me quedo con el de ganancia mayor
			for attribute in attributes:
				attr_gain = gain(data,attribute)
				if attr_gain > best_gain:
					best_gain = attr_gain
					info_attribute = attribute
				if best_gain == 1:
					#si hay ganancia 1 ya encontre uno de los mejores
					break

			#creo el tree con la raiz el atributo otenido
			#y con sus hijos todos los valores posibles del attribute
			info_attr_values = getAttributeValues(info_attribute)
			node.setInfo(info_attribute)
			for info_value in info_attr_values:
			
				new_data = getDataAttributeValue(data,info_attribute,info_value)
				new_node = Node()	
				new_node.setValueForm(info_value)
				new_attributes = copy.deepcopy(attributes)
				new_attributes.remove(info_attribute)
				#realizo la recursion sobre el arbol y luego agrego el sub arbol obtenido como hijo del actual				
				id3Algorthm(new_data,new_attributes,new_node,moment_answer)
				node.setChild(new_node)
				
		

	
