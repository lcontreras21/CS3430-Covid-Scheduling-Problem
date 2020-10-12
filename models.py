'''
Models (objects) for Covid Spread
Changes as of 10/11/2020
	Implement Person object to house which classes they are in
'''

class person:
	def __init__(self, status):
		self.classes = []
		self.status = status 	# to distinguish teachers/students
		self.neighbors = []
		
	def add_class(self, class_no):
		self.classes += [class_no]
		
	def __str__(self):
		return self.status
		
class course:
	def __init__(self, number):
		self.number = number
		self.students = []
	
	def add_student(self, s):
		self.students += [s]
		
	def __lt__(self, other):
		return len(self.students) < len(other.students)
	
	def __str__(self):
		return str(self.students)