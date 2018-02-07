
class Index() :

    def __init__(self, name):
        self.name = name
        self.collection = None
        self.index = None

    def create_reversed_index_booelean(self):
        list = list_termID_docID(self.collection.term_termID,self.doc_docID)
        dict_res = {}
        for elt in list:
            if elt[0] not in dict_res:
                dict_res[elt[0]] = [elt[1]]
            else:
                dict_res[elt[0]].append(elt[1])
        self.reversed_index = dict_res