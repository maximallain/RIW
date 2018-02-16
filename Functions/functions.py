import operator
from math import log
import math

from nltk import word_tokenize


def list_plot(dict_voc):
    """ Returns a frequency's list and rank's list """
    sorted_list = sorted(dict_voc.items(), reverse=True, key=operator.itemgetter(1))
    list_res_frequency = []
    list_res_rank = []
    i = 1
    for e in sorted_list :
        list_res_frequency.append(e[1])
        list_res_rank.append(i)
        i = i + 1
    return (list_res_frequency, list_res_rank)

def list_log(list):
    """ Returns a log's list """
    res = []
    for e in list :
        res.append(log(e))
    return res

def calcul_of_b(m1,m2,t1,t2):
    """ Calculate the b of the Heap's Law """
    res = math.log(m2/m1)/math.log(t2/t1)
    return res

def calcul_of_k(m1,t1,b):
    """ Calculate the k of the Heap's Law """
    return (m1/math.pow(t1,b))

def calcul_of_voc(t,k,b):
    """ Calculates the vocabulary for a given tokens' number t """
    return  k*math.pow(t,b)

def get_stopwords_list():
    """ Returns the common words """
    with open("../Data/CACM/common_words", 'r') as file :
        stopwords_list = file.read()
    return stopwords_list.split()

def vocabulary(list_words):
    """ Create a dictionary (term : frequency)"""
    dict_res = {}
    for e in list_words:
        if e in dict_res:
            dict_res[e] = dict_res[e] + 1
        else:
            dict_res[e] = 1
    return dict_res


def sup_common_words(list) :
    with open("../Data/CACM/common_words","r") as fichier_lu :
        text = fichier_lu.read()
        list_common_words = word_tokenize(text)
        res = []
        for e in list :
            if not e in list_common_words :
                res.append(e)
        return(res)

