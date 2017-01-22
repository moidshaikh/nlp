import nltk
# Appending NLTK data folder to the NLTK data path
nltk.data.path.append('E:\\VMware_shared\\NLTK_data')

# Importing dependencies
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


example_text = '''The following files can be redistributable under the license below: " \
               "Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
* Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
* Neither the name of YourKit nor the
  names of its contributors may be used to endorse or promote products
  derived from this software without specific prior written permission.
"'''
stop_words = set(stopwords.words("english"))

# Tokenizing
words = word_tokenize(example_text)


filtered_text = []

for w in words:
    if w not in stop_words:
        filtered_text.append(w)

print(filtered_text)

# print(len(example_text))
# print(len(filtered_text))