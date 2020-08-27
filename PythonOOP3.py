# study of classes
# python object oriented programming
# class methods and static methods


class student:
	Exam_status = 'PASS'

	def __init__(self, name, email, userid):
		self.name = name
		self.email = email
		self.userid = userid

	def printidCard(self):
		print("Student Name: " + self.name)
		print("Student Email ID: " + self.email)
		print("Student ID: " + str(self.userid))
		print("Student Status: " + student.Exam_status, end='\n\n')

	@classmethod
	def from_string(cls, data):
		name, email, userid = data.split()
		return cls(name, email, userid)

	@classmethod
	def set_status(cls, status):
		student.Exam_status = status


# 	@staticmethod
# 	def even(num):
# 		if num % 2 == 0:
# 			print('EVEN')
# 		else:
# 			print('ODD')
#
# student.even(8)

S0 = student('saurabh', 'sps@gmail.com', 463246)
data = 'vaibhav vps@gmail.com 110233'
S1 = student.from_string(data)
S1.printidCard()
S0.printidCard()
S1.set_status('GOOD BOY')
S0.set_status('VERY GOOD')
S1.printidCard()
S0.printidCard()
