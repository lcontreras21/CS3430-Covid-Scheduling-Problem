from models import *


def add_to_graph(to_add, graph):
    # Things to note:
    #  - to create a new graph, give an empty dictionary along with the dictionary of classes to add
    #  - graph is a dictionary with person keys and dictionary values, where each person's dictionary
    # has a course number key which returns a tuple of the days it meets and the people in it
    for course in to_add:
        course_number = course.number
        people = course.students
        days = course.days
        for person in course.students:  # assume professor in students list
            if graph[person] is None:
                graph[person] = {course_number: (days, people)}
            else:
                graph[person][course_number] = (days, people)
    return graph


def remove_from_graph(to_remove, graph):
    for person in graph:
        for course in graph[person]:
            if course.number in to_remove:  # to_remove is assumed to be a set of course numbers
                del graph[person][course.number]
    return graph
