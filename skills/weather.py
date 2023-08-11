import requests

class get_Weather:
    def __init__(self):
        self.API_Key = "KEY"

    def getWeather(self, city_name):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.API_Key}"
        response = requests.get(url)
        res = response.json()
        forecast = []
        if res["cod"] != "404":
            data = res["main"]
            city_name = res["name"]
            live_temperature = str(round(data["temp"] - 273)) + "℃"
            live_pressure = data["pressure"]

            temp = ("Температура в " + str(city_name)  + " " + live_temperature)
            pressure = ("Давление: " + str(live_pressure))
            forecast.append(temp)
            forecast.append(pressure)
            return forecast
        else:
            error = ("Город не найден. Попробуйте еще раз")
            return error

            

# input = "Чикаго"
# weather = get_Weather()

# print(weather.getWeather(input))