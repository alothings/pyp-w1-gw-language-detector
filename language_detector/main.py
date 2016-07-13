"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""

    ls_num = []
    words_text = text.split()
    for lang in languages:
        words_lang = lang['common_words']
        ls_num.append(num_of_common_words(words_text, words_lang))
        
    lang_index = ls_num.index(max(ls_num))
    return languages[lang_index]['name']

                
def num_of_common_words(ls_text, ls_lang):
    return len([word for word in ls_text if word in ls_lang]);
    
   