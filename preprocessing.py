'''
Preprocessing for Covid Spread
Changes as of 10/11/2020
	Implement CSV reading and splitting into classes
'''
from models import *
import csv

schedule_file = "covid_example_files/demo_schedule_input.txt"  # Can be changed later
constraint_file = "covid_example_files/demo_constraints.txt"


def read_in_constraints():
    '''
    Open a schedule constraints file and store the class name and list of class days in a dictionary
    '''
    constraint_dict = {}
    with open(constraint_file) as csv_file:
        file_reader = csv.reader(csv_file, delimiter="\t")
        csv_file.readline()  # Skip the column titles, in this case [Class Times, 60]
        for row in file_reader:
            # The class times are a long string with the days at the end of the string
            # Split up string by spaces, and select the last item to get days
            if row[0] == "Rooms":
                break
            days = row[1].split(" ")[-1]
            day_list = []
            example = ["M", "T", "W", "TH", "F"]
            for i, letter in enumerate(days):
                if letter == "-":
                    # add days between day_list[-1] to next letter
                    first_day = example.index(day_list[-1])
                    last_day = example.index(days[-1])
                    to_add = example[first_day + 1:last_day]
                    day_list += to_add
                elif letter == "H":
                    day_list[-1] = "TH"
                else:
                    day_list.append(letter)
            constraint_dict[row[0]] = day_list
    return constraint_dict


def read_in_csv():
    '''
    Information is listed as ['Course', 'Room', 'Teacher', 'Time', 'Students']
    '''
    # students, teachers = {}, {}
    constraints = read_in_constraints()  # Store the class days in a dictionary with key as course number and value the list of classes
    classes = {}
    students = []
    with open(schedule_file) as csv_file:
        file_reader = csv.reader(csv_file, delimiter="\t")
        csv_file.readline()  # Readline here to skip headers in csv file
        for row in file_reader:
            if row[0] not in classes:
                classes[row[0]] = Course(row[0])
            # Adding students to classes object
            student_list = row[4].split(" ")
            for s in student_list:
                ### Student handling is not done properly.
                new_person = person("student", "S" + s)
                if new_person not in students:
                    students.append(new_person)
                classes[row[0]].add_person(new_person)
            classes[row[0]].days = constraints[row[0]]  # assigning course dates to object field

        # Adding the professor
        new_person = person("Teacher", "T" + row[2])
        classes[row[0]].add_person(new_person)

    return classes, students

if __name__ == "__main__":
    # read_in_constraints()
    read_in_csv()
