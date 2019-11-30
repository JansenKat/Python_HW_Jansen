import os
import sys
import re

user_path = input('Please provide path to text file.')
user_input = os.path.join(*re.split('[\\\/]', user_path))

#Open, read and split text
with open(user_input,'r') as txt:
    text = txt.read()
    words = re.split(' ',text)
    sentences = re.split('(?<=[.!?])+',text)

#Count words and word lengths
#Contractions and hyphonated words count as a single word
word_len = []
for word in words:
    clean = word.strip()
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

#Format lines, create, write, and read output file
Lines = ['Paragraph Analysis\n',
    '-------------------\n',
    f'Approximate Word Count: {word_count}\n',
    f'Approximate Sentence Count: {sent_count}\n'
    f'Average Letter Count: {avg_word_len}\n',
    f'Average Sentence Length: {avg_sent_len}']

output = open('Paragraph_Analysis.txt','w+')
output.writelines(Lines)
output.close()
output = open('Paragraph_Analysis.txt','r')
print(output.read())