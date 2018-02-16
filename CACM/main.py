from CACM.A_collection_treatment import collection_treatment
from CACM.B_heap_law import statistics
from CACM.C_boolean_model import boolean_main
from CACM.D_vectorial_model import vectorial_main

from pickle import dump, load
from time import time

######## MAIN ########
print("////////////////////////////////////")
print("/////////////  CACM  ///////////////")
print("////////////////////////////////////\n")

print("////////////////////////////////////")
print("/////// COLLECTION TREATMENT ///////")
print("////////////////////////////////////\n")
time1 = time()
collection_treatment()
time2 = time()
print("Collection's treatment execution : %.3f secondes\n" %(time2-time1))


print("////////////////////////////////////")
print("// TOKEN & VOCABULARY'S STATISTIC //")
print("////////////////////////////////////\n")
statistics()

print("////////////////////////////////////")
print("////////// BOOLEAN INDEX ///////////")
print("////////////////////////////////////\n")
boolean_main()

print("\n")
print("////////////////////////////////////")
print("///////// VECTORIAL INDEX //////////")
print("////////////////////////////////////\n")
vectorial_main()


