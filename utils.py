#CUANDO SON VALORES NUMERICOS HACEMOS UN PROCESAMIENTO DE LOS DATOS PARA CREAR INTERVALOS, Y LUEGO AL CREAR EL OBJETO LINE
#LO ASIGNAMOS DENTRO DE UNO DE LOS VALORES YA EXISTENTES
VALUES_AGE = ["teen","adult","grown","elder"]
VALUES_JOB =  ["admin.","blue-collar","entrepreneur","housemaid","management","retired","self-employed","services","student","technician","unemployed","unknown"]
VALUES_MARITAL = ["divorced","married","single","unknown"]
#VALUES_EDUCATION = ["basic.4y","basic.6y","basic.9y","high.school","illiterate","professional.course","university.degree","unknown"]
VALUES_EDUCATION = ["primary","secondary","tertiary","unknown"]
VALUES_DEFAULT = ["no","yes","unknown"]
VALUES_BALANCE = ["low", "mid-low", "mid-high","high"]
VALUES_HOUSING = ["no","yes","unknown"]
VALUES_LOAN = ["no","yes","unknown"]
VALUES_CONTACT = ["cellular","telephone","unknown"]
VALUES_DAY = ["start","mid-start","mid-end","end"]
VALUES_MONTH = ["jan", "feb", "mar", "apr", "may","jun","jul","aug","sep","oct","nov", "dec"]
VALUES_DURATION = ["short", "mid-short", "mid-long","long"]
VALUES_CAMPAIGN = ["low", "mid-low", "mid-high","high"]
VALUES_PDAYS = ["low", "mid-low", "mid-high","high"]
VALUES_PREVIUOS = ["low", "mid-low", "mid-high","high"]
VALUES_POUTCOME = ["failure","other","success","unknown"]

#clase usada para la generacion del arbol de decision
class Node:
   
	def __init__(self):
		self.info = ""
		self.value_from = ""
		self.children = []

	def printNode(self):

		print "node info: " + self.info
		print "node value: " + self.value_from
		hijo = 1
		for c in self.children:
			print "hijo: "  + str(hijo) + " de " + str(self.info)
			c.printNode()
			hijo +=1
			
	def setInfo(self,info):
		self.info = info

	def setValueForm(self,value_from):
		self.value_from = value_from
		
	def setChild(self,child):
		self.children.append(child)
		
	def eval(self, line):
		if (self.children == []) and ((self.info == "yes") or (self.info == "no")):
			return (line.y == self.info)
		else:
			for child in self.children:
				lineAtributeValue = getattr(line, self.info)
				if (child.value_from == lineAtributeValue):
					return (child.eval(line))
				
class Line:

	def __init__(self,age1,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome,y):
		self.age = age1
		self.job = job
		self.marital   = marital
		self.education = education
		self.default   = default
		self.balance   = balance
		self.housing   = housing
		self.loan      = loan
		self.contact   = contact
		self.day       = day
		self.month     = month
		self.duration  = duration
		self.campaign  = campaign
		self.pdays     = pdays
		self.previous  = previous
		self.poutcome  = poutcome
		self.y         = y
	
	def printLine(self):
		
		print "Age:  " + self.age
		print "Job: " + self.job
		print "Marital: " + self.marital
		print "Education: " + self.education
		print "Default: " + self.default
		print "Balance: " + self.balance
		print "Housing: " + self.housing
		print "Loan: " + self.loan
		print "Contact: " + self.contact
		print "Day: " + self.day
		print "Month: " + self.month
		print "Duration: " + self.duration
		print "Campaign: " + self.campaign
		print "Pdays: " + self.pdays
		print "Previous: " + self.previous
		print "Poutcome: " + self.poutcome
		print "Y: " + self.y
		print "--------------------"	
	