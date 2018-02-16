import os
import matplotlib.pyplot as plt
from time import time
from pickle import dump, load

import nltk
import regex

from models.collection_class import Collection
from models.document_class import Document
from Functions.functions import calcul_of_b, calcul_of_k, calcul_de_voc, list_plot, logList


def collection_treatment() :
    i = 1
    time1_all = time()
    collection_list = []
    for num in range(0,10):
        print("Treating collection n°%i"%num)
        collection = Collection()
        print("Lecture")
        i = lecture(num, collection, i)
        print("Updating vocabulary")
        collection.vocabulary_update()
        print("Creating termID_term")
        collection.create_termID_term()
        print("Creating docID_doc")
        collection.create_docID_doc()
        print(collection.doc_list[:3])
        print(collection.tokens_number())
        collection_list.append(collection)
    time2_all = time()
    print("Time of the lecture : {}".format(time2_all-time1_all))
    with open('../Data/CS276/intermediate/collection_list', 'wb') as f:
        dump(collection_list, f)

def lecture(num_directory, collection, i):
    list_doc = []
    dir = "../Data/CS276/" + str(num_directory)
    print(dir)
    for e in os.listdir(dir):
        name_file = dir + "/" + e
        with open(name_file, "r") as fichier_lu:
            text_to_push = fichier_lu.read()
        document = Document()
        document.id = i
        document.add_text_in_doc(text_to_push)
        document.tokenization_CS()
        document.vocabulary_update()
        collection.add_doc(document)
        collection.add_tokens(document.tokens)
        i += 1
    return i



"""def merge_vocabulary(collection_list) :
    if len(collection_list) == 1 :
        return collection_list[0].vocabulary
    else :
        last_collection = collection_list[-1]
        last_vocabulary = last_collection.vocabulary
        other_vocabulary = merge_vocabulary(collection_list[:len(collection_list)-1])
        size = len(other_vocabulary)
        for term in last_vocabulary :
            if term in other_vocabulary :
                other_vocabulary[term] += 1
            else :
                other_vocabulary[term] = 1
            size = len(other_vocabulary)
        return other_vocabulary"""

def merge_vocabulary2(collection_list):
    res = {}
    for elt in collection_list :
        for term, occurence in elt.vocabulary.items() :
            if term not in res :
                res[term] = occurence
            else :
                res[term] += occurence
    return res



def token_nb(collection_list):
    token_number = 0
    for collection in collection_list :
        token_number += collection.tokens_number()
    return token_number





collection_treatment()

with open('../Data/CS276/intermediate/collection_list', 'rb') as f:
    collection_list = load(f)

# Merge vocabulary
vocabulary = merge_vocabulary2(collection_list)
vocabulary2 = merge_vocabulary2(collection_list[:len(collection_list)//2])

# Vocabulary and Token's number
tok1 = token_nb(collection_list)
voc1 = len(vocabulary)
tok2 = token_nb(collection_list[:len(collection_list)//2])
voc2 = len(vocabulary2)
print("Voici les réponses des résultats de la tâche 1 concernant la collection CACM :\n".upper())
print("Question 1\nNombre de token : " + str(tok1)+"\n")
print("Question 2\nTaille du vocabulaire : " + str(voc1)+"\n")
print("Question 3\nNous avons divisé la collection par deux.\n"
      "Nombre de token : " + str(tok2)+
      "\nTaille du vocabulaire : "+str(voc2))

# Calculation of b and k
b = calcul_of_b(voc1,voc2,tok1,tok2)
k = calcul_of_k(voc1,tok1,b)
print("Nous avons alors les coefficients b et k de la loi de Heap ci dessous :\n"
      "b = %.3f" %b)
print("k = %.3f\n" %k)

# Vocabulary size's calculation for a 1 million tokens' collection
tok3 = 1000000
voc3 = int(calcul_de_voc(tok3,k,b))
print("Question 4\n"
      "Supposons le nombre de token a un million, nous trouvons une taille de vocabulaire de "+str(voc3)+"\n")

# Plot
list_to_plot = list_plot(vocabulary)
list_log0 = logList(list_to_plot[0])
list_log1 = logList(list_to_plot[1])
plt.plot(list_to_plot[0], list_to_plot[1])
plt.title('CACM : frequence vs rang')
plt.show()
plt.plot(list_log0, list_log1)
plt.title('CACM : log(frequence) vs log(rang)')
plt.show()

