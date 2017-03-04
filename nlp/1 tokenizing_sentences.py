import nltk
nltk.data.path.append('E:\\VMware_shared\\NLTK_data')
from nltk.tokenize import sent_tokenize, word_tokenize

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

# split by sentences
# print(sent_tokenize(example_text))

# split by words
# print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)