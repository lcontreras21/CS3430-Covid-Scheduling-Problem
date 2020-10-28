import alg1
import preprocessing
from models import *

dict_classes = preprocessing.read_in_csv()
#find_in_person takes dictionary schedule, contagion prob, infect len, sem len, acceptable thresh)
in_person_final = alg1.find_in_person(dict_classes, 1, 3, 14, 15) 
# NOTE: base test input is .1, .3, 7, 1 on demo
