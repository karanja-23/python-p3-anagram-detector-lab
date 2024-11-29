# your code goes here!
class Anagram:
    
    def __init__(self, word):
        self.word =word
        
    def match(self, list):
        matched_words= []
        for list_item in list:
            if sorted(list_item) == sorted(self.word):
                matched_words.append(list_item)
        self.match= matched_words

        if len(self.match) >= 1:
            return self.match
        else:
            return[]
