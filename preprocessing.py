'''
Preprocessing for Covid Spread
Changes as of 10/11/2020
	Implement CSV reading and splitting into classes
'''
from models import *
import csv

schedule_file = "covid_example_files\demo_schedule_input.txt"	# Can be changed later

def read_in_csv():
	'''
	Information is listed as ['Course', 'Room', 'Teacher', 'Time', 'Students']
	'''
	#students, teachers = {}, {}
	classes = {}
	with open(schedule_file) as csv_file:
		file_reader = csv.reader(csv_file, delimiter="\t")
		for row in file_reader:
			if row[0] not in classes:
				classes[row[0]] = course(row[0])
			student_list = row[4].split(" ")
			for s in student_list:
				classes[row[0]].add_student(s)
			'''
			This chunk of code associates the course with each student
				Could add all students to the current student's list of neighbors
				Then at the end call 'set' on list of neighbors to get unique list and remove yourself to get neighbors
			if row[2] not in teachers:
				teachers[row[2]] = person("teacher")	
			teachers[row[2]].add_class(row[0])
			student_list = row[4].split(" ")
			for s in student_list:
				if s not in students:
					students[s] = person("student")
				students[s].add_class(row[0])
			'''
	return classes
			
			
if __name__ == "__main__":
	read_in_csv()