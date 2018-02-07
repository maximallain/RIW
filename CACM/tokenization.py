from nltk import word_tokenize
import re
import operator
from CACM.models.document_class import *



def lecture_doc(path_r, path_w):
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



