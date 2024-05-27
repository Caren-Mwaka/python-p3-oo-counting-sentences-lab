#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value = ''):
        self._value = None  
        self.value = value 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            return
        self._value = new_value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        result = re.split(r'[!.?]', self.value)
        result = [sentence for sentence in result if sentence.strip()]
        return len(result)

my_string = MyString("This is a sentence.")
print(my_string.is_sentence())  

my_string = MyString("This is not a sentence")
print(my_string.is_sentence())  

string = MyString("This is a string! It has three sentences. Right?")
print(string.count_sentences())  