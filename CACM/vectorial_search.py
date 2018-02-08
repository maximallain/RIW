import operator
import pickle
from math import log

import time

from CACM.models.index_class import Index

path = "../Data/CACM/cacm.all"
#lecture_doc(path)
"""
with open('../Data/CACM/collection_without_index.pickle', 'rb') as f:
    collection = pickle.load(f)

#index_vectorial = Index("Reversed Index with Frequency")
collection.create_reversed_index_vectorial()

with open('../Data/CACM/collection_with_weight_index.pickle', 'wb') as f:
    pickle.dump(collection, f)
"""
with open('../Data/CACM/collection_with_weight_index.pickle', 'rb') as f:
    collection = pickle.load(f)

def vectorial_search(term, collection, number):
    N = collection.doc_number
    id_term = collection.id_term_method(term)
    if id_term == -1 :
        print("Le terme n'est pas dans la collection")
    dft = collection.vocabulary[term]
    list_tuple_docID_frequence = collection.reversed_index[id_term]
    dict_docID_weight = {}
    for elt in list_tuple_docID_frequence :
        tf_td = elt[1]
        max_frequency = collection.doc_docID[elt[0]].max_frequency()
        doc_len = collection.doc_docID[elt[0]].tokens_number()

        dict_docID_weight[elt[0]] = weight(N, tf_td, dft, doc_len, max_frequency, number)

        #dict_docID_weight[elt[0]] = tf_idf(N, tf_td, dft)

        #dict_docID_weight[elt[0]] = normalized_tf_idf(N, tf_td, dft, doc_len)

        #dict_docID_weight[elt[0]] = normalized_frequence(tf_td, max_frequency)
    sorted_list = sorted(dict_docID_weight.items(), reverse=True, key=operator.itemgetter(1))
    return sorted_list

def weight(N, tf_td, dft, doc_len, max_tf_in_doc, number):
    if number == 1 :
        return tf_idf(N, tf_td, dft)
    if number == 2 :
        return normalized_tf_idf(N, tf_td, dft, doc_len)
    else :
        return normalized_frequence(tf_td, max_tf_in_doc)


def tf_idf(N, tf_td, dft) :
    return (1 + log(tf_td,10))*(log((N/dft),10))

def normalized_tf_idf(N, tf_td, dft, doc_len) :
    return tf_idf(N, tf_td, dft)/doc_len

def normalized_frequence(tf_td, max_tf_in_doc) :
    return tf_td/max_tf_in_doc

"""def boolean_main(collection) :
    print("/// Bienvenue dans le meilleur moteur de recherche de la planète. ///")
    print("- - - - -\n/// Recherche d'un seul mot ///")
    term_searched = input("Entrez un mot :\n").lower()
    time1 = time.time()
    collection_doc = vectorial_search(term_searched, collection)
    time2 = time.time()
    print('Temps de la requête : {} seconde(s)'.format(time2-time1))
    if len(collection_doc)==0 :
        print("Il n'y a pas de documents correspondant à votre recherche.")
    else :
        print("Voici les {} documents dans lesquelles apparait le mot {} :\n".format(collection_doc.__len__(),term_searched))
        for docID in collection_doc :
            print(collection.doc_docID[docID[0]])
    print("\n- - - - -\n/// Requête bouléenne ///")
    request = input("Entrez une expression normale conjonctive sous le format ci-dessous.\nAND : * ; OR : + ; NOT : -\nExemple : 1*2+3*4+-5 qui signifie 1 AND (2 OR 3) AND (4 OR NOT(5))\n").lower()
    time1 = time.time()
    collection_doc = spelling_out_request(request, collection)
    time2 = time.time()
    print('Temps de la requête : {} seconde(s)'.format(time2-time1))
    if len(collection_doc)==0 :
        print("Il n'y a pas de documents correspondant à votre recherche.")
    else :
        print("Voici les {} documents dans lesquelles apparait le mot {} :\n".format(collection_doc.__len__(), term_searched))
        for docID in collection_doc :
            print(collection.doc_docID[docID])"""

#boolean_main(collection)
