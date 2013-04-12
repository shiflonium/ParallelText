import requests
import re
from bs4 import BeautifulSoup


language_dictionaries = {
    'SQ': 1,       # Albanian
    'AR': 2,       # Arabic
    'BG':3,        # Bulgarian
    'CS':  4,       # Czech
    'FA':  5,       # Farsi
    'FR':  6,       # French
    'DE': 7,        # German
    'EL': 8,        # Greek
    'HU': 9,       # Hungarian
    'IT': 10,       # Italian
    'LV': 11,     # Latvian
    'PL': 12,     # Polish
    'PT': 13,     # Portuguese
    'RO': 14,     # Romanian
    'RU': 15,     # Russian
    'HR': 16,     # Croatian
    'SK': 17,     # Slovak
    'ES': 18,     # Spanish
    'SV': 19,     # Swedish
    'TR':20,      # Turkish
    'VI': 21,      # Vietnamese
    'YI': 22,      # Yiddish
    'EN': 23,    # English
    'ZH': 24      # Chinese
    'HE': 25      # Hebrew
}


from_lang = str(language_dictionaries['EN'])
to_lang  = str(language_dictionaries['HE'])
word = "God"
dictionary_request="http://www.lingvozone.com/dictionary?action=translation_ajax&language_id_from=" + from_lang + "&language_id_to=" + to_lang + "&word_id=&word=" + word
r = requests.get(url)
response_text = r.text
soup = BeautifulSoup(response_text)
definition_soup = soup.find_all('a' , {"class": "black"})
for definition in (definition_soup):
    definition_string = definition.string
    print definition_string

