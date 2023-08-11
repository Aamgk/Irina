from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
class TextProcess:
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('russian'))
        self.vectorizer = CountVectorizer()
 
    def preprocess(self, input):
        preprocessed_texts = []
        tokens = word_tokenize(input, language='russian')
        print(tokens)
        filtered_tokens = [word for word in tokens if word.lower() not in self.stop_words]
        stemmed_tokens = [self.stemmer.stem(word) for word in filtered_tokens]
        preprocessed_texts.append(' '.join(stemmed_tokens))
        print(preprocessed_texts)
        self.vectorizer.fit_transform(preprocessed_texts)
        return preprocessed_texts

    

# tp = TextProcess()
# input = "Скажи мне часы"
# print(input)
# print(word_tokenize(input))
# print(tp.preprocess(input))