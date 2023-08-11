from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report
from model.dataProcessing import TextPreprocessor
import pickle

class TextClassifier:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.tfidf_transformer = TfidfTransformer()
        self.clf = MultinomialNB()
        

    def fit(self, X, y):
        X_counts = self.vectorizer.fit_transform(X)
        X_tfidf = self.tfidf_transformer.fit_transform(X_counts)
        self.clf.fit(X_tfidf, y)

    def predict(self, X):
        X_counts = self.vectorizer.transform(X)
        X_tfidf = self.tfidf_transformer.transform(X_counts)
        return self.clf.predict(X_tfidf)
    
    def evaluate(self, X, y):
        y_pred = self.predict(X)
        print(classification_report(y, y_pred, zero_division=1))
    
    def save_model(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_model(cls, file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)

   

    
# if __name__ == '__main__':
#     # preprocessor = TextPreprocessor()
#     # dataset = preprocessor.preprocess()

#     # if not dataset:
#     #         print("Error: empty dataset")
#     #         exit()
      
#     # clf = TextClassifier()

#     # load_oldckass = TextClassifier.load_model("text_classifier_model.pkl")
#     # X_train = [" ".join(data_point["text"]) for data_point in dataset]
#     # y_train = [data_point["intent"] for data_point in dataset]  
#     # clf.fit(X_train, y_train)

#     # clf.save_model("text_classifier_model.pkl")
#     # print("done")

#     # Load the model from a file
#     loaded_classifier = TextClassifier.load_model("text_classifier_model.pkl")
#     X_test = [
#         "Дарова",
#         "Какой час на часах?",
#         "Всего доброго!",
#         "Какой год",
#         "Что я могу ожидать от погоды сегодня",
#         "Надеюсь, ты можешь открыть Гугл для меня",
#         "Какие операции можешь выполнить",
#         "Добрый день",
#         "Сколько минут",
#         "Пока",
#         "Какой год",
#         "Можете ли вы рассказать о текущих погодных условиях",
#         "Я хотел бы открыть ВК, не мог бы ты сделать это",
#         "Чем ты можешь мне помочь"
#     ] 
#     y_test = ["greeting", "time", "goodbye", "date", "weather", "open", "function", "greeting", "time", "goodbye", "date", "weather", "open", "function"]# corresponding labels
#     y_pred = loaded_classifier.predict(X_test)
#     loaded_classifier.evaluate(X_test, y_test)