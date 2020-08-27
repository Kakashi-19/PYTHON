import random


class Person:
    increm = 1.05

    def __init__(self, name, age, position):
        self.name = name.title()
        self.age = age
        self.position = position.title()

    def printID(self):
        print('Name: ' + self.name)
        print('Position: ' + self.position)
        print('Age: ' + str(self.age))
        print('Email: ' + '{}{}@gmail.com'.format(self.name, self.age), end='\n')
        if self.position == 'Teacher':
            print('Salary: ' + str(self.salary), end='\n\n')

    @classmethod
    def from_string(cls, string):
        data = string.split()
        name, age, position = data
        return cls(name, age, position)

    @staticmethod
    def fortune():
        print('Fortune: ' + random.choice(['Good day', 'Great day', 'Awesome day']))


class Employee(Person):

    def __init__(self, name, age, position, salary):
        super().__init__(name, age, position)
        self.salary = salary

    # def printID(self):                                     #no need to form new function as it inherits methods from the parent class
    #     print('Name: ' + self.name)
    #     print('Position: ' + self.position)
    #     print('Age: ' + str(self.age))
    #     print('Email: ' + '{}{}@gmail.com'.format(self.name, self.age))
    #     print('Salary: ' + str(self.salary), end='\n\n')

    def raised_salary(self):
        self.salary = int(self.salary * self.increm)


prs1 = Person.from_string('Arnav 22 student')
# prs1.printID()

prs2 = Employee('Vaibhav', 20, 'Teacher', 100000)
prs2.printID()
prs2.increm = 1.10
prs2.raised_salary()
prs2.printID()
'''
learn how to present a class as a dictionary
objects are hashable
to represent or convert into dictionary
us object or instance.__dict__ like prs1.__dict__
now u can use the obejt as a dictionary
and object attributes and their values as key value pairs of the dictionary
'''
