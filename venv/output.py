from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize,sent_tokenize,word_tokenize
from nltk import pos_tag,ne_chunk,ngrams,wordpunct_tokenize
from collections import Counter
from nltk.stem import LancasterStemmer
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk import WordNetLemmatizer


s="Google initial public offering (IPO) took place five years later, on August 19, 2004. "

res=wn.synsets("google")
print("wordnet\n",res)
tok=[word_tokenize(t) for t in sent_tokenize(s)]
print("tok\n",tok)
pStemmer = PorterStemmer()
print ("stem")
print(pStemmer.stem(s))
print("pos\n")
print(pos_tag(str(s)))
print("lemm\n")
l=WordNetLemmatizer()
print(l.lemmatize(s))
print("ner\n")
print(ne_chunk(pos_tag(wordpunct_tokenize(s))))
ner=ngrams(s,3)
print(Counter(ner))