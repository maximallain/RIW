from pickle import load
import matplotlib.pyplot as plt


from CACM.C_boolean_model import boolean_search
from Functions.functions import list_termID_docID

with open('../Data/CACM/intermediate/collection_with_boolean_index', 'rb') as f:
    collection = load(f)
term1 = ''

def evaluation_main()

def recover_relevant_documents(term) :
    return len(boolean_search(term, collection))

def recover_document_list(term) :
    list = []
    #id_term = collection.id_term_method(term)
    for id_doc, doc in collection.docID_doc.items():
        if term in doc.vocabulary:
            list.append(id_doc)
    return list

def test():
    R = recover_relevant_documents(term1)
    A = collection.doc_number
    # Rappel's list
    R_list = []
    # Precision's list
    P_list = []
    p = 0
    i = 0
    #for doc in collection.doc_list :
    list_terms_doc = recover_document_list(term1)
    for doc in collection.doc_list :
        i += 1
        if doc.id in list_terms_doc :
            p += 1
        R_list.append(p/R)
        P_list.append(p/i)
    print(R_list)
    print(P_list)
    plt.plot(R_list, P_list)
    plt.title(' ')
    plt.show()



test()