class Employee(object):
	"""docstring for Employee"""

	raiseAmount = 10
	num_of_emps = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + "@company.com"

		Employee.num_of_emps += 1

	def fullName(self):
		return '{} {}'.format(self.first, self.last)

	def applyRaise(self):
		self.pay += int((self.pay * self.raiseAmount) / 100)

	@classmethod
	def setRaiseAmount(cls, amount):
		cls.raiseAmount = amount

	@classmethod
	def fromString(cls, empStr):
		first, last, pay = empStr.split('_')
		return cls(first, last, pay)

	@staticmethod
	def isWorkDay(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

	#Dunder Methods
	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

	def __str__(self):
		return '{} - {}'.format(self.fullName(), self.email)

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullName())

# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.comm'
# emp_1.pay = 50000
		
# emp_2.first = 'Rajeev'
# emp_2.last = 'Muthyalu'
# emp_2.email = 'rajeev.muthyalu@technicolor.comm'
# emp_2.pay = 118000


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Sachin', 'Tendulkar', 118000)


# print(emp_1)

print(emp_1.__str__())
print(emp_1.__repr__())
print(emp_1 + emp_2)
print(len(emp_1))

print(emp_1)
print(emp_2.email)
print(emp_1.fullName())
print(Employee.fullName(emp_2))

print(emp_2.pay)
emp_2.applyRaise();
print(emp_2.pay)

print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.num_of_emps)

Employee.setRaiseAmount(15)
emp_2.applyRaise();
print(emp_2.pay)

emp_3 = Employee.fromString('Gireesha_Bogineni_98000')
print(emp_3.email)
print(emp_3.pay)

import datetime

myDate = datetime.date(2017, 7, 26)
print(Employee.isWorkDay(myDate))


class Developer(Employee):
	raiseAmount = 44.068
	"""docstring for ClassName"""
	def __init__(self, first, last, pay, pgmlang):
		super(Developer, self).__init__(first, last, pay)
		self.pgmlang = pgmlang

	def __repr__(self):
		return super(Developer, self).__repr__()[:-1] + ", '{}')".format(self.pgmlang)
		

dev_1 = Developer('Gangaram', 'Sharma', 50000, 'java')
print(dev_1.email)
print(dev_1.pgmlang)

dev_2 = Developer('Raghu', 'Krishna', 118000, 'python')
print(dev_2.email)
print(dev_2.pgmlang)
dev_2.applyRaise()
print(dev_2.pay)

print(dev_1.__repr__())

# print(help(Developer))


class Manager(Employee):
	"""docstring for Manager"""
	def __init__(self, first, last, pay, employees = None):
		super(Manager, self).__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:	
			self.employees = employees

	def addEmployee(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)
			print('{} is added to {}\'s team'.format(emp.fullName(), self.fullName()))
		else:
			print('Duplicate Entry: {} is already added to {}\'s team'.format(emp.fullName(), self.fullName()))

	def removeEmployee(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
			print('{} removed from {}\'s team.'.format(emp.fullName(), self.fullName()))
		else:
			print('{} not found in Employees list reporting to {}.'.format(emp.fullName(), self.fullName()))

	def printEmployees(self):
		for emp in self.employees:
			print('-->', emp.fullName())

dev_3 = Developer('Ranjit', 'Sharma', 75000, 'python')
manager_1 = Manager('Suvidha', 'Guntumadugu', 170000, [dev_1, dev_2])
print(manager_1.email)
manager_1.printEmployees()
manager_1.addEmployee(dev_3)
manager_1.addEmployee(dev_2)
manager_1.printEmployees()
manager_1.removeEmployee(dev_2)
manager_1.printEmployees()
manager_1.removeEmployee(dev_2)

print(isinstance(manager_1, Manager))
print(isinstance(manager_1, Employee))
print(isinstance(manager_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))











