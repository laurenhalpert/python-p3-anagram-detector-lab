class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, list_of_words):
        separated_word = list(self.word)
        match = []
        for elem in list_of_words:
            separated_elem = list(elem)
            
            if sorted(separated_elem) == sorted(separated_word):
                match.append(elem)
        return match
            