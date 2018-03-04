from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# stop words - preprocessing
ps = PorterStemmer()
example_words = ["python", "pythoner", "pythoned", "pythoning", "pythonli"]
for w in example_words:
    print(ps.stem(w)) #prints the stem of the example_words
new_txt = "It is very important to be pythonly while you are pythoning with python. all pythoners have python programmers"
words = word_tokenize(new_txt)
for w in words:
    print(ps.stem(w))
