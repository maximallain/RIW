import nltk
import regex

from Functions.functions import get_stopwords_list, sup_common_words, vocabulary


class Document() :

    def __init__(self):
        self.id = None
        self.title = ""
        self.tokens = None
        self.text = None
        self.vocabulary = {}
        self.collection = None

    def __repr__(self):
        return "Doc N°{} - {}".format(self.id, self.title)

    def tokens_number(self):
        """ Returns the tokens' number """
        return len(self.tokens)

    def add_text_in_doc(self, text):
        """ Adds text in the document """
        self.text = text
        self.title_doc()

    def tokenization_CACM(self):
        """ Tokenazises the text and stocks the tokens for CACM's collection """
        doc_tokens = nltk.word_tokenize(self.text)
        num_doc = doc_tokens.pop(1)
        self.id = int(num_doc)
        tokens_list = sup_common_words([elt.lower() for elt in doc_tokens])
        self.tokens = tokens_list


    def tokenization_CS(self):
        """ Tokenazises the text and stocks the tokens for CS's collection """
        stop_word_list = get_stopwords_list()
        stop_word_set = set(stop_word_list)
        useful_tokens = []
        tokens = self.text.split()
        for token in tokens:
            match = regex.match('[a-z]+', token)
            if match is not None and match.group() not in stop_word_set:
                useful_tokens.append(token)
        self.tokens = useful_tokens

    def vocabulary_update(self):
        """ Creates the vocabulary's dictionary from tokens """
        self.vocabulary = vocabulary(self.tokens)

    def title_doc(self):
        """ Adds the document's title """
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
        """ Find the highest frequency from vocabulary's terms """
        max = 0
        for term, frequency in self.vocabulary.items() :
            if frequency > max :
                max = frequency
        return max