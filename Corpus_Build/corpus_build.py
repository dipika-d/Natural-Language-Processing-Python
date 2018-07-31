import sys
from gensim.corpora import WikiCorpus

def build_corpus(infile,outfile):
	""" Converts a Wikipedia xml dump to a text corpus"""
	output = open(outfile,'w')
	wiki = WikiCorpus(infile)

	i = 0
	for text in wiki.get_texts():
		output.write(bytes(' '.join(text),'utf-8').decode('utf-8')+'\n')
		i += 1
		if (i%10 == 0):
			print('Processed '+ str(i) + ' articles')

	output.close()
	print('Processing complete!')

if __name__=="__main__":
	if len(sys.argv) != 3:
		print('Usage: python make_wiki_corpus.py <wikipedia_dump_file> <processed_text_file>')
		sys.exit(1)
	infile = sys.argv[1]
	outfile = sys.argv[2]
	build_corpus(infile,outfile)

