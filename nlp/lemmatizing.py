import nltk
# Appending NLTK data folder to the NLTK data path
nltk.data.path.append('E:\\VMware_shared\\NLTK_data')

# Lemmatizing is similar to stemming
# output is a word with a same meaning as origial word

# Importing dependencies
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# checking if works
# print all synonyms for wicked
print(lemmatizer.lemmatize("wicked"))
