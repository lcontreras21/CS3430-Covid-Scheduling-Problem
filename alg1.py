#header 

import math
import models
from alg2 import *
from graph import plot


def find_in_person(dict_of_classes, contagion_prob, infection_len, semester_len, acceptable_threshold): 

    sorted_classes = sorted(dict_of_classes)
    margin = math.ceil(len(dict_of_classes)/2)
    in_person = models.graph()
    in_person.add_to_graph(dict_of_classes, sorted_classes[0:margin])
    size = margin
    last_time = False
    counter = 0
    while margin >= 1:
        infection_number, graph_data = model_infected(in_person, contagion_prob, infection_len, semester_len)
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


