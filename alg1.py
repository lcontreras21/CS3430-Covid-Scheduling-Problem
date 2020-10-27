#header 

import math
import models
import alg2


def find_in_person(dict_of_classes, contagion_prob, infection_len, semester_len, acceptable_threshold): 

    sorted_classes = sorted(dict_of_classes)
    margin = math.ceil(len(dict_of_classes)/2)
    in_person = models.graph()
    models.graph.add_to_graph(in_person, dict_of_classes, sorted_classes[0:margin])
    size = margin
    last_time = False
    
    while margin >= 1:
        infection_number = alg2.model_infected(in_person, contagion_prob, infection_len, semester_len)
        if last_time == True:
            break
        if margin == 1:
           last_time = not(False)
        else:
            margin = math.ceil(margin/2)
        if infection_number < acceptable_threshold:
            models.graph.add_to_graph(in_person, dict_of_classes, sorted_classes[size:size + margin])
            print("add half")
            size = size+margin
        elif infection_number > acceptable_threshold:
            models.graph.remove_from_graph(in_person, sorted_classes[size - margin:size])
            size = size-margin
            print("remove half")
        else: 
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

    return sorted_classes[0:size]


