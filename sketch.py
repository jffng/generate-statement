from sys import argv
from clarifai.client import ClarifaiApi
import nltk, random
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]
api = ClarifaiApi();
imgs = []
for f in onlyfiles:
	if 'jpg' in f:
		imgs.append('./' + f)

beg = int(argv[1])
end = int(argv[2])

results = []
for i in imgs[beg:end]:
	results.append(api.tag_images([open(i)]))

words = results[0]['results'][0]['result']['tag']['classes']
try:
	words += results[1]['results'][0]['result']['tag']['classes']
except:
	print 'second image blows'
	
sentence = ''

for w in words:
	sentence += str(w) + ' '

text = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(text)

nouns = []
adjectives = []
plural = []
verbs = []

for t in tags:
    if 'NNS' in t[1]:
        plural.append(t[0])
    elif 'JJ' in t[1]:
        adjectives.append(t[0])
    elif 'NN' in t[1]:
        nouns.append(t[0])
    elif 'V' in t[1]:
        verbs.append(t[0])

nn1 = nouns[random.randint(0,len(nouns)-1)]
nn2 = nouns[random.randint(0,len(nouns)-1)]
nn3 = nouns[random.randint(0,len(nouns)-1)]
nn4 = nouns[random.randint(0,len(nouns)-1)]
nn5 = nouns[random.randint(0,len(nouns)-1)]
nn6 = nouns[random.randint(0,len(nouns)-1)]
nn7 = nouns[random.randint(0,len(nouns)-1)]
try:
	jj1 = adjectives[1]
	jj2 = adjectives[2]
	jj3 = adjectives[0]
except:
	print 'less than three adjectives'

try:
	vb = verbs[random.randint(0,len(verbs)-1)]
except:
	print 'no verbs'

try:
	nns = plural[random.randint(0,len(plural)-1)]
except:
	print 'no plural'

try:
    print "Her artworks demonstrate how {noun1} extends beyond its own subjective limits and often tells a story about the effects of {noun2} over the latter half of the twentieth century.\n".format(noun1=nn1,noun2=nn2) 
    print "It challenges the binaries we continually reconstruct between {noun3} and {noun4}, between our own '{adj1}' and '{adj2}' selves.\n".format(noun3=nn3,noun4=nn4,adj1=jj1,adj2=jj2)
    print "In a search for new methods to '{verb1}', she focuses on the idea of '{noun4}' and more specifically on '{plural1}' where anyone can do anything at any given moment: the non-private {noun5} the non-privately owned {noun6} that is {adj3}.\n".format(verb1=vb,noun4=nn4,plural1=nns,noun5=nn5,noun6=nn6,adj3=jj3)
    print "\n"
except:
    print 'failed first\n'
try:
    print "My work explores the relationship between {noun1} and {noun2}.\n".format(noun1=nn1,noun2=nn2)
    print "With influences as diverse as {noun3} and {noun4}, new tensions are distilled from both traditional and modern {plural}\n".format(noun3=nn3,noun4=nn4,plural=nns)
    print "As {noun5} becomes distorted through {adj} practice, the viewer is left with a clue to the inaccuracies of our {noun6}.\n".format(noun5=nn5,adj=jj1,noun6=nn6)
    print "\n"
except:
    print 'failed second\n'
try:
    print "Her works are characterised by the use of {noun1} in an atmosphere of {adj} mentality in which {noun2} plays an important role.\n".format(noun1=nn1,adj=jj1,noun2=nn2) 
    print "By taking {noun3} as subject matter while commenting on the {adj2} aesthetic of middle class values, her works references {noun4} as well as the {noun5} or the {noun6} and the {adj3} movement as a form of resistance against the logic of the {noun7}.\n".format(noun3=nn3,noun4=nn4,noun5=nn5,noun6=nn6,noun7=nn7,adj2=jj2,adj3=jj3)
except:
    print 'failed third'