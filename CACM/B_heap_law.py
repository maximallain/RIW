import pickle
import matplotlib.pyplot as plt

from CACM.models.collection_class import Collection
from CACM.tokenization import separate_doc, tokenization, lecture_doc
from Functions.functions import calcul_of_b, calcul_of_k, calcul_de_voc, list_plot, logList, create_collection_div_by_2
from CACM.models.collection_class import Collection

#create_collection_div_by_2()

def answer_question() :
    path_pickle = "../Data/CACM/collection_without_index.pickle"
    path_pickle_div2 = "../Data/CACM/collection_div_by_2.pickle"
    with open(path_pickle, 'rb') as f:
        collection = pickle.load(f)

    with open(path_pickle_div2, 'rb') as f:
        collection_div2 = pickle.load(f)
    tok1 = collection.tokens_number()
    voc1 = collection.vocabulary_size
    tok2 = collection_div2.tokens_number()
    voc2 = collection_div2.vocabulary_size


    print("Voici les réponses des résultats de la tâche 1 concernant la collection CACM :\n".upper())
    print("Question 1\nNombre de token : " + str(tok1)+"\n")
    print("Question 2\nTaille du vocabulaire : " + str(voc1)+"\n")
    print("Question 3\nNous avons divisé la collection par deux.\nNombre de token : " + str(tok2)+"\nTaille du vocabulaire : "+str(voc2))
    b = calcul_of_b(voc1,voc2,tok1,tok2)
    print("Nous avons alors les coefficients b et k de la loi de Heap ci dessous :\nb = " + str(b))
    k = calcul_of_k(voc1,tok1,b)
    print("k : " + str(k)+"\n")
    tok3 = 1000000
    voc3 = int(calcul_de_voc(tok3,k,b))
    print("Question 4\nSupposons le nombre de token a un million, nous trouvons une taille de vocabulaire de "+str(voc3))

    list_to_plot = list_plot(collection.vocabulary)

    print(list_to_plot[0])
    print(list_to_plot[1])
    list_log0 = logList(list_to_plot[0])
    list_log1 = logList(list_to_plot[1])
    plt.plot(list_to_plot[0], list_to_plot[1])
    plt.ylabel('CACM : frequence vs rang')
    plt.show()
    print(list_log0)
    print(list_log1)
    plt.plot(list_log0, list_log1)
    plt.ylabel('CACM : log(frequence) vs log(rang)')
    plt.show()