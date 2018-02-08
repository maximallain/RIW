from CACM.boolean_search import boolean_main, boolean_search
from CACM.vectorial_search import vectorial_search

from pickle import dump, load
from time import time

#BOOLEAN INDEX

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
    print(collection.doc_docID[elt])

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
    print(collection.doc_docID[elt[0]])


#boolean_main(collection)

"""
# TEST
print(collection.term_termID)
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

