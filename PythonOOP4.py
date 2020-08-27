# study of class
# Python_OOP

class SchoolEmployeeDb:
	def __init__(self, name, age, sid):
		self.name = name
		self.age = age
		self.sid = sid
		self.email = self.name + str(self.age) + '@school.in'

	def printID(self):
		print('Name: ' + self.name)
		print('Age: ' + str(self.age))
		print('SID: ' + str(self.sid))


class student(SchoolEmployeeDb):
	def __init__(self, name, age, sid, branch):
		super().__init__(name, age, sid)
		self.branch = branch

	def printSID(self):
		self.printID()
		print('Branch: ' + self.branch)


class Teacher(SchoolEmployeeDb):
	def __init__(self, name, age, sid, subject):
		super().__init__(name, age, sid)
		self.subject = subject

	def printTID(self):
		self.printID()
		print('Subject: ' + self.subject)


std_1 = student('Vaibhav', 20, 110021, 'CSE')
std_1.printSID()
tch_1 = Teacher('arnav', '42', '273813', 'DBMS')
tch_1.printTID()
