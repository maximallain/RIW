from time import time
import os

from models.collection_class import Collection
from models.document_class import Document


def collection_treatment():
    """ Treatment of the collection CS276 """

    # Initialization
    i = 1
    time1_all = time()
    collection_list = []

    # Treatment of each collection
    for num in range(0,10):
        print("Treating collection n°%i"%num)
        collection = Collection()

        print("Lecture")
        i = reading(num, collection, i)

        print("Updating vocabulary")
        collection.vocabulary_update()

        print("Creating termID_term")
        collection.create_termID_term()

        print("Creating docID_doc")
        collection.create_docID_doc()
        collection_list.append(collection)

    time2_all = time()
    print("Time of the lecture : {}".format(time2_all-time1_all))

    return collection_list


def reading(num_directory, collection, i):
    """ Reading of a collection, creation of documents, association between documents and collection """

    dir = "../Data/CS276/" + str(num_directory)
    for e in os.listdir(dir):
        name_file = dir + "/" + e
        with open(name_file, "r") as fichier_lu:
            text_to_push = fichier_lu.read()

        # Document's creation
        document = Document()
        document.id = i
        document.add_text_in_doc(text_to_push)
        document.tokenization_CS()
        document.vocabulary_update()

        # Collection and document's association
        collection.add_doc(document)
        collection.add_tokens(document.tokens)
        i += 1
    return i