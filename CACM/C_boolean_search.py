from time import time
from pickle import dump, load

def boolean_main() :
    """Main function of the boolean model"""

    # Index's creation
    collection = index_creation()

    # One word request
    print("- - - - -\n"
          "/// Recherche d'un seul mot ///")
    term_searched = input("Entrez un mot :\n").lower()

    # Search
    time1 = time()
    collection_doc = boolean_search(term_searched, collection)
    time2 = time()
    print('Temps de la requête : %.3f seconde(s)' %(time2-time1))

    # Print the result
    if len(collection_doc)==0 :
        print("Il n'y a pas de document correspondant à votre recherche.")
    else :
        print("Voici les {} documents dans lesquelles apparait le mot {} :\n".format(len(collection_doc),term_searched))
        for docID in collection_doc :
            print(collection.docID_doc[docID])

    # Multiple words request
    print("\n- - - - -\n"
          "/// Requête bouléenne ///")
    request = input("Entrez une expression normale conjonctive sous le format ci-dessous.\n"
                    "AND : * ; OR : + ; NOT : -\n"
                    "Exemple : 1*2+3*4+-5 qui signifie 1 AND (2 OR 3) AND (4 OR NOT(5))\n").lower()

    # Search
    time1 = time()
    collection_doc = spelling_out_request(request, collection)
    time2 = time()
    print('Temps de la requête : %.3f seconde(s)' %(time2-time1))

    # Print the result
    if len(collection_doc)==0 :
        print("Il n'y a pas de documents correspondant à votre recherche.")
    else :
        print("Voici les {} documents dans lesquelles apparait le mot {} :\n".format(len(collection_doc), request))
        for docID in collection_doc :
            print(collection.docID_doc[docID])

def index_creation():
    """Creation of the collection's index"""
    print('Création de l\'index...')
    with open('../Data/CACM/intermediate/collection_without_index.pickle', 'rb') as f:
        collection = load(f)

    time_index_1 = time()
    collection.create_reversed_index_boolean()
    time_index_2 = time()

    with open('../Data/CACM/intermediate/collection_with_boolean_index', 'wb') as f:
        dump(collection, f)
    print('Index créé en %.2f secondes' % (time_index_2 - time_index_1))
    return collection

def spelling_out_request(request, collection):
    """Function which takes a FNC request and returns a list of document"""
    conjunction_list = request.split("*")
    first = True
    final_list = []
    for exp in conjunction_list :
        terms_list = exp.split("+")
        clause_res = []
        for term in terms_list :
            if term[0] == "-" :
                one_word_res = b_not_search(term[1:],collection)
            else :
                one_word_res = boolean_search(term, collection)
            clause_res = merge_sorted_list(clause_res,one_word_res)
        if first :
            final_list = clause_res
            first = False
        else :
            final_list = intersection_list(final_list, clause_res)
    return final_list

def boolean_search(term, collection):
    """Function which takes a term and returns the document's list whose contains this term"""
    id_term = collection.id_term_method(term)
    if id_term == -1 :
        return []
    list_doc = collection.reversed_index[id_term]
    return list_doc

def b_or_search(term1, term2, collection):
    """Function which takes two terms and returns the document's list whose contains one of this terms"""
    if isinstance(term1,str):
        list_doc_term1 = boolean_search(term1, collection)
    else :
        list_doc_term1 = term1
    if isinstance(term2,str) :
        list_doc_term2 = boolean_search(term2, collection)
    else :
        list_doc_term2 = term2
    return merge_sorted_list(list_doc_term1,list_doc_term2)

def b_and_search(term1, term2, collection) :
    """Function which takes two terms (or document's list) and returns the document's list whose contains the two terms"""
    if isinstance(term1,str):
        list_doc_term1 = boolean_search(term1, collection)
    else :
        list_doc_term1 = term1
    if isinstance(term2,str) :
        list_doc_term2 = boolean_search(term2, collection)
    else :
        list_doc_term2 = term2
    return intersection_list(list_doc_term1,list_doc_term2)

def b_not_search(term, collection) :
    """Function which takes a term and returns the document's list whose doesn't contain this term"""
    res = collection.list_docID_all()
    id_term = collection.id_term_method(term)
    if id_term == -1 :
        return res
    list_doc = collection.reversed_index[id_term]
    for e in list_doc :
        res.remove(e)
    return res

def merge_sorted_list(list1, list2):
    """Function which merges and sorts two document's lists"""
    res = []
    while (list1 != []) and (list2 != []):
        if int(list1[0]) < int(list2[0]):
            res.append(list1[0])
            list1 = list1[1:]
        elif list1[0] == list2[0]:
            res.append(list1[0])
            list1 = list1[1:]
            list2 = list2[1:]
        elif list1[0] > list2[0]:
            res.append(list2[0])
            list2 = list2[1:]
    res.extend(list1 + list2)
    return res

def intersection_list(list1, list2):
    """Function which intersects and sorts two document's lists"""
    res = []
    while (list1!=[]) and (list2!=[]):
        if list1[0]==list2[0] :
            res.append(list1[0])
            list1=list1[1:]
            list2=list2[1:]
        elif list1[0]<list2[0]:
            list1=list1[1:]
        else :
            list2=list2[1:]
    return res

"""answer = ''
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



# TESTS
print(len(boolean_search("computer", collection)))
print(len(boolean_search("systems", collection)))
print(len(boolean_search("program", collection)))
print(len(b_or_search("program", "systems", collection)))
print(len(b_and_search("computer", b_or_search("program", "systems", collection), collection)))
req1 = "systems*-computer"
req2 = "systems*program"
req3 = "systems*program+-computer"
res1 = b_not_search("computer", collection)
res2 = boolean_search("systems", collection)
res3 = boolean_search("program", collection)

print(res2)
print(res1)
print(res3)
collection_doc1 = spelling_out_request(req1, collection)
print("Voici les {} documents dans lesquelles apparait le mot {} :\n".format(collection_doc1.__len__(), req1))
for docID in collection_doc1:
    print(collection.docID_doc[docID])

collection_doc2 = spelling_out_request(req2, collection)
collection_doc2bis = b_or_search("systems","program",collection)
print("Voici les {} documents dans lesquelles apparait le mot {} :\n".format(collection_doc2.__len__(), req2))
for docID in collection_doc2:
    print(collection.docID_doc[docID])
collection_doc3 = spelling_out_request(req3, collection)
print("Voici les {} documents dans lesquelles apparait le mot {} :\n".format(collection_doc3.__len__(), req3))
for docID in collection_doc3:
    print(collection.docID_doc[docID])
collection_doc4 = merge_sorted_list(collection_doc1,collection_doc2)
print("Doit correspondre avec {}".format(len(collection_doc4)))
for docID in collection_doc4:
    print(collection.docID_doc[docID])"""