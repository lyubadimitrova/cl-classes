import gensim
import re
from scipy.stats import spearmanr, pearsonr

'''
lemma_only_sentences = []
with open("odds&ends/gg.txt", 'r') as file:
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
'''

sentences = []
with open("odds&ends/gg.txt", 'r') as file:
    words = []
    for line in file:
        word, pos, lemma = line.split('\t')
        #word = re.sub('-', '', word)
        if word in '.?!:':
            sentences.append(words)
            words = []
            continue
        if word not in ',—':
            words.append(word)
            
#model = gensim.models.Word2Vec(lemma_only_sentences, size=150, window=5, min_count=0)
model = gensim.models.Word2Vec(sentences, size=200, window=5, min_count=0)

with open("rg.txt", 'r', encoding='utf-8') as file:
    pairs = [line.strip().split(';') for line in file.readlines() if not line.startswith(' ')]

    
X = []
Y = []
ps = []
for pair in pairs:
    try:
        X.append((model[pair[0]],model[pair[1]]))
        Y.append(float(pair[2]))
        ps.append(pair)
    except KeyError:
        print(pair, " skipped")
        
pY = []
for pair in ps:
    pY.append(model.similarity(pair[0], pair[1]))

print(Y)
print(pY)
print(spearmanr(Y, pY))
print(pearsonr(Y, pY))
    
        
