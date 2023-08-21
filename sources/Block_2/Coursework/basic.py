class BasicWord:
    def __init__(self, word, anagrams):
        '''заполнение данных объекта'''
        self.anagrams = []
        self.word = ""
        self.word = word
        self.anagrams.extend(anagrams)

    def is_correct(self, user_word):
        '''возвращает корректность слова'''
        return user_word in self.anagrams

    def __repr__(self):
        '''возвращает представление объекта'''
        anagrams = ", ".join(self.anagrams)
        return f"Слово: {self.word}. Анаграммы: {anagrams}"

    def count_words(self):
        '''возвращает количество анаграм'''
        return len(self.anagrams)

    def is_empty(self):
        '''проверяет существует ли слово'''
        return not bool(self.word)
