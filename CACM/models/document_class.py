from nltk import word_tokenize

from Functions.functions import sup_common_words, vocabulary


class Document() :

    def __init__(self):
        self.id = None
        self.title = ""
        self.tokens = None
        self.text = None
        self.vocabulary = {}
        self.collection = None


    def tokens_number(self):
        return len(self.tokens)

    def __repr__(self):
        return "Doc N°{} - {}".format(self.id, self.title)

    def add_text_in_doc(self, text):
        self.text = text
        self.title_doc()

    def tokenization(self):
        # Tokenazise le text
        doc_tokens = word_tokenize(self.text)
        num_doc = doc_tokens.pop(1)
        self.id = int(num_doc)
        tokens_list = sup_common_words([elt.lower() for elt in doc_tokens])
        self.tokens = tokens_list

    def vocabulary_update(self):
        self.vocabulary = vocabulary(self.tokens)

    def title_doc(self):
        doc_lines = self.text.split("\n")
        bool = False
        for line in doc_lines:
            if ".W" in line:
                break
            if bool == True:
                line += " "
                self.title += line
            if ".T" in line:
                bool = True

    def max_frequency(self):
        max = 0
        for term, frequency in self.vocabulary.items() :
            if frequency > max :
                max = frequency
        return max