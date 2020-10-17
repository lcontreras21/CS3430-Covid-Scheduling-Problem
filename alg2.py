#header 

import random

def model_infected(in_person, contagion_prob, infection_len, semester_len):
    infected_people = {}
    people_list = list(in_person.items())
    random_person = random.choice(people_list) #check if this stores too much info 
    infected_people.add(random_person) 
    
    time = 1
    infected_total = 1

    while time < semester_length:
        for person in infected_people:
            weekday = "Monday" #fix this (with modular division) 
            for course in infected_people[person.number]:
                if time in course.day:
                    for person in course.students:
                        if person not in infected_people:
                            prob = random.random()
                            if prob <= contagion_prob:
                                infected_people.add(person)
                                infected_total += 1
                        if person.infection_length >= infection_len:
                            infected_people.remove(person)
                        if weekday != "Friday":
                            person.infection_length += 3
                        else: 
                            person.infection_length += 1
                time += 1
        return infected_total 


