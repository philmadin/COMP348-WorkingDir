import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('names')
from nltk.corpus import names
m = names.words('male.txt')
f = names.words('female.txt')
import random
random.seed(1234) # Set the random seed to allow replicability
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
#print(nltk.classify.accuracy(classifier2,devtest_set2))
#print(classifier2.most_informative_features())
#print(classifier2.show_most_informative_features())
def gender_features5(word):
    return {'suffix1': word[-1:],
            'suffix2': word[-2:],
            'suffix3': word[-3:],
            'suffix4': word[-4:],
            'suffix5': word[0],
            'suffix6': word[:1]}

train_set3=[(gender_features5(n),g) for (n,g) in train_names]
devtest_set3=[(gender_features5(n),g) for (n,g) in devtest_names]
classifier3=nltk.NaiveBayesClassifier.train(train_set3)
test_set3=[(gender_features5(n),g) for (n,g) in test_names]
classifier3=nltk.NaiveBayesClassifier.train(train_set3)
print(nltk.classify.accuracy(classifier3,test_set3))
#print(nltk.classify.accuracy(classifier3,devtest_set3))
#print(classifier3.show_most_informative_features())
train_accuracy2 = []
devtest_accuracy2 = []
nsamples = range(10,500,5)
for n in nsamples:
    classifier2 = nltk.NaiveBayesClassifier.train(train_set2[:n])
    train_accuracy2.append(nltk.classify.accuracy(classifier2,train_set2[:n]))
    devtest_accuracy2.append(nltk.classify.accuracy(classifier2,devtest_set2))

from matplotlib import pyplot as plt
plt.plot(nsamples,train_accuracy2,label='Train')
plt.plot(nsamples,devtest_accuracy2,label='Devtest')
plt.xlabel('Training size')
plt.ylabel('Accuracy')
plt.title('Classifier 2')

plt.legend()
plt.show()