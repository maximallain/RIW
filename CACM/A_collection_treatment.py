from CACM.models.collection_class import Collection
from CACM.models.document_class import Document
import pickle

def collection_treatment(path = "../Data/CACM/cacm.all") :
    """Create a collection object which is composed by a document's list"""
    intermediate_path = "../Data/CACM/intermediate/useful_cacm.txt"

    # We keep only the useful parts of the collection
    lecture_doc(path, intermediate_path)

    # We separate the documents and we stock them in a list
    list_doc = separate_doc(intermediate_path)

    # Once separated, we create the document objects, then we add them to the collection
    collection = Collection()
    for doc in list_doc :
        collection.add_doc(doc)
        doc.tokenization()
        doc.vocabulary_update()
        collection.add_tokens(doc.tokens)

    # We create the vocabulary from the tokens' list
    collection.vocabulary_update()

    # We create the dictionary {termID : term}
    collection.create_termID_term()

    # We create the dictionary {docID : document}
    collection.create_docID_doc()

    # Serialization of the treated collection without index
    with open('../Data/CACM/intermediate/collection_without_index.pickle', 'wb') as f:
        pickle.dump(collection, f)

def lecture_doc(path_r, path_w):
    """Function which keep only the useful parts of a document's collection"""
    useful_text=[]
    n=0
    with open(path_r,"r") as text:
        for line in text :
            if line[:2] in [".I",".T",".W",".K"] :
                n=1
                useful_text+=line
            elif line[:2] in [".B",".A",".N",".X"] :
                n=0
            else :
                if n==1:
                    useful_text+=[line]
    with open(path_w, 'w') as new_file:
        for item in useful_text:
            new_file.write(item)

def separate_doc(path):
    """Function which separates documents from a collection"""
    with open(path, "r") as text:
        list_doc = []
        text_to_push = ""
        for line in text:
            if line[:2] == ".I" and text_to_push != "" :
                document = Document()
                document.add_text_in_doc(text_to_push)
                list_doc.append(document)
                text_to_push = line
            else :
                text_to_push += line
        document = Document()
        document.add_text_in_doc(text_to_push)
        list_doc.append(document)
    return list_doc


