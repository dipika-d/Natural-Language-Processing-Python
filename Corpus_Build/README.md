## Build a Text Corpus from a Wikipedia Data Dump

This directory contains [corpus_build.py](<insert link>) which is a script that extracts and compiles a natural language text corpus from a Wikipedia data dump.

This script is inspired by the article found [here](https://www.kdnuggets.com/2017/11/building-wikipedia-text-corpus-nlp.html) and the Wikipedia dump files can be found [here](https://dumps.wikimedia.org/enwiki/latest/).

__To run on command line :__
```python
python3 corpus_build.py wikipedia_dump_file_name.bz2 processed_output_text_file_name.txt
```
The script might take some time to run depending upon how large your chosen dump file is and if it is running as intended 
you can see ![this](<insert link>) kind of a progress.

This will output a plaintext corpus that can be used for training/testing. 
