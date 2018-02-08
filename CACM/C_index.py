
def dict_term_id(list_voc) :
    """

    :param list_voc: list of tuples of vocabulary and its frequences
    :return: dictionary (key : id_term, value : term)
    """
    dict_res = {}
    id = 1
    for elt in list_voc :
        dict_res[id] = elt[0]
        id += 1
    return dict_res


def dict_doc_id(list_doc) :
    """

    :param list_doc: dictionary (key : id, value : list of the tokens of the doc
    :return: dictionary (key : id_doc, value : list of token of a doc)
    """
    dict_res = {}
    id = 1
    for key, value in list_doc.items():
        dict_res[id] = value
        id += 1
    return dict_res

def list_termID_docID(term_termID, doc_docID) :
    tuple_list = []
    for id_term, term in term_termID.items() :
        for id_doc, doc in doc_docID.items() :
            if term in doc :
                tuple_list.append((id_term,id_doc))
    return tuple_list


def reversed_index(list) :
    dict_res = {}
    for elt in list :
        if elt[0] not in dict_res :
            dict_res[elt[0]] = [elt[1]]
        else :
            dict_res[elt[0]].append(elt[1])
    return dict_res


