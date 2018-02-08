from CACM.A_collection_treatment import lecture_doc, separate_doc
from Functions.functions import calcul_of_b, calcul_of_k, calcul_de_voc, list_plot, logList
from CACM.models.collection_class import Collection

from pickle import dump, load
import matplotlib.pyplot as plt

def statistics() :
    """Calculation of heap law's coefficients k & b"""
    #create_collection_div_by_2()

    # Lecture of the two collections
    path_pickle = "../Data/CACM/intermediate/collection_without_index.pickle"
    path_pickle_div2 = "../Data/CACM/intermediate/collection_div_by_2.pickle"
    with open(path_pickle, 'rb') as f:
        collection = load(f)
    with open(path_pickle_div2, 'rb') as f:
        collection_div2 = load(f)

    # Vocabulary and Token's number
    tok1 = collection.tokens_number()
    voc1 = collection.vocabulary_size
    tok2 = collection_div2.tokens_number()
    voc2 = collection_div2.vocabulary_size

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
          "b = " + str(b))
    print("k : " + str(k)+"\n")

    # Vocabulary size's calculation for a 1 million tokens' collection
    tok3 = 1000000
    voc3 = int(calcul_de_voc(tok3,k,b))
    print("Question 4\n"
          "Supposons le nombre de token a un million, nous trouvons une taille de vocabulaire de "+str(voc3))

    # Plot
    list_to_plot = list_plot(collection.vocabulary)
    list_log0 = logList(list_to_plot[0])
    list_log1 = logList(list_to_plot[1])
    plt.plot(list_to_plot[0], list_to_plot[1])
    plt.title('CACM : frequence vs rang')
    plt.show()
    plt.plot(list_log0, list_log1)
    plt.title('CACM : log(frequence) vs log(rang)')
    plt.show()

def create_collection_div_by_2(path_r_div = "../Data/CACM/intermediate/cacm.div_by_2",
                               path_w_div="../Data/CACM/intermediate/useful_cacm.div_by_2",
                               path_pickle_div="../Data/CACM/intermediate/collection_div_by_2.pickle"
                               ):
    """Function which create and write in a pickle a collection divided by two"""
    text_res = []
    with open("../Data/CACM/cacm.all", "r") as file:
        temp = file.read()
        text_res.append(temp)
        text_res[0] = text_res[0][:len(text_res[0]) // 2]
    with open(path_r_div, 'w') as written:
        written.write(text_res[0])

    lecture_doc(path_r_div, path_w_div)
    collection_div2 = Collection()
    list_doc = separate_doc(path_w_div)
    for doc in list_doc:
        collection_div2.add_doc(doc)
        doc.tokenization()
        doc.vocabulary_update()
        collection_div2.add_tokens(doc.tokens)
    collection_div2.vocabulary_update()
    with open(path_pickle_div, 'wb') as f:
        dump(collection_div2, f)