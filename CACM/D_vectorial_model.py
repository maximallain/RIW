import operator
from pickle import dump, load
from math import log, sqrt
from time import time

path_wo_index = '../Data/CACM/intermediate/collection_without_index.pickle'

def vectorial_main() :
    """Main function of the vectorial model"""

    # Index's creation
    collection = index_creation()

    # Request
    query = input("Entrez une requête sous la forme d'une suite de termes séparés par des espaces :\n")

    # Weighting choice
    answer = ''
    while answer not in [1, 2, 3]:
        answer = input("Quelle type de pondération souhaitez-vous tester ?\n"
                       "1 - tf_idf\n"
                       "2 - tf_idf normalisé\n"
                       "3 - fréquence normalisée\n")
        try:
            answer = int(answer)
        except ValueError:
            print("Veuillez entrer un chiffre entre 1 et 3.")
    number = answer

    # Search
    time1 = time()
    res = query_search(query = query, collection = collection, number = number)
    time2 = time()

    # Print the result
    if len(res) == 0:
        print("Il n'y a pas de document correspondant à votre recherche.\nTemps de la requête : %.3f seconde(s)" % (time2-time1))
    else:
        print("Voici les 10 documents les plus pertinents pour la requête suivante '%s'\n"
              "%d documents trouvés en %.3f seconde(s):\n" %(query,res.__len__(),(time2-time1)))
        i = 0
        for docID in res:
            if i == 9 :
                break
            print(collection.docID_doc[docID[0]])
            i +=1


def index_creation():
    """Creation of the collection's index"""

    print('Création de l\'index...')

    # Collection's lecture
    with open(path_wo_index, 'rb') as f:
        collection = load(f)

    time_index_1 = time()
    collection.create_reversed_index_vectorial()
    time_index_2 = time()

    print('Index créé en %.2f secondes' % (time_index_2 - time_index_1))

    return collection


def query_search(query, collection, number):
    """Function which takes a request and returns a sorted documents' list"""
    terms_list = query.split(" ")
    dict_docID_weight = {"size": 0, "docID_weight": {}}
    for term in terms_list :
        doc_list = term_search(term, collection, number)
        add_list_in_dict(dict_docID_weight, doc_list)
    res = {}
    for doc, weight_list in dict_docID_weight["docID_weight"].items():
        res[doc] = cos(weight_list)
    return sorted(res.items(), reverse=True, key=operator.itemgetter(1))

def cos(list):
    """Function which defines the similarity of request in a document"""
    num = 0
    den = 0
    for elt in list :
        num += elt
        den += pow(elt,2)
    return num/(sqrt(den)*sqrt(len(list)))


def add_list_in_dict(dict, list2):
    """Function which adds a list of tuple (document, term's weight in this document) of a term to the main dictionnary"""
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
    """Function which return a list of documents which contain the term. The list is sorted by weight"""
    N = collection.doc_number
    id_term = collection.id_term_method(term)
    if id_term == -1 :
        print("Le terme %s n'est pas dans la collection" % term)
        return []
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
    """Function which return the chosen weight's function"""
    if number == 1 :
        return tf_idf(N, tf_td, dft)
    if number == 2 :
        return normalized_tf_idf(N, tf_td, dft, doc_len)
    else :
        return normalized_frequence(tf_td, max_tf_in_doc)


def tf_idf(N, tf_td, dft) :
    """Function tf_idf"""
    return (1 + log(tf_td,10))*(log((N/dft),10))

def normalized_tf_idf(N, tf_td, dft, doc_len) :
    """Function tf_idf normalized"""
    return tf_idf(N, tf_td, dft)/doc_len

def normalized_frequence(tf_td, max_tf_in_doc) :
    """Function frequence normalized"""
    return tf_td/max_tf_in_doc