from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import json
import random

class TextPreprocessor:
    def __init__(self, data_path='data.json'):
        with open(data_path, encoding='utf8') as dataset_file:
            self.dataset = json.load(dataset_file)
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('russian'))

    def preprocess(self):
        random.shuffle(self.dataset)
        for data_point in self.dataset:
            tokens = word_tokenize(data_point["text"])
            filtered_tokens = [word for word in tokens if word.lower() not in self.stop_words]
            stemmed_tokens = [self.stemmer.stem(word) for word in filtered_tokens]
            vectorizer = CountVectorizer()
            vectorizer.fit_transform(stemmed_tokens)
            data_point["text"] = tokens
            print(data_point)
        return self.dataset
    


# preprocessor = TextPreprocessor()
# print(preprocessor.preprocess())