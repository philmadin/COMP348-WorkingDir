import nltk
nltk.download('punkt')
nltk.download('reuters')
nltk.download('gutenberg')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')
hope = nltk.corpus.gutenberg.raw('austen-emma.txt')
print(hope)