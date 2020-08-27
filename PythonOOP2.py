# study of classes
# python object oriented programming
#class variables


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
		print("Student Status: " + self.Exam_status, end='\n\n')  # calling the exam_status variable by self(instance) so that it can be changed individually.


Student0 = student('vaibhav', 'vps@gamil.com', 217312)
Student1 = student('arnav', 'sps@gamil.com', 100000)
Student0.printidCard()
Student1.printidCard()
Student1.Exam_status = 'SUPER'  # changing Exam status for Student1 instance
Student0.printidCard()
Student1.printidCard()
