from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
text = 'Fazıl Say is a Turkish pianist and composer who was born in Ankara, described recently as "not merely a pianist of genius; but undoubtedly he will be one of the great artists of the twenty-first century".'
stopwords = stopwords.words('english')
words = word_tokenize(text)
print(words)

filtered_words = []
for word in words:
    if word not in stopwords:
        filtered_words.append(word)

print(filtered_words)