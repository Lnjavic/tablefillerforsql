import db
import random

class structure:
	def __init__(self):
		pass

	def member_structure(self):
		x = random.randint(1,2)
		gender = ""
		a = b = ""
		if x == 1:
			a = db.firstMaleName()
			b = db.lastMaleName()
			gender = "Male"
		else:
			a = db.firstFemaleName()
			b = db.lastfemaleName()
			gender = "Female"

		return{
		"firstName":a,
		"lastName":b,
		"nationalID":db.generateIDno(),
		"phoneNumber":db.genPhone(),
		"emailAddress":db.generateEmail([a,b]),
		"gender":gender,
		"dateOfBirth":db.createDate(),
		"dateOfReg":db.createREGDate()
		}

	def contribution_structure(self):
		methods = ["Employer remittance","Mpesa","Bank transfer"]
		return{
		"memberID":"",
		"amount":db.genSalary(),
		"Date":db.createREGDate(),
		"method":methods[random.randint(0,2)],
		}

	def benefit_structure(self):
		reasons = ["Death","Retirement","Disability"]
		return{
		"memberID":"",
		"amount":db.genSalary(),
		"date":db.createREGDate(),
		"reason":reasons[random.randint(0,2)]
		}

	def dependants_structure(self):
		rel = ["Son","Daughter","Father","Mother","Sister","Brother","Wife","Husband"]
		return{
		"memberID":"",
		"firstname":"",
		"lastName":"",
		"relationship":"",
		"dateOfBirth":db.createDate()
		}

