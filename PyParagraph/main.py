import os
import re

user_input = input('Please provide path to text file.')

#Open, read and split text
with open(user_input,'r') as txt:
    text = txt.read()
    words = re.split(' ',text)
    sentences = re.split('(?<=[.!?])+',text)

#Count words and word lengths
word_count = len(words) + 1
word_len = []

for word in words:
    word_len.append(len(word))

#Count sentences and lengths
sent_count = len(sentences) + 1
sent_len = []

for sent in sentences:
    sent = sent.split(' ')
    sent_len.append(len(sent)+1)

print('Word_count: ' + str(word_count))
print('Sent_count: ' + str(sent_count))
