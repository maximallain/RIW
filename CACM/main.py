from CACM.boolean_search import *
import pickle

answer = ''
while answer not in ['o','n'] :
    answer = input("Voulez-vous recréer l'index inversé ? (o/n)").lower()
    if answer == 'o' :
        print('Création de l\'index...')
        with open('../Data/CACM/collection_without_index.pickle', 'rb') as f:
            collection = pickle.load(f)
        time_index_1 = time()
        collection.create_reversed_index_boolean()
        time_index_2 = time()
        with open('../Data/CACM/collection_with_boolean_index', 'wb') as f:
            pickle.dump(collection, f)
        print('Index créé en %.2f secondes' % (time_index_2-time_index_1))



with open('../Data/CACM/collection_with_boolean_index', 'rb') as f:
    collection = pickle.load(f)



boolean_main(collection)


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

