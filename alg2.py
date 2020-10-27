#header 

import random


def model_infected(in_person, contagion_prob, infection_len, semester_len):
    infected_people = {}
    infection_info = {}     # stores how many days into an infection someone is
    people_list = list(in_person.graph.items())
    random_person = random.choice(people_list)     #check if this stores too much info
    infected_people[random_person[0]] = random_person[1]
    infection_info[random_person[0]] = 0    # initially, set the number of days they've been sick to 0

    recovered_list = set()     # stores the students who have recovered and therefore cannot be re-infected in the default
    # problem statement

    to_remove = set()   # stores the students who should be removed from the infected_people dictionary after they have
    # recovered (possibly redundant with recovered_list)

    time = 1
    infected_total = 1

    day_dict = {1: "M", 2: "T", 3: "W", 4: "Th", 5: "F"}

    while time < semester_len:
        for infected_person in infected_people:
            weekday = day_dict[time % 7]
            for course in infected_people[infected_person].items():     # for all courses said infected person is in
                if time in course[1][0]:
                    for person in course.students:
                        if person not in recovered_list:
                            if person not in infected_people:
                                prob = random.random()
                                if prob <= contagion_prob:
                                    infected_people[person] = in_person.graph[person]
                                    infection_info[person] = 0
                                    infected_total += 1
            if infection_info[infected_person] >= infection_len:
                to_remove.add(infected_person)  # can't change the size of the dictionary while iterating through it
                recovered_list.add(infected_person)
            if weekday == "Friday":     # change each student's infection length as appropriate
                infection_info[infected_person] += 3
            else:
                infection_info[infected_person] += 1

        # change the time once per iteration of the while loop!
        if weekday == "Friday":
            time += 3
        else:
            time += 1

        for to_be_removed in to_remove:
            del infected_people[to_be_removed]  # remove no longer infected students from the infected_student
            # dictionary

        to_remove.clear()   # and remove all of those from the set to be removed as well!

    return infected_total


