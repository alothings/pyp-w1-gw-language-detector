"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""

    num_of_common_words = []
    text_words = text.split()
    for lang_dict in languages:
        lang_words = lang_dict['common_words']
        num_of_common_words.append(num_common_elements(text_words, lang_words))
        
    max_lang_index = num_of_common_words.index(max(num_of_common_words))
    return languages[max_lang_index]['name']

                
def num_common_elements(list_1, list_2):
    return len([word for word in list_1 if word in list_2]);
    
   