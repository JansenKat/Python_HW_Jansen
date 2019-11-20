import os
import re

#user_input = input('Please provide path to text file.')
user_input = 'raw_data/readme_test.txt'

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

avg_word_len = round(sum(word_len)/word_count,1)

#Count sentences and lengths
sent_count = len(sentences) + 1
sent_len = []

for sent in sentences:
    sent = sent.split(' ')
    sent_len.append(len(sent)+1)

avg_sent_len = round(sum(sent_len)/sent_count,1)

Lines = ['Paragraph Analysis\n',
    '-----------------\n',
    'Approximate Word Count: ' + str(word_count) + '\n',
    'Approximate Sentence Count: ' + str(sent_count) + '\n'
    'Average Letter Count: ' + str(avg_word_len) + '\n',
    'Average Sentence Length: ' + str(avg_sent_len)]

output = open('Paragraph_Analysis.txt','w+')
output.writelines(Lines)
output.close()
output = open('Paragraph_Analysis.txt','r')
print(output.read())