from collections import Counter

sentence = 'Peter Piper picked a peck of pickled peppers A peck of pickled peppers \
            Peter Piper picked If Peter Piper picked a peck of pickled \
            peppers Wheres the peck of pickled peppers Peter Piper picked'
words = sentence.split()

word_count = Counter(words)

print word_count['the']
print word_count