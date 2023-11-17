from nltk.stem import PorterStemmer
#ekleri siliyor
ps = PorterStemmer()
words = ['drive', 'driving', 'driver', 'drives', 'drove', 'cats', 'children']

for w in words:
    print(ps.stem(w))