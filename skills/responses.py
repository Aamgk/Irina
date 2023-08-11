from skills.dateTime import DateTime
from skills.weather import get_Weather
from skills.greet import Greet
from skills.bye import GoodBye
from skills.speaklisten import SpeakListen
from skills.open import Open
from skills.func import Functions

class Replies:
    def __init__(self):
        self.sp = SpeakListen()


    def Replying(self, intent, input):
        if intent == 'greeting':
            greet  = Greet()
            result = greet.greeting()
            self.sp.speak(result)
            return result 
        elif intent == 'goodbye':
            bye = GoodBye()
            self.sp.speak(bye.byeBye()) 
            exit()
        elif intent == 'time':
            tm = DateTime()
            result = "Время сейчас: " + str(tm.time())
            self.sp.speak(result)
            return result  
        elif intent == 'date':
            dt = DateTime()
            result = 'Сегодня: ' + str(dt.date())
            self.sp.speak(result)
            return result
        elif intent == 'weather':
            text = "Погоду какого города вы хотите узнать?"
            self.sp.speak(text)
            city_name = self.sp.listen()
            print(city_name)
            weather = get_Weather()
            result = weather.getWeather(city_name)
            self.sp.speak(result) 
            return result
        elif intent == 'open':
            op = Open(input)
            self.sp.speak("Открываю...")
            op.Open_sesame()
            return "open"
        elif intent == 'function':
            f = Functions()
            self.sp.speak(f.tell_Functions())
            return "done"
        else:
            self.sp.speak("ПРостите, я вас не поняла")

           
         
    
# lists = ['Можешь', ',', 'пожалуйста', ',', 'открыть', 'Google']
# r = Replies()
# print(r.Replying('open',lists))