import operator
from math import log
import os
import math
from nltk import word_tokenize

def lecture(num_directory):
    texts_res = []
    dir = "Data/CS276/" + str(num_directory)
    for e in os.listdir(dir):
        name_file = dir + "/" + e
        with open(name_file, "r") as fichier_lu:
            texte_entier = fichier_lu.read()
            texts_res.append(texte_entier)
    return texts_res

def sorted_list_vocabulary(list_words):
    #print("On traite la liste de tokens pour la transformer en vocabulaire...")
    dict_res = {}
    for e in list_words:
        if e in dict_res:
            dict_res[e] = dict_res[e] +  1
        else :
            dict_res[e] = 1
    list_triee = sorted(dict_res.items(), reverse=True, key=operator.itemgetter(1))
    return list_triee

def vocabulary(list_words):
    #print("On traite la liste de tokens pour la transformer en vocabulaire...")
    dict_res = {}
    for e in list_words:
        if e in dict_res:
            dict_res[e] = dict_res[e] +  1
        else :
            dict_res[e] = 1
    return dict_res


def majuscule_to_minuscule(list_words):
    #print("On transforme en minsucule...")
    res = []
    for e in list_words :
        res.append(str(e).lower())
    return res


def tokenization(file):
    with open(file, "r") as fichier_lu:
        texte = fichier_lu.read()
        list_res = word_tokenize(texte)
    return list_res

def nombre_token_text(text) :
    list = word_tokenize(text)
    return list

def sup_common_words(list) :
    #print("On supprime les common words...")
    with open("../Data/CACM/common_words","r") as fichier_lu :
        text = fichier_lu.read()
        list_common_words = word_tokenize(text)
        res = []
        for e in list :
            if not e in list_common_words :
                res.append(e)
        return(res)

def list_plot(dict_voc):
    sorted_list = sorted(dict_voc.items(), reverse=True, key=operator.itemgetter(1))
    list_res_frequence = []
    list_res_rang = []
    i = 1
    for e in sorted_list :
        list_res_frequence.append(e[1])
        list_res_rang.append(i)
        i = i + 1
    return (list_res_frequence, list_res_rang)

def logList(list):
    res = []
    for e in list :
        res.append(log(e))
    return res

def calcul_of_b(m1,m2,t1,t2):
    res = math.log(m2/m1)/math.log(t2/t1)
    return res

def calcul_of_k(m1,t1,b):
    return (m1/math.pow(t1,b))

def calcul_de_voc(t,k,b):
    return  k*math.pow(t,b)

def divide_a_file(file, name_file_created):
    with open(file, "r") as fichier_lu :
        with open(name_file_created, "w") as fichier_ecrit :
            text = fichier_lu.read()
            print(text.__len__())
            text2 = text[:text.__len__()//2]
            print(text2.__len__())
            fichier_ecrit.write(text2)

def list_termID_docID(termID_term, docID_doc) :
    tuple_list = []
    for id_term, term in termID_term.items() :
        for id_doc, doc in docID_doc.items() :
            if term in doc.tokens :
                tuple_list.append((id_term,id_doc))
    return tuple_list

def list_termID_docID_frequence(termID_term, docID_doc) :
    tuple_list = []
    for id_term, term in termID_term.items() :
        for id_doc, doc in docID_doc.items() :
            if term in doc.vocabulary :
                tuple_list.append((id_term,id_doc,doc.vocabulary[term]))
    return tuple_list

