import alg1
import preprocessing
from models import *
import sys
import time

dict_classes, students = preprocessing.read_in_csv()
#find_in_person takes dictionary schedule, contagion prob, infect len, sem len, acceptable thresh)
if "" in sys.argv or len(sys.argv) != 5:
    print("Arguments not satisfied.\nUsing default arguments of contagion_prob = 0.1, infection_len = 3, semester_len = 7, acceptable_thresh = 1.")
    in_person_final = alg1.find_in_person(dict_classes, students, 0.1, 3, 7, 3)
else:
    in_person_final = alg1.find_in_person(dict_classes, students, float(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
# NOTE: base test input is .1, 3, 7, 1 on demo
