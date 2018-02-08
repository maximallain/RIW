from Functions.functions import vocabulary, list_termID_docID, list_termID_docID_frequence


class Collection() :

    def __init__(self):
        self.doc_list = []
        self.doc_number = 0
        self.tokens_list = []
        self.vocabulary = None
        self.vocabulary_size = None
        self.termID_term = None
        self.docID_doc = None
        self.reversed_index = None


    def add_tokens(self, tokens_list):
        self.tokens_list.extend(tokens_list)

    def tokens_number(self):
        compteur = 0
        for doc in self.doc_list :
            compteur += doc.tokens_number()
        return compteur

    def add_doc(self,doc):
        self.doc_list.append(doc)
        self.doc_number += 1

    def vocabulary_update(self):
        self.vocabulary = vocabulary(self.tokens_list)
        self.vocabulary_size = len(self.vocabulary)

    def create_termID_term(self):
        dict_res = {}
        id = 1
        for elt in self.vocabulary.keys():
            dict_res[id] = elt
            id += 1
        self.termID_term = dict_res

    def create_docID_doc(self):
        dict_res = {}
        for doc in self.doc_list:
            dict_res[doc.id] = doc
        self.docID_doc = dict_res

    def list_docID_all(self):
        res = []
        for document in self.doc_list :
            res.append(document.id)
        return res

    def collection_frequence_term(self,term):
        for elt in self.vocabulary :
            if elt[0] == term :
                return elt[1]
        return 0

    def id_term_method(self, term_searched):
        for id, term in self.termID_term.items():
            if term == term_searched:
                return id
        return -1

    def create_reversed_index_boolean(self):
        list = list_termID_docID(self.termID_term, self.docID_doc)
        dict_res = {}
        for elt in list :
            if elt[0] not in dict_res :
                dict_res[elt[0]] = [elt[1]]
            else:
                dict_res[elt[0]].append(elt[1])
        self.reversed_index = dict_res

    def create_reversed_index_vectorial(self):
        list = list_termID_docID_frequence(self.termID_term, self.docID_doc)
        dict_res = {}
        for elt in list:
            if elt[0] not in dict_res:
                dict_res[elt[0]] = [(elt[1],elt[2])]
            else:
                dict_res[elt[0]].append((elt[1],elt[2]))
        self.reversed_index = dict_res

    def __repr__(self):
        return "Doc_list : {}\nTokens_list : {}\nTokens_number : {}\nVocabulary :{}\nVocabulary_size : {}".format(self.doc_list, self.tokens_list, self.tokens_number(), self.vocabulary, self.vocabulary_size)

