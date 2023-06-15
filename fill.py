import obj_ects
import cx_Oracle
import random
import test
from config import config
from cryptography.fernet import Fernet


conn = cx_Oracle.connect(
	user=config.username,password=config.password,dsn="localhost/XEPDB1",encoding="UTF-8"
	)

cursor = conn.cursor()


class make_dbs(test.createTables):
	def __init__(self):
		super().__init__()

dbs = make_dbs()


class filler(obj_ects.structure):
	def __init__(self):

		self.member_fill = """
INSERT INTO members (
firstName,lastName,nationalID,phoneNumber,emailAddress,
gender,dateOfBirth,dateOfRegistration
) VALUES (:x,:x,:x,:x,:x,:x,:X,:X)
		"""
		self.cont_fill = """
INSERT INTO contribution (
memberID,amount,dateOfContribution,paymentMethod)
VALUES (:x,:x,:x,:x)

		"""
		self.benefit_fill = """
INSERT INTO benefits (
memberID,amountBenefited,dateOfBenefit,reasonForBenefit
) VALUES (:x,:x,:x,:x)

		"""
		self.dependant_fill = """
INSERT INTO dependants (
dependedMemberID,
firstName,
lastName,
gender,
relationship,
dateOfBirth
)
VALUES (:x,:x,:x,:x,:x,:x)

		"""
		self.member_info = []

	def fill_table_members(self):
		a = super().member_structure()
		file = open("crypt.txt","rb")
		key = file.read()
		f = Fernet(key)
		string = str(a["nationalID"]).encode()
		token = f.encrypt(string)
		file.close()
		params = [a["firstName"],a["lastName"],token.decode(),a["phoneNumber"],a["emailAddress"],a["gender"],a["dateOfBirth"],a["dateOfReg"]]

		try:
			cursor.execute(self.member_fill,params)
			conn.commit()
		except cx_Oracle.Error as rr:
			print(rr)

	def get_members(self):
		get= "SELECT memberID,firstName,lastName,gender,dateOfBirth FROM members"
		cursor.execute(get)
		for x in cursor:
			self.member_info.append(x)



	def fill_table_contribution(self):
		a = super().contribution_structure()
		d = random.randint(0,len(self.member_info)-1)

		params = [self.member_info[d][0],a["amount"],a["Date"],a["method"]]

		try:

			cursor.execute(self.cont_fill,params)
			conn.commit()
		except cx_Oracle.Error as rr:
	
			print(rr)

	def fill_table_benefits(self):
		a = super().benefit_structure()
		d = random.randint(0,len(self.member_info)-1)

		params = [self.member_info[d][0],a["amount"],a["date"],a["reason"]]
		try:

			cursor.execute(self.benefit_fill,params)
			conn.commit()
		except cx_Oracle.Error as rr:
			print(rr)

	def fill_table_dependant(self):
		a = super().dependants_structure()
		d = random.randint(0,len(self.member_info)-1)

		males = ["Father","Son","Brother"]
		females = ["Mother","Daughter","Sister"]

		rela = ""

		gender = self.member_info[d][3]

		if gender == "Female":
			rela = females[random.randint(0,2)]
		else:
			rela = males[random.randint(0,2)]

		params = [self.member_info[d][0],self.member_info[d][1],self.member_info[d][2],self.member_info[d][3],rela,a["dateOfBirth"]]
		try:
			cursor.execute(self.dependant_fill,params)
			conn.commit()
		except cx_Oracle.Error as rr:

			print(rr)


