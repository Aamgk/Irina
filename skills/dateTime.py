from datetime import datetime
import locale

class DateTime:
   def time(self):
      tnow = datetime.now()
      current_time = tnow.strftime("%H:%M")
      return current_time
   
   def date(self):
      dnow = datetime.now()
      current_date = dnow.strftime("%d.%m %Y")
      return current_date


# DateT = DateTime()
# date = DateT.date()
# time = DateT.time()
# print(date)
# print(time)