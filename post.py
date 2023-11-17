import nltk

# Her kelime, bir dil bilgisi kategorisine aittir ve cümlenin anlamını anlamak için bu bilgi önemlidir. Dil bilgisi etiketleri, bir kelimenin cinsiyetini, sayısını, zamansal durumunu ve diğer dil özelliklerini belirtir.
# NNP (Proper Noun, Singular): İsim, özel isim, tekil (örneğin, "Friedrich").
# VB (Verb, 3rd person singular present): Fiil, üçüncü tekil şahıs, şimdiki zaman (örneğin, "has").
# JJ (Adjective): Sıfat (örneğin, "profound").
# IN (Preposition): Edat (örneğin, "on").
# CC (Coordinating Conjunction): Bağlaç (örneğin, "and").
text = 'to run,Friedrich Wilhelm Nietzsche was a German philosopher, cultural critic, composer, poet, philologist, and a Latin and Greek scholar whose work has exerted a profound influence on Western philosophy and modern intellectual history. He began his career as a classical philologist before turning to philosophy. He became the youngest ever to hold the Chair of Classical Philology at the University of Basel in 1869 at the age of 24. Nietzsche resigned in 1879 due to health problems that plagued him most of his life; he completed much of his core writing in the following decade. In 1889 at age 44, he suffered a collapse and afterward, a complete loss of his mental faculties. He lived his remaining years in the care of his mother until her death in 1897 and then with his sister Elisabeth Förster-Nietzsche. Nietzsche died in 1900.'
tokenized = nltk.word_tokenize(text)
print(nltk.pos_tag(tokenized))
