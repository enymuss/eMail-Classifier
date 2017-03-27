import nltk

def dialogue_act_features(post):
    features = {}
    print post
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word.lower())] = True
    return features

f = open('msgTwoEmailsClean2.txt', 'rU')
featureSet = []
for line in f:
    if len(line) > 1:
        featureSet += [dialogue_act_features(line)]

for sset in featureSet:
    print sset
