import re
import wikipedia


class Article:
    def __init__(self, lang="sq"):
        wikipedia.set_lang(lang)
        title = wikipedia.random()
        print(title)
        self.content = wikipedia.summary(title)


    def remove_nonchar(self):
        self.content = re.sub(r'[^A-Za-z0-9 ëËçÇ]+', '', self.content)
    
    def list_words(self) -> list:
        return self.content.split(" ")

    def list_chars(self) -> list:
        self.content.replace(" ", " ")
        return list(self.content)
    
    def lower_case(self):
        self.content = self.content.lower()