import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('names')
from nltk.corpus import names
m = names.words('male.txt')
f = names.words('female.txt')
import random
random.seed(54321) # Set the random seed to allow replicability
names = ([(name,'male') for name in m] +
         [(name,'female') for name in f])
random.shuffle(names)
train_names = names[1500:]
devtest_names = names[500:1500]
test_names = names[:500]
def gender_features2(word):
    return {'suffix1': word[-1:],
            'suffix2': word[-2:]}
train_set2=[(gender_features2(n),g) for (n,g) in train_names]
devtest_set2=[(gender_features2(n),g) for (n,g) in devtest_names]
classifier2=nltk.NaiveBayesClassifier.train(train_set2)
nltk.classify.accuracy(classifier2,devtest_set2)
#print(classifier2.most_informative_features())
#print(classifier2.show_most_informative_features())
def gender_features5(word):
    return {'suffix1': word[-1:],
            'suffix2': word[-2:],
            'suffix3': word[-3:],
            'suffix4': word[-4:],
            'suffix5': word[-5:]}

train_set3=[(gender_features5(n),g) for (n,g) in train_names]
devtest_set3=[(gender_features5(n),g) for (n,g) in devtest_names]
classifier3=nltk.NaiveBayesClassifier.train(train_set3)
nltk.classify.accuracy(classifier3,devtest_set3)
#print(classifier3.show_most_informative_features())
