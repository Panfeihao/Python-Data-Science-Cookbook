from nltk import stem

input_words = ['movies', 'dogs', 'planes', 'flowers', 'flies', 'fries', 'fry', 'weeks' 'planted', 'running', 'throttle']

wordnet_lemm = stem.WordNetLemmatizer()
wn_words = [wordnet_lemm.lemmatize(w) for w in input_words]
print wn_words