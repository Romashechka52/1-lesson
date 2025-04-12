class WordLengthIterator:
    def __init__(self, word_list):
        self.word_list = word_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.word_list):
            word_length = len(self.word_list[self.index])
            self.index += 1
            return word_length
        else:
            raise StopIteration


words = ["Привіт", "світ", "Python", "ітератор", "довжина"]


iterator = WordLengthIterator(words)

for length in iterator:
    print(length)
