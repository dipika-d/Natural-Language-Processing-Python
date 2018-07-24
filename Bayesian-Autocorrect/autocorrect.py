""" Author - Dipika Desaboyina
This is a simple probabilistic autocorrector implemented using Peter Norvig's approach
and the Edit Distance Algorithm """

import re
from collections import Counter

# words() tokenizes the given text
def words(text):
	pattern = re.compile('\w+\s*')
	words = re.findall(pattern,text)
	words = [word.strip() for word in words]
	return words

# hashtable that contains the word frequencies from big.txt
WORDS = Counter(words(open('big.txt').read()))

# 10 most frequent words from big.txt
# print(WORDS.most_common(10))

# P(word) in big.txt 
def P(word):
	N = sum(WORDS.values())
	return (WORDS[word])/N

# correction() returns corrected word upon searching incorrect spelling
def correction(word):
	return max(candidates(word),key=P)

# candidates() creates set of all candidates that could be possible corrections of the spelling)
def candidates(word):
	return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

# the subset of words that is in WORDS
def known(words):
	return set(word for word in words if word in WORDS)

# all the possible corrections that are 1 edit distance away using the four operations -> delete, transpose, replace, insert
def edits1(word):
	letters = 'abcdefghijklmnopqrstuvwxyz'
	splits = [(word[:i],word[i:]) for i in range(len(word)+1)]
	deletes = [L+R[1:] for L,R in splits if R]
	transposes = [L+R[1]+R[0]+R[2:] for L,R in splits if len(R)>1]
	replaces = [L+c+R[1:] for L,R in splits if R for c in letters]
	inserts = [L+c+R for L,R in splits for c in letters]
	return set(deletes+transposes+replaces+inserts)

# all the possible corrections of the word from edits1 -> words that are two edit distances away
def edits2(word):
	return(e2 for e1 in edits1(word) for e2 in edits1(e1))

def spell_check():
	response = input("Please enter your search term\n")
	print("Did you mean "+correction(response)+"?")
	print("\t********\t")
	print("\n")
	spell_check()

spell_check()




