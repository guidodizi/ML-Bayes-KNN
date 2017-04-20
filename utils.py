from __future__ import division

# age (numeric)
# job : type of job (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')
# marital : marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)
# education (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')
# default: has credit in default? (categorical: 'no','yes','unknown')
# housing: has housing loan? (categorical: 'no','yes','unknown')
# loan: has personal loan? (categorical: 'no','yes','unknown')
# # related with the last contact of the current campaign:
# contact: contact communication type (categorical: 'cellular','telephone') 
# month: last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')
# day_of_week: last contact day of the week (categorical: 'mon','tue','wed','thu','fri')
# duration: last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.
# # other attributes:
# campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
# pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
# previous: number of contacts performed before this campaign and for this client (numeric)
# poutcome: outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')
# # social and economic context attributes
# emp_var_rate: employment variation rate - quarterly indicator (numeric)
# cons_price_idx: consumer price index - monthly indicator (numeric) 
# cons_conf_idx: consumer confidence index - monthly indicator (numeric) 
# euribor3m: euribor 3 month rate - daily indicator (numeric)
# nr_employed: number of employees - quarterly indicator (numeric)
# #Output variable (desired target):
# 21 - y - has the client subscribed a term deposit? (binary: 'yes','no')

#CUANDO SON VALORES NUMERICOS HACEMOS UN PROCESAMIENTO DE LOS DATOS PARA CREAR INTERVALOS, Y LUEGO AL CREAR EL OBJETO LINE
#LO ASIGNAMOS DENTRO DE UNO DE LOS VALORES YA EXISTENTES
VALUES_AGE = ["teen","adult","grown","elder"]
VALUES_JOB =  ["admin.","blue-collar","entrepreneur","housemaid","management","retired","self-employed","services","student","technician","unemployed","unknown"]
VALUES_MARITAL = ["divorced","married","single","unknown"]
VALUES_EDUCATION = ["basic.4y","basic.6y","basic.9y","high.school","illiterate","professional.course","university.degree","unknown"]
VALUES_DEFAULT = ["no","yes","unknown"]
VALUES_HOUSING = ["no","yes","unknown"]
VALUES_LOAN = ["no","yes","unknown"]
VALUES_CONTACT = ["cellular","telephone"]
VALUES_MONTH = ["jan", "feb", "mar", "apr", "may","jun","jul","aug","sep","oct","nov", "dec"]
VALUES_DAY_OF_WEEK = ["mon","tue","wed","thu","fri"]
VALUES_DURATION = ["short", "mid-short", "mid-long","long"]
VALUES_CAMPAIGN = ["low", "mid-low", "mid-high","high"]
VALUES_PDAYS = ["low", "mid-low", "mid-high","high"]
VALUES_PREVIOUS = ["low", "mid-low", "mid-high","high"]
VALUES_POUTCOME = ["failure","nonexistent","success"]
VALUES_EMP_VAR_RATE = ["low", "mid-low", "mid-high","high"]
VALUES_CONS_PRICE_IDX = ["low", "mid-low", "mid-high","high"]
VALUES_CONS_CONF_IDX = ["low", "mid-low", "mid-high","high"]
VALUES_EURIBOR3M = ["low", "mid-low", "mid-high","high"]
VALUES_NR_EMPLOYED = ["low", "mid-low", "mid-high","high"]

class Line:
	def __init__(self,age,job,marital,education,default,housing,loan,contact,month,day_of_week,duration,
	campaign,pdays,previous,poutcome,emp_var_rate,cons_price_idx,cons_conf_idx,euribor3m,nr_employed,y):
		self.age = age
		self.job = job
		self.marital = marital
		self.education = education
		self.default = default
		self.housing = housing
		self.loan = loan
		self.contact = contact
		self.month = month
		self.day_of_week = day_of_week
		self.duration = duration
		self.campaign = campaign
		self.pdays = pdays
		self.previous = previous
		self.poutcome = poutcome
		self.emp_var_rate = emp_var_rate
		self.cons_price_idx = cons_conf_idx
		self.cons_conf_idx = cons_conf_idx
		self.euribor3m = euribor3m
		self.nr_employed = nr_employed
		self.y = y

