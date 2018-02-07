from CACM.models.collection_class import Collection
from CACM.tokenization import separate_doc
import pickle

path = "../Data/CACM/cacm.all"
#lecture_doc(path)
collection = Collection()
list_doc = separate_doc("../Data/CACM/useful_cacm.txt")
for doc in list_doc :
    collection.add_doc(doc)
    doc.tokenization()
    doc.vocabulary_update()
    collection.add_tokens(doc.tokens)

collection.vocabulary_update()
collection.create_term_termID()
collection.create_doc_docID()

# Serialization of the treated collection without index
with open('../Data/CACM/collection_without_index.pickle', 'wb') as f:
    pickle.dump(collection, f)

#BOOLEAN
#collection.create_reversed_index_boolean()


