#header 

import math
import alg2

def find_in_person(dict_of_classes, contagion_prob, infection_len, semester_len, acceptable_threshold): 

    sorted_classes = dict(sorted(dict_of_classes))
    margin = math.ceil(len(dict_of_classes)/2)
    in_person = graph()
    graph.add_to_graph(in_person, sorted_classes[0:margin])
    size = margin
    
    while margin >= 1:
        infection_number = alg2.model_infected(in_person, contagion_prob, infection_len, semester_len)
        margin = math.ceil(margin/2)
        if infection_number < acceptable_threshold:
            graph.add_to_graph(in_person, sorted_classes[size:size+margin])
            size = size+margin
        elif infection_number > acceptable_threshold:
            graph.remove_from_graph(in_person, sorted_classes[size-margin:size])
            size = size-margin
        else: 
            break
    
    num_seats_in_person = 0
    for course in sorted_classes[0:size]:
        num_seats_in_person += len(course.students)
    print(f"In person student seats: {num_seats_in_person}")
    
    num_seats_total = 0
    for course in dict_of_classes:
        num_seats_total += len(course.students)
    print(f"Total possible student seats: {num_seats_total}")

    return sorted_classes[0:size]


