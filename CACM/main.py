from CACM.A_collection_treatment import collection_treatment
from CACM.B_heap_law import statistics
from CACM.C_boolean_search import boolean_main, boolean_search
from CACM.D_vectorial_search import vectorial_main

from pickle import dump, load
from time import time

#BOOLEAN INDEX

"""
answer = ''
while answer not in ['o','n'] :
    answer = input("Voulez-vous recréer l'index inversé ? (o/n)\n").lower()
    if answer == 'o' :
        print('Création de l\'index...')
        with open('../Data/CACM/collection_without_index.pickle', 'rb') as f:
            collection = load(f)
        time_index_1 = time()
        collection.create_reversed_index_boolean()
        time_index_2 = time()
        with open('../Data/CACM/collection_with_boolean_index', 'wb') as f:
            dump(collection, f)
        print('Index créé en %.2f secondes' % (time_index_2-time_index_1))
with open('../Data/CACM/collection_with_boolean_index', 'rb') as f:
    collection = load(f)

res1 = boolean_search("graph", collection)
print("Voici les {} documents dans lesquelles apparait le mot {} :\n".format(len(res1), "graph"))
for elt in res1 :
    print(collection.docID_doc[elt])

# VECTORIAL INDEX
answer = ''
while answer not in ['o','n'] :
    answer = input("\nVoulez-vous recréer l'index vectoriel inversé ? (o/n)\n").lower()
    if answer == 'o' :
        print('Création de l\'index...')
        with open('../Data/CACM/collection_without_index.pickle', 'rb') as f:
            collection = load(f)
        time_index_1 = time()
        collection.create_reversed_index_vectorial()
        time_index_2 = time()
        with open('../Data/CACM/collection_with_vectorial_index', 'wb') as f:
            dump(collection, f)
        print('Index créé en %.2f secondes' % (time_index_2-time_index_1))

with open('../Data/CACM/collection_with_vectorial_index', 'rb') as f:
    collection = load(f)
answer = ''
while answer not in [1,2,3] :
    answer = input("Quelle type de pondération souhaitez-vous tester ?\n1 - tf_idf\n"
                   "2 - tf_idf normalisé\n3 - fréquence normalisée\n")
    try :
        answer = int(answer)
    except ValueError :
        print("Veuillez entrer un chiffre entre 1 et 3.")
number = answer



res1 = vectorial_search("graph", collection, number)
print("Voici les {} documents dans lesquelles apparait le mot {} :\n".format(len(res1), "graph"))
for elt in res1 :
    print(collection.docID_doc[elt[0]])


#boolean_main(collection)
"""
"""
# TEST
print(collection.termID_term)
for doc in collection.doc_list :
    print(doc.id)
    print(doc.tokens)
print(collection.reversed_index)

print(boolean_search("computer", collection))
print(boolean_search("systems", collection))
print(boolean_search("program", collection))

print(boolean_search("programming", collection))
print(boolean_search("computer", collection))

print(b_or_search("computer","programming", collection))
print(b_and_search("computer","programming", collection))

print(boolean_search("computer", collection))
print(boolean_search("systems", collection))
print(boolean_search("program", collection))

print(b_not_search("program", collection))
print(spelling_out_request("computer+program+systems", collection))
"""

######## MAIN ########
"""
print("////////////////////////////////////")
print("/////// COLLECTION TREATMENT ///////")
print("////////////////////////////////////")
time1 = time()
collection_treatment()
time2 = time()
print("Collection's treatment execution : %.3f secondes\n" %(time2-time1))


print("////////////////////////////////////")
print("// TOKEN & VOCABULARY'S STATISTIC //")
print("////////////////////////////////////")
statistics()

print("////////////////////////////////////")
print("////////// BOOLEAN INDEX ///////////")
print("////////////////////////////////////")
boolean_main()
"""
print("////////////////////////////////////")
print("///////// VECTORIAL INDEX //////////")
print("////////////////////////////////////")
vectorial_main()

