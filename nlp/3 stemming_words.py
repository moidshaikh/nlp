# Appending NLTK data folder to the NLTK data path
import nltk
nltk.data.path.append('E:\\VMware_shared\\NLTK_data')

# import dependencies

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


# Stemming is converting words to base word

ps = PorterStemmer()

t = 'run running ran runnable runnability interrun'
# print(t.split(' '))
# example_words = t.split(' ')

example_words = ['python', 'pythoner','pythoning','pythoned','pythonly']

for w in example_words:
    print(ps.stem(w))