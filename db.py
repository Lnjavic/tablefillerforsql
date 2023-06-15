import names
import random

def getMonth_s(i):
	shorts = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
	return shorts[i];

def createDate():
	day = random.randint(1,29);
	year = random.randint(1920,1980)
	month = random.randint(0,11)
	
	fulldate = "{}-{}-{}".format(day,getMonth_s(month),year);
	return fulldate
	
def createREGDate():
	day = random.randint(1,29);
	year = random.randint(2000,2022)
	month = random.randint(0,11)
	
	fulldate = "{}-{}-{}".format(day,getMonth_s(month),year);
	return fulldate
	
def firstMaleName():
	a = len(names.malefnames)-1
	g = random.randint(0,a)
	
	fullname = "{}".format(names.malefnames[g])
	return fullname

def lastMaleName():
	a = len(names.surnames)-1
	g = random.randint(0,a)
	
	fullname = "{}".format(names.surnames[g])
	return fullname
	
def firstFemaleName():
	a = len(names.femalefnames)-1
	g = random.randint(0,a)
	
	fullname = "{}".format(names.femalefnames[g])
	return fullname

def lastfemaleName():
	a = len(names.femalelnames)-1
	g = random.randint(0,a)
	
	fullname = "{}".format(names.femalelnames[g])
	return fullname
	


def genPhone():
	number = random.randint(9999999,99999999);
	phoneNo = "07{}".format(number)
	return phoneNo
	
def genTelephone():
	number = random.randint(9999999,99999999);
	phoneNo = "02{}".format(number)
	return phoneNo
	
def genAccount():
	number = random.randint(900000,90000000);
	return number
	
def generateEmail(x):
	a = random.randint(0,100);
	email = "{}{}{}@gmail.com".format(x[0],a,x[1])
	return email.lower()
	
def generateIDno():
	id = random.randint(10000000,49999999)
	return id
	
def genPB():
	pb = random.randint(100000,4999999)
	return pb
	
def genEmployerCode():
	code = random.randint(1000,100000);
	return code
	
def generateKRA():
	pin = random.randint(10000000000,99999999999)
	KRApin = "ALX{}".format(pin)
	return KRApin
	
def genNSSF():
	b = random.randint(100,10000)
	return b
	
def genSalary():
	n = random.randint(1000,100000)
	return n
	
def genContribution():
	x = random.randint(0,2)
	cont = [1680,1200,2160]
	return cont[x]