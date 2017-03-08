import nltk;
nltk.download()
emma = nltk.corpus.gutenberg.words('austen-emma.txt');
print(len(emma));