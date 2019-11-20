import os
import re

#user_input = input('Please provide path to text file.')
user_input = 'raw_data/readme_test.txt'

#Open, read and split text
with open(user_input,'r') as txt:
    text = txt.read()
    words = re.split(' ',text)
    sentences = re.split('(?<=[.!?])+',text)
print(len(words))
#Count words and word lengths
word_len = []
for word in words:
    if len(word)>0:
        clean = word.strip().strip(',').strip('.').strip('\'')
        #print(clean)
        #print(len(clean))
        word_len.append(len(clean))
word_count = len(word_len)
avg_word_len = round(sum(word_len)/word_count,1)

#Count sentences and lengths
sent_len = []
for sent in sentences:
        if len(sent)>0:
            clean = sent.strip().strip(',').strip('.').split(' ')
            sent_len.append(len(clean))
sent_count = len(sent_len)
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