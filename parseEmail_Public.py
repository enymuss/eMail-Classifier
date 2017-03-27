import nltk.corpus
import csv
posts = nltk.corpus.nps_chat.xml_posts()
def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word.lower())] = True
    return features

featureSets = []
newPosts =  []
for post in posts:
    featureSets += [(dialogue_act_features(post.text), post.get('class'))]

size = int(len(featureSets) * 0.001)
train_set, test_set = featureSets[size:], featureSets[:size]
classifier = nltk.NaiveBayesClassifier.train(featureSets)



f = open('bigCleanMailbox.txt', 'rU')
featureSetEmail = []
setOfResults = []
d = {}
#classify each line
for line in f:
    line = line.strip()
    if len(line) > 1:
        d = {}
        d["line"] = line
        d["count"] = 1
        newS = line.decode("ascii", 'ignore')
        d["classsifyResult"] = classifier.classify(dialogue_act_features(newS))
        setOfResults += [d]

setOfResults2 = []
#delete duplicates
for i in range(0, len(setOfResults)):
    if setOfResults[i] not in setOfResults[i+1:]:
        setOfResults2.append(setOfResults[i])

#save result to CSV
f = open('mycsvfile.csv','wb')
w = csv.DictWriter(f,d.keys())
w.writerows(setOfResults2)
f.close()

print (nltk.classify.accuracy(classifier, test_set))
