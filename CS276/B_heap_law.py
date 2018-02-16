import matplotlib.pyplot as plt

from Functions.functions import calcul_of_b, calcul_of_k, calcul_of_voc, list_plot, list_log


def statistics(collection_list):
    """ Calculation of heap law's coefficients k & b """

    # Merge vocabulary
    vocabulary = merge_vocabulary(collection_list)
    vocabulary2 = merge_vocabulary(collection_list[:len(collection_list) // 2])

    # Vocabulary and Token's number
    tok1 = token_nb(collection_list)
    voc1 = len(vocabulary)
    tok2 = token_nb(collection_list[:len(collection_list) // 2])
    voc2 = len(vocabulary2)
    print("Voici les réponses des résultats de la tâche 1 concernant la collection CS276 :\n".upper())
    print("Question 1\nNombre de token : " + str(tok1) + "\n")
    print("Question 2\nTaille du vocabulaire : " + str(voc1) + "\n")
    print("Question 3\nNous avons divisé la collection par deux.\n"
          "Nombre de token : " + str(tok2) +
          "\nTaille du vocabulaire : " + str(voc2))

    # Calculation of b and k
    b = calcul_of_b(voc1, voc2, tok1, tok2)
    k = calcul_of_k(voc1, tok1, b)
    print("Nous avons alors les coefficients b et k de la loi de Heap ci dessous :\n"
          "b = %.3f" % b)
    print("k = %.3f\n" % k)

    # Vocabulary size's calculation for a 1 million tokens' collection
    tok3 = 1000000
    voc3 = int(calcul_of_voc(tok3, k, b))
    print("Question 4\n"
          "Supposons le nombre de token a un million, nous trouvons une taille de vocabulaire de " + str(voc3) + "\n")

    # Plot
    list_to_plot = list_plot(vocabulary)
    list_log0 = list_log(list_to_plot[0])
    list_log1 = list_log(list_to_plot[1])
    plt.plot(list_to_plot[0], list_to_plot[1])
    plt.title('CS276 : frequence vs rang')
    plt.show()
    plt.plot(list_log0, list_log1)
    plt.title('CS276 : log(frequence) vs log(rang)')
    plt.show()

def merge_vocabulary(collection_list):
    """ Merges the vocabulary of a collections' list """
    res = {}
    for elt in collection_list :
        for term, occurence in elt.vocabulary.items() :
            if term not in res :
                res[term] = occurence
            else :
                res[term] += occurence
    return res

def token_nb(collection_list):
    """ Returns the tokens' number of a collections' list """
    token_number = 0
    for collection in collection_list :
        token_number += collection.tokens_number()
    return token_number
