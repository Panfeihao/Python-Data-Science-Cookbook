# 1
sentence = 'Peter Piper picked a peck of pickled peppers A peck of pickled peppers \
            Peter Piper picked If Peter Piper picked a peck of pickled \
            peppers Wheres the peck of pickled peppers Peter Piper picked'

# 2
word_dict = {}
# 3
# for word in sentence.split():
#     if word not in word_dict:
#         word_dict[word] =1
#     else:
#         word_dict[word]+=1
# 3.1
for word in sentence.split():
    word_dict.setdefault(word,0)
    word_dict[word]+=1
    
# 4
print word_dict
