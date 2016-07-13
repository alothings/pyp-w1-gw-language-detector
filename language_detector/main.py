"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""

    ls_num = []
    ls_text = text.split()
    for lang in languages:
        ls_num.append(num_of_common(ls_text, lang['common_words']))

    return languages[ls_num.index(max(ls_num))]['name']

                
def num_of_common(ls_text, ls_lang):
    return len([word for word in ls_text if word in ls_lang]);
    
        

#print(common(['a', 'to', 'be'], ['hello', 'to', 'be']))            
   