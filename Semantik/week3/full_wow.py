# coding: utf-8
import gensim
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import re
import sys
'''
sentences = []
with open("../gg.txt", 'r') as file:
    words = []
    for line in file:
        word, pos, lemma = line.split('\t')
        word = re.sub('-', '', word)
        if word in '.?!:':
            sentences.append(words)
            words = []
            continue
        if word not in ',—':
            words.append(word)


lemma_sentences = []
with open("../gg.txt", 'r') as file:
    words = []
    for line in file:
        word, pos, lemma = line.strip().split('\t')
        word = re.sub('-', '', word)
        lemma = re.sub('-', '', word)
        if word in '.?!:':
            lemma_sentences.append(words)
            words = []
            continue
        if word not in ',—' and lemma != '<unknown>':
            words.append(word + '_' + lemma)
            

pos_sentences = []
with open("../gg.txt", 'r') as file:
    words = []
    for line in file:
        word, pos, lemma = line.split('\t')
        if word in '.?!:':
            pos_sentences.append(words)
            words = []
            continue
        if word not in ',—':
            words.append(word + '_' + pos[0])
'''

lemma_only_sentences = []
with open("../gg.txt", 'r') as file:
    words = []
    for line in file:
        word, pos, lemma = line.strip().split('\t')
        if lemma in '.?!:':
            lemma_only_sentences.append(words)
            words = []
            continue
        if lemma != '<unknown>':
            words.append(lemma)
        else:
            words.append(word)
            
            
model = gensim.models.Word2Vec(lemma_only_sentences, size=150, window=5, min_count=2)

with open("wordstoplot.txt", 'r', encoding='utf-8') as file:
    words = [line.strip() for line in file.readlines() if not line.startswith(' ')]
    #words = [line.strip() for line in file.readlines()]

    
X = []
ws = []
for word in words:
    try:
        w = word.split('/')[1]
        X.append(model[w])
        ws.append(word)
    except KeyError:
        print(word, " skipped")

pca = PCA(n_components=2)
result = pca.fit_transform(X)
'''
with open("table.txt", 'w', encoding='utf-8') as file:
    for i, w in enumerate(ws):
        file.write('{}\t{}\t{}/{}\n'.format(result[i,0], result[i,1], w[1], w[0]))
'''
sc = plt.scatter(result[:, 0], result[:, 1])
for i, w in enumerate(ws):
    annot = plt.annotate(w, xy=(result[i,0], result[i,1]))

plt.show()
