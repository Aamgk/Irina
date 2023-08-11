from skills.responses import Replies
from model.textClass import TextClassifier
from model.textProcessing import TextProcess
from skills.speaklisten import SpeakListen
from model.dataProcessing import TextPreprocessor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split



class VA:
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.clf = TextClassifier.load_model("text_classifier_model.pkl")
        self.sp = SpeakListen()
        self.input_processor = TextProcess()
        self.rp = Replies()

    def assistent(self):    
        self.sp.speak("Здравствуйте, я голосовой ассистент Ирина")
        while(True):
            self.sp.speak("Чем могу помочь?")
            input = self.sp.listen()
            print(input)
            processed_input = self.input_processor.preprocess(input)
            intent = self.clf.predict(processed_input)
            # print(intent)
            # print(self.rp.Replying(intent))
            self.rp.Replying(intent, processed_input)
            # self.sp.speak(say)


assist = VA()
assist.assistent()