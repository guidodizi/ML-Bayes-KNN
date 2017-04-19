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

#dictionaries with all values of attribute and a tuple with number of yes and no for that value
dict_age = {"teen":(0,0),"adult":(0,0),"grown":(0,0),"elder":(0,0)}
dict_job = {"admin.":(0,0),"blue-collar":(0,0),"entrepreneur":(0,0),"housemaid":(0,0),"management":(0,0),"retired":(0,0),"self-employed":(0,0),"services":(0,0),"student":(0,0),"technician":(0,0),"unemployed":(0,0),"unknown":(0,0)}
dict_marital = {"divorced":(0,0),"married":(0,0),"single":(0,0),"unknown":(0,0)}
dict_education = {"basic.4y":(0,0),"basic.6y":(0,0),"basic.9y":(0,0),"high.school":(0,0),"illiterate":(0,0),"professional.course":(0,0),"university.degree":(0,0),"unknown":(0,0)}
dict_default = {"no":(0,0),"yes":(0,0),"unknown":(0,0)}
dict_housing = {"no":(0,0),"yes":(0,0),"unknown":(0,0)}
dict_loan = {"no":(0,0),"yes":(0,0),"unknown":(0,0)}
dict_contact = {"cellular":(0,0),"telephone":(0,0)}
dict_month = {"jan":(0,0), "feb":(0,0), "mar":(0,0), "apr":(0,0), "may":(0,0),"jun":(0,0),"jul":(0,0),"aug":(0,0),"sep":(0,0),"oct":(0,0),"nov":(0,0), "dec":(0,0)}
dict_day_of_week = {"mon":(0,0),"tue":(0,0),"wed":(0,0),"thu":(0,0),"fri":(0,0)}
dict_duration = {"short":(0,0), "mid-short":(0,0), "mid-long":(0,0),"long":(0,0)}
dict_campaign = {"low":(0,0), "mid-low":(0,0), "mid-high":(0,0),"high":(0,0)}
dict_pdays = {"low":(0,0), "mid-low":(0,0), "mid-high":(0,0),"high":(0,0)}
dict_previous = {"low":(0,0), "mid-low":(0,0), "mid-high":(0,0),"high":(0,0)}
dict_poutcome = {"failure":(0,0),"nonexistent":(0,0),"success":(0,0)}
dict_emp_var_rate = {"low":(0,0), "mid-low":(0,0), "mid-high":(0,0),"high":(0,0)}
dict_cons_price_idx = {"low":(0,0), "mid-low":(0,0), "mid-high":(0,0),"high":(0,0)}
dict_cons_conf_idx = {"low":(0,0), "mid-low":(0,0), "mid-high":(0,0),"high":(0,0)}
dict_euribor3m = {"low":(0,0), "mid-low":(0,0), "mid-high":(0,0),"high":(0,0)}
dict_nr_employed = {"low":(0,0), "mid-low":(0,0), "mid-high":(0,0),"high":(0,0)}

numYes = 0
numNo = 0
for item in train_data:
	if item.y = "yes"
		#add to age dictonary, on key item.age, to the place 0 of the tuple, which corresponds to YES
		dict_age[item.age][0] =+ 1
		dict_job[item.job][0] =+ 1
		dict_marital[item.marital][0] =+ 1
		dict_education[item.education][0] =+ 1
		dict_default[item.default][0] =+ 1
		dict_housing[item.housing][0] =+ 1
		dict_loan[item.loan][0] =+ 1
		dict_contact[item.contract][0] =+ 1
		dict_month[item.month][0] =+ 1
		dict_day_of_week[item.day_of_week][0] =+ 1
		dict_duration[item.duration][0] =+ 1
		dict_campaign[item.campaign][0] =+ 1
		dict_pdays[item.pdays][0] =+ 1
		dict_previous[item.previous][0] =+ 1
		dict_poutcome[item.poutcome][0] =+ 1
		dict_emp_var_rate[item.emp_var_rate][0] =+ 1
		dict_cons_price_idx[item.cons_price_idx][0] =+ 1
		dict_cons_conf_idx[item.cons_conf_idx][0] =+ 1
		dict_euribor3m[item.euribor3m][0] =+ 1
		dict_nr_employed[item.nr_employed][0] =+ 1

		numYes += 1
	elif item.y = "no"
		#add to age dictonary, on key item.age, to the place 1 of the tuple, which corresponds to NO	
		dict_age[item.age][1] =+ 1
		dict_job[item.job][1] =+ 1
		dict_marital[item.marital][1] =+ 1
		dict_education[item.education][1] =+ 1
		dict_default[item.default][1] =+ 1
		dict_housing[item.housing][1] =+ 1
		dict_loan[item.loan][1] =+ 1
		dict_contact[item.contract][1] =+ 1
		dict_month[item.month][1] =+ 1
		dict_day_of_week[item.day_of_week][1] =+ 1
		dict_duration[item.duration][1] =+ 1
		dict_campaign[item.campaign][1] =+ 1
		dict_pdays[item.pdays][1] =+ 1
		dict_previous[item.previous][1] =+ 1
		dict_poutcome[item.poutcome][1] =+ 1
		dict_emp_var_rate[item.emp_var_rate][1] =+ 1
		dict_cons_price_idx[item.cons_price_idx][1] =+ 1
		dict_cons_conf_idx[item.cons_conf_idx][1] =+ 1
		dict_euribor3m[item.euribor3m][1] =+ 1
		dict_nr_employed[item.nr_employed][1] =+ 1
		numNo += 1
p_Yes = float(numYes / (numYes + numNo))
p_No = float(numNo / (numYes + numNo))

