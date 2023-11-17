import nltk
text = "Steve Jobs was an American entrepreneur and business magnate. He was the chairman, chief executive officer (CEO), and a co-founder of Apple Inc., chairman and majority shareholder of Pixar, a member of The Walt Disney Company's board of directors following its acquisition of Pixar, and the founder, chairman, and CEO of NeXT. Jobs is widely recognized as a pioneer of the microcomputer revolution of the 1970s and 1980s, along with Apple co-founder Steve Wozniak. "
tokenized = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokenized)
named_ent = nltk.ne_chunk(tagged)
named_ent.draw()

#Elbette, anlatımı basitleştirelim. Bu kod, bir metindeki adlandırılmış varlıkları (kişilerin isimleri, şirket isimleri, vb.) belirlemek ve görselleştirmek için kullanılır.
#Özetle, bu kod metindeki adlandırılmış varlıkları belirler ve görselleştirir. Örneğin, "Steve Jobs" gibi isimleri veya "Apple Inc." gibi şirket isimlerini tanıyabilir ve bu bilgileri görsel bir şekilde sunabilir.