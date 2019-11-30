import os
import re

user_path = input('Please provide path to text file. ')
user_input = os.path.join(*re.split('[\\\/]', user_path))

#Open, read and split text
with open(user_input,'r') as txt:
    text = txt.read()
    words = re.split(' ',text)
    sentences = re.split('(?<=[.!?])+',text)

#Count words and word lengths
#Contractions and hyphonated words count as a single word
word_len = []
word_len = [len(word.strip()) for word in words]
word_count = len(word_len)
avg_word_len = round(sum(word_len)/word_count,1)

#Count sentences and lengths
sent_len = []
sent_len = [len(sent.strip().strip(',').strip('.').split(' ')) for sent in sentences if len(sent) > 0]
sent_count = len(sent_len)
avg_sent_len = round(sum(sent_len)/sent_count,1)

#Format lines, create, write, and read output file
Lines = ['Paragraph Analysis\n',
    '-------------------\n',
    f'Approximate Word Count: {word_count}\n',
    f'Approximate Sentence Count: {sent_count}\n'
    f'Average Letter Count: {avg_word_len}\n',
    f'Average Sentence Length: {avg_sent_len}']

with open('Paragraph_Analysis.txt','w+') as output:
    output.writelines(Lines)

with open('Paragraph_Analysis.txt','r') as output:
    print(output.read())