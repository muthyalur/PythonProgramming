class Employee(object):
	"""docstring for Employee"""

	raiseAmount = 10
	num_of_emps = 0

	def __init__(self, first, last):
		self.first = first
		self.last = last
		# self.email = first + '.' + last + "@company.com"

		Employee.num_of_emps += 1

	@property
	def email(self):
		return '{}.{}@company.com'.format(self.first, self.last)

	@property	
	def fullName(self):
		return '{} {}'.format(self.first, self.last)

	@fullName.setter
	def fullName(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last
	
	@fullName.deleter
	def fullName(self):
		print('Delete Name!')
		self.first = None
		self.last = None

emp_1 = Employee('Corey', 'Schafer')

emp_1.first = 'Jim'

emp_1.fullName = 'Rajeev Muthyalu'

print(emp_1.first)
# print(emp_1.email())
print(emp_1.email)
# print(emp_1.fullName())
print(emp_1.fullName)


del emp_1.fullName


print(emp_1.first)
# print(emp_1.email())
print(emp_1.email)
# print(emp_1.fullName())
print(emp_1.fullName)