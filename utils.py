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
	