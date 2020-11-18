#header 

import random


def model_infected(in_person, contagion_prob, infection_len, semester_len, reinfect, k_many_infected, varied_inf_len):
    infected_people = {}
    infection_info = {}     # stores how many days into an infection someone is
    people_list = list(in_person.graph.items())

    if k_many_infected == 1:
        random_person = random.choice(people_list)     #check if this stores too much info
        infected_people[random_person[0]] = random_person[1]
        infection_info[random_person[0]] = 0    # initially, set the number of days they've been sick to 0
    else:   # otherwise we want to start with k many infected people
        list_of_infected_people = random.sample(people_list, k=k_many_infected)     # instead choose k-many infected people
        print(list_of_infected_people)
        for person in list_of_infected_people:
            infected_people[person[0]] = person[1]
            infection_info[person[0]] = 0


    recovered_list = set()     # stores the students who have recovered and therefore cannot be re-infected in the default
    # problem statement

    to_remove = set()   # stores the students who should be removed from the infected_people dictionary after they have
    # recovered (possibly redundant with recovered_list)

    time = 1
    infected_total = 1
    recovered_total = 0
    total_people = len(people_list)
    # Used to build graphs for infected, recovered
    infected_over_semester = [0] * semester_len 
    recovered_over_semester = [0]  * semester_len 
    susceptible_over_semester = [0] * semester_len

    day_dict = {1: "M", 2: "T", 3: "W", 4: "Th", 5: "F"}

    while time < semester_len:
        infected_to_add = {}
        weekday = day_dict[time % 7]
        for infected_person in infected_people:
            for course in infected_people[infected_person]:     # for all courses said infected person is in
                if weekday in course.days:
                    for person in course.students:
                        if reinfect == False:
                            if (person not in recovered_list) and (person.number not in infected_people) and (person not in infected_to_add):
                                prob = random.random()
                                if prob <= contagion_prob:
                                    infected_to_add[person] = in_person.graph[person.number]
                                    infection_info[person] = 0
                                    infected_total += 1
                        else:   # otherwise people can become reinfected having contracted the virus
                            if (person.number not in infected_people) and (person not in infected_to_add):
                                # reduce probability of infection if previously infected?
                                prob = random.random()
                                if prob <= contagion_prob:
                                    infected_to_add[person] = in_person.graph[person.number]
                                    infection_info[person] = 0
                                    infected_total += 1     # NOTE: if someone is reinfected, they are counted again in the infected total
            if varied_inf_len == False:
                if infection_info[infected_person] >= infection_len:
                    to_remove.add(infected_person)  # can't change the size of the dictionary while iterating through it
                    recovered_list.add(infected_person)
                    recovered_total += 1
            else:   # otherwise we want to vary the infection length, so we random choose when an infection ends
                # (to keep things simple)
                random_inf_len = random.randint(infection_len/5, infection_len)
                if infection_info[infected_person] >= random_inf_len:
                    to_remove.add(infected_person)
                    recovered_list.add(infected_person)
                    recovered_total += 1
            if weekday == "F":     # change each student's infection length as appropriate
                infection_info[infected_person] += 3
            else:
                infection_info[infected_person] += 1
        infected_people.update(infected_to_add)
        
        # Handle graph and plotting stuff here 
        infected_over_semester[time-1] = infected_total
        recovered_over_semester[time-1] = recovered_total
        susceptible_over_semester[time-1] = total_people - infected_total
        # change the time once per iteration of the while loop!
        if weekday == "F":
            if  time <= semester_len:
                infected_over_semester[time] = infected_total
                recovered_over_semester[time] = recovered_total
                susceptible_over_semester[time] = total_people - infected_total
            if time + 1 <= semester_len:
                infected_over_semester[time + 1] = infected_total
                recovered_over_semester[time + 1] = recovered_total
                susceptible_over_semester[time + 1] = total_people - infected_total
            time += 3
        else:
            time += 1

        for to_be_removed in to_remove:
            del infected_people[to_be_removed]  # remove no longer infected students from the infected_student
            # dictionary

        to_remove.clear()   # and remove all of those from the set to be removed as well!
        
    
    graph_data = [infected_over_semester, recovered_over_semester, susceptible_over_semester]
    return infected_total, graph_data
