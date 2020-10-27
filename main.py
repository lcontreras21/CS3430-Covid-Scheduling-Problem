import alg1
import preprocessing
from models import *

dict_classes = preprocessing.read_in_csv()
in_person_final = alg1.find_in_person(dict_classes, .1, 3, 7, 1)    # NOTE: base test input is .1, .3, 7, 1 on demo
