from nltk.tokenize import sent_tokenize, word_tokenize
text = "Alan Turing, İngiliz matematikçi, bilgisayar bilimcisi ve kriptolog. Bilgisayar biliminin kurucusu sayılır. Geliştirmiş oldugu Turing testi ile makinelerin ve bilgisayarların düşünme yetisine sahip olup olamayacakları konusunda bir kriter öne sürmüştür."
print(text.split())
print(word_tokenize(text))

print(sent_tokenize(text))

for token in word_tokenize(text):
    print(token)