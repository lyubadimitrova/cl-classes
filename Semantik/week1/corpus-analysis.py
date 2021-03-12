# coding: utf-8
from nltk.corpus import PlaintextCorpusReader
from nltk.book import *

corpus_root = 'bg_corpus'
c = PlaintextCorpusReader(corpus_root, '.*')

print(len([filename for filename in c.fileids() if filename.endswith("txt")]), " documents\n")
print(len(c.words("all_docs")), " tokens\n")

vocab = set()
for word in c.words("all_docs"):
    vocab.add(word.lower())
print(len(vocab), " types\n") 


fdist = FreqDist([w.lower() for w in c.words('all_docs')])
fdist.plot(100)              #not too nice looking


with open("words.txt", 'w', encoding='utf-8') as file:          #to get a kind of table, which I then used in an online graph maker
    for tuple in fdist.most_common(200):
        file.write(tuple[0])
        file.write('\t')
        file.write(str(tuple[1]))
        file.write('\n')

        
        
