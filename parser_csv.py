import csv
from utils import * 
import string
import sys
from operator import is_not
from functools import partial

FILE_NAME = 'bank-additional-full.csv'
#FILE_NAME = 'bank.csv'

class Common_Values:
	
	def __init__(self):
		self.jobs = [0] * len(VALUES_JOB)
		self.marital = [0] * len(VALUES_MARITAL)
		self.education = [0] * len(VALUES_EDUCATION)
		self.default = [0] * len(VALUES_DEFAULT)
		self.housing = [0] * len(VALUES_HOUSING)
		self.loan = [0] * len(VALUES_LOAN)
		self.contact = [0] * len(VALUES_CONTACT)
		self.poutcome = [0] * len(VALUES_POUTCOME)
		
def isFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False


def getInterval(interval ,value):
	i=0
	while i < len(interval):
		if interval[i][0] <= value <= interval[i][1]:
			return i

def replaceNumericValues():
	intervals = makeIntervals(min,max,4)
	for item in items:
		attr = 0
		for attribute in item:
			if attribute.isnumeric():
				item.attribute = getInterval(intervals[i],item.attribute)
				
def makeIntervals(min,max,qty):
	i = 0
	intervals = []
	while i < len(min):
		j = 0
		intervals_med = []
		size = (float(max[i]) - float(min[i]))/qty
		leftLimits = []
		rightLimits = []
		while j < qty:	
			if  j == 0:
				interval = [int(min[i])+size*(j+1)]			
			elif j == qty -1: 
				interval = [int(min[i])+size*j]	
			else:
				interval = [int(min[i])+size*j, int(min[i])+size*(j+1)]
			intervals_med.append(interval)
			j+=1
		i+=1
		intervals.append(intervals_med)
	return intervals

def createIntervalsAttributes():
	first = True
	second = True
	common_values = Common_Values()
	attributes = []
	numericAtt = []
	with open(FILE_NAME, 'rb') as csvfile:
		for line in csvfile.readlines():
			if first:
				first = False
				c = line.split(';')
				for a in c:
					attribute = str.replace(a,'"','')
					attribute = str.replace(attribute,'\n','')	
					attribute = str.replace(attribute,'\r','')												
					attribute = str.replace(attribute,'.','_')												
					attributes.append(attribute)
				size = len(attributes)
				min = [None] * size
				max = [None] * size
			else:
				c = line.split(';')
				i = 0
				for a in c:
					attribute = str.replace(a,'"','')
					attribute = str.replace(attribute,'\n','')
					attribute = str.replace(attribute,'\r','')		
					if i == 1:
					#attribute jobs
						ind = VALUES_JOB.index(attribute)
						common_values.jobs[ind] += 1
					elif i == 2:
					#attribute marital						
						ind = VALUES_MARITAL.index(attribute)
						common_values.marital[ind] += 1
					elif i == 3:
					#attribute education
						ind = VALUES_EDUCATION.index(attribute)
						common_values.education[ind] += 1
					elif i == 4:
					#attribute default
						ind = VALUES_DEFAULT.index(attribute)
						common_values.default[ind] += 1
					elif i == 5:
					#attribute housing
						ind = VALUES_HOUSING.index(attribute)
						common_values.housing[ind] += 1
					elif i == 6:
					#attribute loan
						ind = VALUES_LOAN.index(attribute)
						common_values.loan[ind] += 1
					elif i == 7:
					#attribute contact
						ind = VALUES_CONTACT.index(attribute)
						common_values.contact[ind] += 1
					elif i == 14:
					#attribute poutcome
						ind = VALUES_POUTCOME.index(attribute)
						common_values.poutcome[ind] += 1			
					if isFloat(attribute):
						if second:
							numericAtt.append(attributes[i])
						if min[i] == None or float(attribute) < min[i]:						
							min[i]= float(attribute)					
						elif max[i] == None or float(attribute) > max[i]:
							max[i]= float(attribute)
					i+=1
				second = False
		min = filter(partial(is_not, None), min)
		max = filter(partial(is_not, None), max)
		intervals = makeIntervals(min,max,4)
		
	return intervals,attributes,common_values

def getData(intervals,attributes,common_values, fix_unknown = False):
	first = True
	items = []
	with open(FILE_NAME, 'rb') as csvfile:
		first = True
		for line in csvfile.readlines():
			if first:
				first = False
			else:
				l = []
				c = line.split(';')
				i = 0
				for a in c:
					attribute_value = str.replace(a,'"','')
					attribute_value = str.replace(attribute_value,'\n','')
					attribute_value = str.replace(attribute_value,'\r','')	
					if (fix_unknown) and (attribute_value == "unknown"):
						if i == 1:
						#attribute jobs
							attribute_value = VALUES_JOB[common_values.jobs.index(max(common_values.jobs))]
						elif i == 2:
						#attribute marital						
							attribute_value = VALUES_MARITAL[common_values.marital.index(max(common_values.marital))]
						elif i == 3:
						#attribute education
							attribute_value = VALUES_EDUCATION[common_values.education.index(max(common_values.education))]
						elif i == 4:
						#attribute default
							attribute_value = VALUES_DEFAULT[common_values.default.index(max(common_values.default))]
						elif i == 5:
						#attribute housing
							attribute_value = VALUES_HOUSING[common_values.housing.index(max(common_values.housing))]
						elif i == 6:
						#attribute loan
							attribute_value = VALUES_LOAN[common_values.loan.index(max(common_values.loan))]
						elif i == 7:
						#attribute contact
							attribute_value = VALUES_CONTACT[common_values.contact.index(max(common_values.contact))]
						elif i == 14:
						#attribute poutcome
							attribute_value = VALUES_POUTCOME[common_values.poutcome.index(max(common_values.poutcome))]
					
					if isFloat(attribute_value):
						if i == 0:#es age
							interval = intervals[0]
							values = VALUES_AGE
						elif i == 10:#es duration
							interval = intervals[1]
							values = VALUES_DURATION
						elif i == 11:#es campaign
							interval = intervals[2]
							values = VALUES_CAMPAIGN
						elif i == 12:#es paydays
							interval = intervals[3]
							values = VALUES_PDAYS
						elif i == 13:#es previous
							interval = intervals[4]
							values = VALUES_PREVIOUS
						elif i == 14:#es emp_var_rate
							interval = intervals[5]
							values = VALUES_PREVIOUS
						elif i == 15:#es cons_price_idx
							interval = intervals[6]
							values = VALUES_PREVIOUS
						elif i == 16:#es cons_conf_idx
							interval = intervals[7]
							values = VALUES_PREVIOUS
						elif i == 17:#es euribor3m
							interval = intervals[8]
							values = VALUES_PREVIOUS
						elif i == 18:#es nr_employed
							interval = intervals[9]
							values = VALUES_PREVIOUS
										
						if float(attribute_value) < interval[0][0]:
							attribute_value = values[0]
						elif float(attribute_value) >= interval[1][0] and float(attribute_value) < interval[1][1]:
							attribute_value = values[1]
						elif float(attribute_value) >= interval[2][0] and float(attribute_value) < interval[2][1]:
							attribute_value = values[2]
						elif float(attribute_value) >= interval[3][0]:
							attribute_value = values[3]
					i += 1
						
					l.append(attribute_value)
				item = Line(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17],l[18],l[19],l[20])
				items.append(item)
	return items
			