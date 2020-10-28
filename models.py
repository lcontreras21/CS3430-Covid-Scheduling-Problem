'''
Models (objects) for Covid Spread
Changes as of 10/11/2020
	Implement Person object to house which classes they are in
'''

class person:
    def __init__(self, status, s):
        self.classes = []
        self.status = status 	# to distinguish teachers/students
        self.neighbors = []
        self.number = s
        #self.infection_length = 0

    def add_class(self, class_no):
        self.classes += [class_no]

    def __repr__(self):
        return self.number
        
    def __str__(self):
        return self.status + " " + self.number
		
class Course:
    def __init__(self, number):
        self.number = number
        self.students = []
        self.days = []
	
    def add_person(self, s):
        self.students += [s]
		
    def __lt__(self, other):
        return len(self.students) < len(other.students)
	
    def __str__(self):
        return str(self.students)

    def __repr__(self):
        return 'C'+self.number

class graph:
    # Things to note:
    #  - to create a new graph, give an empty dictionary along with the dictionary of classes to add
    #  - graph is a dictionary with person keys and dictionary values, where each person's dictionary
    # has a course number key which returns a tuple of the days it meets and the people in it
    def __init__(self):
        self.graph = {}

    def add_to_graph(self, dict_of_classes, list_to_add):
        for course in list_to_add:
            course = dict_of_classes[course]
            for person in course.students:  # assume professor in students list
                if person.number not in self.graph.keys():
                    self.graph[person.number] = [course]
                else:
                    self.graph[person.number].append(course)
    
    def remove_from_graph(self, courses_to_remove):
        for person in self.graph:
            for course in self.graph[person]:
                if course.number in courses_to_remove:  # to_remove is assumed to be a set of course numbers
                    self.graph[person].remove(course)
    
    def __str__(self):
        return str(self.graph.keys())
