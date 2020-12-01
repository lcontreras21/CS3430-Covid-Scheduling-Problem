#header 

import math
from models import Course, graph
from alg2 import *
from graph import plot


def find_in_person(dict_of_classes, list_of_students, contagion_prob, infection_len, semester_len, acceptable_threshold,
                   y_n_reinfect = False, how_many_infected = 1, y_n_varied_inf_len = False, y_n_party = False,
                   y_n_pods = False):

    sorted_classes = sorted(dict_of_classes)
    #print(type(sorted_classes))
    margin = math.ceil(len(dict_of_classes)/2)
    in_person = graph()
    in_person.add_to_graph(dict_of_classes, sorted_classes[0:margin])

    if y_n_party:   # if we're considering the parties extension
        # add students to parties (right now one party) and decide how many and their composition
        a_party = random.sample(list_of_students, k=int(len(list_of_students)*.15))      # add a reason for percentage of population?


        # make parties courses that meet ~once~
        party_course = Course(1000000)     # we assume there are less than 1m courses
        party_course.set_people(a_party)
        party_course.days = ['F']

        # add party course to graph
        in_person.add_special_course(party_course)   # verify party has been added!


    if y_n_pods:    # if we're considering the pods extension
        # add students to housing pods and make these courses that meet daily?
        pods = []
        for i in range(0, len(list_of_students), 5):    # arbitrarily, there are 5 students in a housing group
            # general idea from https://stackoverflow.com/a/312464
            pods.append(list_of_students[i:i+5])

        for i in range(0, len(pods)):
            pod_course = Course(1000000 + i + 1)
            pod_course.set_people(pods[i])
            pod_course.days = ['M', 'T', 'W', 'TH', 'F', 'S', 'SU']
            in_person.add_special_course(pod_course)






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
    plot(graph_data)

    print("In-person classes: ",sorted_classes[0:size])
    return sorted_classes[0:size]


