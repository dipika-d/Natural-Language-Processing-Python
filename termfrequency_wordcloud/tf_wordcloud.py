# This script takes any PDF document, extracts the lemmas from it, and creates
# a word cloud of the most frequently occurring lemmas in the text. Number of lemmas 
# can be specified as an argument in the 'top' variable. I have used Keith Johnson's
# Signal Processing textbook as an example case in this code.


import os 
import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from string import punctuation 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#sets working directory
os.chdir("/home/allomorph/Downloads")

#ingesting and reading the PDF of the textbook
intext = open("Keith Johnson-Acoustic and auditory phonetics (Kindle friendly).pdf",'rb')
read_text = PyPDF2.PdfFileReader(intext)
num_pages = read_text.getNumPages() #prints the number of pages
#print(num_pages)

#building a stopword set including punctuations
stopwords = set(stopwords.words('english'))
stopwords = stopwords.union(punctuation)

#calling the lemmatizer function
wnl = WordNetLemmatizer()

#building a lexicon of words from the textbook by the variable instances
instances = []
for i in range(0,num_pages):
	page = read_text.getPage(i)
	content = page.extractText()
	content.encode('utf-8')
	tokens = word_tokenize(content)
	filtered_tokens = [word.lower() for word in tokens if word not in stopwords]
	for instance in filtered_tokens:
		instances.append(instance)


#building a list of lemmas in the textbook
lemmas = [wnl.lemmatize(term) for term in instances]
distribution = nltk.FreqDist(lemmas) #getting a list of tuples of the 50 most common words and their frequency
top = [w for w in distribution.most_common(61)]

#getting the most common words that are longer than two letters 
keywords = []
for kw in top:
	for item in kw:
		if type(item)==str and len(item)>2:
			if item not in stopwords:
				keywords.append(item)

#print(keywords)



#generating a word cloud of the most used words in the textbook, size directly proportional to frequency
wordcloud = WordCloud(width = 1000, height = 500).generate(" ".join(keywords))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
