# coding: utf-8
import gensim
from scipy.stats import spearmanr, pearsonr
sentences = []
with open("odds&ends/gg.txt", 'r') as file:
    words = []
    for line in file:
        word = line.split('\t')[0]
        if word in '.?!:':
            sentences.append(words)
            words = []
            continue
        if word != ',':
            words.append(word)
            
model = gensim.models.Word2Vec(sentences, size=200, window=5, min_count=0)
with open('rg.txt', 'r', encoding='utf-8') as file:
    pairs = [line.strip().split(';') for line in file.readlines() if not line.startswith(' ')]
    
X = []
Y = []
ps = []
for pair in pairs:
    try:
        X.append((model[pair[0]], model[pair[1]]))
        Y.append(float(pair[2]))
        ps.append(pair)
    except KeyError:
        print(pair, ' skipped')
        
pY = []
for pair in ps:
    pY.append(model.similarity(pair[0], pair[1]))
    
pY
spearman(Y, pY)
spearmanR(Y, pY)
spearmanr(Y, pY)
spearmanr(Y, pY)
with open('mc.txt', 'r', encoding='utf-8') as file:
    pairs2 = [line.strip().split(';') for line in file.readlines() if not line.startswith(' ')]
    
X2, Y2, ps2 = [], [], []
X2.append(3)
Y2
X2.pop()
X2
for pair in pairs2:
    try:
        X2.append((model[pair[0]], model[pair[1]]))
        Y2.append(float(pair[2]))
        ps2.append(pair)
    except KeyError:
        print(pair, ' skipped')
        
pY2 = []
for pair in ps2:
    pY.append(model.similarity(pair[0], pair[1]))
    
spearman(Y2, pY2)
spearmanr(Y2, pY2)
len(pairs2)
len(X)
len(X2)
len(Y2)
len(ps2)
len(pY2)
for pair in ps2:
    pY2.append(model.similarity(pair[0], pair[1]))
    
spearmanr(Y2, pY2)
pY = []
for pair in ps:
    pY.append(model.similarity(pair[0], pair[1]))
    
spearmanr(Y, pY)
pearsonr(Y, pY)
pearson(Y2, pY2)
pearsonr(Y2, pY2)
