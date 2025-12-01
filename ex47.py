class ParseError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

    def peek(word_list):
        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None


    def skip(word_list, word_type):
        while peek(word_list) == word_type:
            match(word_list, word_type)

    def parse_verb(word_list):
        skip(word_list, 'stop')

        if peek(word_list) == 'verb':
            return match(word_list, 'verb')
        else:
            raise ParseError("EXPECTED A VERB NEXT")
    def parse_object(word_list):
        skip(word_list, 'stop')
        next_word = peek(word_list)









