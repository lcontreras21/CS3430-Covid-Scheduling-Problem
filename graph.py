'''
Handle graphing for infected, recovered over the course of the semester.
Note: Susceptible does not include people that are remote. 
    For example, in a very basic example with 8 classes, the first 6 could be considered remote. 
    Teacher 4 can be teaching the last two classes, but since they are remote, she won't appear in the
    count for susceptability. 
'''

import matplotlib.pyplot as plt

def plot(graph_data):
    infected_over_time = graph_data[0]
    recovered_over_time = graph_data[1]
    susceptible_over_time = graph_data[2]
    time = list(range(1, len(infected_over_time)+1))

    fig, ax = plt.subplots()
    ax.plot(time, infected_over_time, label="infected", color="r")
    ax.plot(time, recovered_over_time, label="recovered", color="g")
    ax.plot(time, susceptible_over_time, label="susceptible", color="b")

    ax.legend()
    ax.set_title("Susceptible/Infected/Recovered Over Time")
    ax.set_ylabel("Total (people)")
    ax.set_xlabel("Time (days)")
    plt.show()
