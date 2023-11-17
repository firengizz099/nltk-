from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()
words = ['drive', 'driving', 'driver', 'drives', 'drove', 'cats', 'children']
for w in words:
    print(lem.lemmatize(w))
lem.lemmatize('drove', 'v')