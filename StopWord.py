import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps=PorterStemmer()

stop_words = set(stopwords.words('english'))

data = input("Enter the data: ")
data = data.lower()

phrases = sent_tokenize(data)
word = word_tokenize(data)
words = []

for w in word:
    words.append(ps.stem(w))

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

freq = nltk.FreqDist(filtered_sentence)

for key,val in freq.items():
    print (str(key) + ':' + str(val))
