#header 

import math
import models
from alg2 import *
# from graph import plot


def find_in_person(dict_of_classes, num_students, contagion_prob, infection_len, semester_len, acceptable_threshold,
                   y_n_reinfect = False, how_many_infected = 1, y_n_varied_inf_len = False):

    sorted_classes = sorted(dict_of_classes)
    margin = math.ceil(len(dict_of_classes)/2)
    in_person = models.graph()
    in_person.add_to_graph(dict_of_classes, sorted_classes[0:margin])

    list_of_students = []
    for i in range(num_students):
        student_num = i + 1
        list_of_students.append("S" + str(student_num))

    # add students to parties (right now one party) and decide how many and their composition
    a_party = random.sample(list_of_students, k=7)

    # make parties courses that meet ~once~
    # models.Course()

    # add students to housing pods and make these courses that meet daily?
    pods = []
    for i in range(0, len(list_of_students), 5):    # arbitrarily, there are 5 students in a housing group
        # general idea from https://stackoverflow.com/a/312464
        pods.append(list_of_students[i:i+5])





    size = margin
    last_time = False
    counter = 0
    while margin >= 1:
        infection_number, graph_data = model_infected(in_person, contagion_prob, infection_len, semester_len,
                                                      y_n_reinfect, how_many_infected, y_n_varied_inf_len)
        margin = math.ceil(margin/2)
        if infection_number == acceptable_threshold:
            break
        elif infection_number < acceptable_threshold:
            in_person.add_to_graph(dict_of_classes, sorted_classes[size:size+margin])
            size = size + margin
            counter += 1
        else: 
            in_person.add_to_graph(dict_of_classes, sorted_classes[size-margin:size])
            size = size - margin
            counter += 1
        if margin == 1:
            break
    num_seats_in_person = 0
    for course in sorted_classes[0:size]:
        num_seats_in_person += len(dict_of_classes[course].students)
    # find the number of teacher 'seats' to remove
    num_teacher_seats = len(sorted_classes[0:size])
    # return the number of student seats
    print(f"In-person Student Seats: {num_seats_in_person - num_teacher_seats}")
    
    num_seats_total = 0
    for course in dict_of_classes:
        num_seats_total += len(dict_of_classes[course].students)
    num_teacher_seats = len(dict_of_classes)
    print(f"Best Case Student Seats Value: {num_seats_total - num_teacher_seats}")

    # Handle graphing here
    # plot(graph_data)

    print("In-person classes: ",sorted_classes[0:size])
    return sorted_classes[0:size]


