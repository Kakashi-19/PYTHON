# study of classes
# python object oriented programming
# instance variables

class student:
	def __init__(self, name, email, id):
		self.name = name
		self.email = email
		self.id = id

	def printidCard(self):
		print("Student Name: " + self.name)
		print("Student Email ID: " + self.email)
		print("Student ID: " + str(self.id))


num = int(input())
for i in range(1, num + 1):
	name = input()
	email = input()
	id = int(input())
	Student = student(name, email, id)
	student.printidCard(Student)
