
import nltk
from nltk import tokenize
nltk.download('punkt')
nltk.download('words')

para = "Hello! My name is Ritu. Today you'll be learning NLTK."
sents = tokenize.sent_tokenize(para)
print("\nSentence Tokenization\n====================\n", sents)

#word tokenize
print("\nWord Tokenization\n=================\n")
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index])
    print(words)
