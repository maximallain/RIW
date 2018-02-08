import operator
import pickle
from math import log, sqrt
from time import time

def main_vectorial(collection) :
    answer = ''
    while answer not in [1, 2, 3]:
        query = input("Entrez une requête sous la forme d'une suite de termes séparés par des espaces :\n")
        answer = input("Quelle type de pondération souhaitez-vous tester ?\n"
                       "1 - tf_idf\n"
                       "2 - tf_idf normalisé\n"
                       "3 - fréquence normalisée\n")
        try:
            answer = int(answer)
        except ValueError:
            print("Veuillez entrer un chiffre entre 1 et 3.")
    number = answer
    time1 = time()
    res = query_search(query = query, collection = collection, number = number)
    time2 = time()
    if len(res) == 0:
        print("Il n'y a pas de document correspondant à votre recherche.")
    else:
        print("Voici les 10 documents les plus pertinents pour la requête suivante '%s'\n (%d documents trouvés en %.3f seconde(s):\n" %(query,res.__len__(),(time2-time1)))
        i = 0
        for docID in res:
            if i == 9 :
                break
            print(collection.docID_doc[docID[0]])
            i +=1



def query_search(query, collection, number):
    terms_list = query.split(" ")
    dict_docID_weight = {"size": 0, "docID_weight": {}}
    for term in terms_list :
        doc_list = term_search(term, collection, number)
        add_list_in_dict(dict_docID_weight, doc_list)
    res = {}
    for doc, weight_list in dict_docID_weight["docID_weight"].items():
        res[doc] = cos(weight_list)
    return sorted(res.items(), reverse=True, key=operator.itemgetter(1))

def cos(list) :
    num = 0
    den = 0
    for elt in list :
        num += elt
        den += pow(elt,2)
    return num/(sqrt(den)*sqrt(len(list)))


def add_list_in_dict(dict, list2) :
    size = dict["size"] + 1
    dict["size"] = size
    for elt in list2 :
        if elt[0] not in dict["docID_weight"]:
            dict["docID_weight"][elt[0]] = []
            for i in range(0,size-1) :
                dict["docID_weight"][elt[0]].append(0)
        dict["docID_weight"][elt[0]].append(elt[1])
    for key, value in dict["docID_weight"].items() :
        if len(value) != size :
            dict["docID_weight"][key].append(0)


def term_search(term, collection, number):
    N = collection.doc_number
    id_term = collection.id_term_method(term)
    if id_term == -1 :
        print("Le terme n'est pas dans la collection")
    dft = collection.vocabulary[term]
    list_tuple_docID_frequence = collection.reversed_index[id_term]
    dict_docID_weight = {}
    for elt in list_tuple_docID_frequence :
        tf_td = elt[1]
        max_frequency = collection.docID_doc[elt[0]].max_frequency()
        doc_len = collection.docID_doc[elt[0]].tokens_number()
        dict_docID_weight[int(elt[0])] = weight(N, tf_td, dft, doc_len, max_frequency, number)
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



"""
path = "../Data/CACM/cacm.all"
#lecture_doc(path)

with open('../Data/CACM/collection_without_index.pickle', 'rb') as f:
    collection = pickle.load(f)

#index_vectorial = Index("Reversed Index with Frequency")
collection.create_reversed_index_vectorial()

with open('../Data/CACM/collection_with_weight_index.pickle', 'wb') as f:
    pickle.dump(collection, f)
"""
with open('../Data/CACM/collection_with_weight_index.pickle', 'rb') as f:
    collection = pickle.load(f)

main_vectorial(collection)

""" TEST A SUPPRIMER
query = "algorithm computer time"
number = 1
dict_to_print = query_search(query,collection,number)
print(dict_to_print)
#TEST ADD LIST IN DICT
list = [(1,0.5798),(2,0.5646), (3,0.829)]
dict = {"size" : 3, "docID_weight" : {1 : [0,0.5,0.6], 2 : [0.2,0.4,0.8]}}
add_list_in_dict(dict, list)
print(dict)
"""