class Struct:
	def __init__(self, train_data):
		self.train_data = train_data
		self.numYes = 0
		self.numNo = 0
		#dictionaries with all values of attribute and a tuple with numbers of yes and no for that value
		self.dict_age = {}
		for value in VALUES_AGE:
			self.dict_age.setdefault(value, [0,0])

		self.dict_job = {}
		for value in VALUES_JOB:
			self.dict_job.setdefault(value, [0,0])

		self.dict_marital = {}
		for value in VALUES_MARITAL:
			self.dict_marital.setdefault(value, [0,0])

		self.dict_education = {}
		for value in VALUES_EDUCATION:
			self.dict_education.setdefault(value, [0,0])

		self.dict_default = {}
		for value in VALUES_DEFAULT:
			self.dict_default.setdefault(value, [0,0])

		self.dict_housing = {}
		for value in VALUES_HOUSING:
			self.dict_housing.setdefault(value, [0,0])

		self.dict_loan = {}
		for value in VALUES_LOAN:
			self.dict_loan.setdefault(value, [0,0])

		self.dict_contact = {}
		for value in VALUES_CONTACT:
			self.dict_contact.setdefault(value, [0,0])

		self.dict_month = {}
		for value in VALUES_MONTH:
			self.dict_month.setdefault(value, [0,0])

		self.dict_day_of_week  = {}
		for value in VALUES_DAY_OF_WEEK:
			self.dict_day_of_week.setdefault(value, [0,0])

		self.dict_duration  = {}
		for value in VALUES_DURATION:
			self.dict_duration.setdefault(value, [0,0])

		self.dict_campaign  = {}
		for value in VALUES_CAMPAIGN:
			self.dict_campaign.setdefault(value, [0,0])

		self.dict_pdays = {}
		for value in VALUES_PDAYS:
			self.dict_pdays.setdefault(value, [0,0])

		self.dict_previous = {}
		for value in VALUES_PREVIOUS:
			self.dict_previous.setdefault(value, [0,0])

		self.dict_poutcome = {}
		for value in VALUES_POUTCOME:
			self.dict_poutcome.setdefault(value, [0,0])

		self.dict_emp_var_rate = {}
		for value in VALUES_EMP_VAR_RATE:
			self.dict_emp_var_rate.setdefault(value, [0,0])

		self.dict_cons_price_idx = {}
		for value in VALUES_CONS_PRICE_IDX:
			self.dict_cons_price_idx.setdefault(value, [0,0])

		self.dict_cons_conf_idx = {}
		for value in VALUES_CONS_CONF_IDX:
			self.dict_cons_conf_idx.setdefault(value, [0,0])

		self.dict_euribor3m = {}
		for value in VALUES_EURIBOR3M:
			self.dict_euribor3m.setdefault(value, [0,0])

		self.dict_nr_employed = {}
		for value in VALUES_NR_EMPLOYED:
			self.dict_nr_employed.setdefault(value, [0,0])

	def processData(self):
		for item in self.train_data:
			if item.y == "yes":
				#add to age dictonary, on key item.age, to the place 0 of the tuple, which corresponds to YES
				self.dict_age[item.age][0] += 1
				self.dict_job[item.job][0] += 1
				self.dict_marital[item.marital][0] += 1
				self.dict_education[item.education][0] += 1
				self.dict_default[item.default][0] += 1
				self.dict_housing[item.housing][0] += 1
				self.dict_loan[item.loan][0] += 1
				self.dict_contact[item.contact][0] += 1
				self.dict_month[item.month][0] += 1
				self.dict_day_of_week[item.day_of_week][0] += 1
				self.dict_duration[item.duration][0] += 1
				self.dict_campaign[item.campaign][0] += 1
				self.dict_pdays[item.pdays][0] += 1
				self.dict_previous[item.previous][0] += 1
				self.dict_poutcome[item.poutcome][0] += 1
				self.dict_emp_var_rate[item.emp_var_rate][0] += 1
				self.dict_cons_price_idx[item.cons_price_idx][0] += 1
				self.dict_cons_conf_idx[item.cons_conf_idx][0] += 1
				self.dict_euribor3m[item.euribor3m][0] += 1
				self.dict_nr_employed[item.nr_employed][0] += 1

				self.numYes += 1
			elif item.y == "no":
				#add to age dictonary, on key item.age, to the place 1 of the tuple, which corresponds to NO	
				self.dict_age[item.age][1] += 1
				self.dict_job[item.job][1] += 1
				self.dict_marital[item.marital][1] += 1
				self.dict_education[item.education][1] += 1
				self.dict_default[item.default][1] += 1
				self.dict_housing[item.housing][1] += 1
				self.dict_loan[item.loan][1] += 1
				self.dict_contact[item.contact][1] += 1
				self.dict_month[item.month][1] += 1
				self.dict_day_of_week[item.day_of_week][1] += 1
				self.dict_duration[item.duration][1] += 1
				self.dict_campaign[item.campaign][1] += 1
				self.dict_pdays[item.pdays][1] += 1
				self.dict_previous[item.previous][1] += 1
				self.dict_poutcome[item.poutcome][1] += 1
				self.dict_emp_var_rate[item.emp_var_rate][1] += 1
				self.dict_cons_price_idx[item.cons_price_idx][1] += 1
				self.dict_cons_conf_idx[item.cons_conf_idx][1] += 1
				self.dict_euribor3m[item.euribor3m][1] += 1
				self.dict_nr_employed[item.nr_employed][1] += 1

				self.numNo += 1
		self.p_Yes = (self.numYes / (self.numYes + self.numNo)) * 100
		self.p_No = (self.numNo / (self.numYes + self.numNo)) * 100
