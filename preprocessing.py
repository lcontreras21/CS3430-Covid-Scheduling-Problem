'''
Preprocessing for Covid Spread
Changes as of 10/11/2020
	Implement CSV reading and splitting into classes
'''
from models import *
import csv

schedule_file = "covid_example_files/demo_schedule_input.txt"	# Can be changed later

def read_in_csv():
    '''
    Information is listed as ['Course', 'Room', 'Teacher', 'Time', 'Students']
    '''
    #students, teachers = {}, {}
    classes = {}
    our_graph = graph()
    with open(schedule_file) as csv_file:
        file_reader = csv.reader(csv_file, delimiter="\t")
        csv_file.readline()                 # Readline here to skip headers in csv file
        for row in file_reader:
                if row[0] not in classes:
                        classes[row[0]] = Course(row[0])
                student_list = row[4].split(" ")
                for s in student_list:
                        new_student = person("student", s)
                        classes[row[0]].add_student(new_student)
                classes[row[0]].day.append("Monday")              # Set placeholder day. Need to read in constraints file to figure out day of week

    return classes
    #our_graph.add_to_graph(classes)
    #return our_graph

			
			
if __name__ == "__main__":
    final_graph = read_in_csv()
    print(final_graph.graph["1"])
