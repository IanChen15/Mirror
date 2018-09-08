from tkinter import *
import json, urllib.request
from PIL import Image, ImageTk



ui_locale = '' # e.g. 'fr_FR' fro French, '' as default
time_format = 12 # 12 or 24
date_format = "%b %d, %Y" # check python doc for strftime() for options
news_country_code = 'us'
weather_api_token = '<TOKEN>' # create account at https://darksky.net/dev/
weather_lang = 'en' # see https://darksky.net/dev/docs/forecast for full list of language parameters values
weather_unit = 'us' # see https://darksky.net/dev/docs/forecast for full list of unit parameters values
latitude = None # Set this if IP location lookup does not work for you (must be a string)
longitude = None # Set this if IP location lookup does not work for you (must be a string)
xlarge_text_size = 94
large_text_size = 48
medium_text_size = 28
small_text_size = 18

icon_lookup = {
    'clear-day': "assets/Sun.png",  # clear sky day
    'wind': "assets/Wind.png",   #wind
    'cloudy': "assets/Cloud.png",  # cloudy day
    'partly-cloudy-day': "assets/PartlySunny.png",  # partly cloudy day
    'rain': "assets/Rain.png",  # rain day
    'snow': "assets/Snow.png",  # snow day
    'snow-thin': "assets/Snow.png",  # sleet day
    'fog': "assets/Haze.png",  # fog day
    'clear-night': "assets/Moon.png",  # clear sky night
    'partly-cloudy-night': "assets/PartlyMoon.png",  # scattered clouds night
    'thunderstorm': "assets/Storm.png",  # thunderstorm
    'tornado': "assests/Tornado.png",    # tornado
    'hail': "assests/Hail.png"  # hail
}

class Weather(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.locationLbl = Label(self, text="hello", font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.locationLbl.pack(side=TOP, anchor=CENTER)
        self.degreeFrm = Frame(self, bg="black")
        self.degreeFrm.pack(side=TOP, anchor=CENTER)
        self.temperatureLbl = Label(self.degreeFrm, font=('Helvetica', large_text_size), fg="white", bg="black", anchor=CENTER)
        self.iconLbl = Label(self.degreeFrm, bg="black")
        self.iconLbl.pack(side=LEFT, anchor=CENTER, padx=20)
        self.temperatureLbl.pack(side=LEFT, anchor=N)
        self.currentlyLbl = Label(self, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.currentlyLbl.pack(side=TOP, anchor=W)
        self.forecastLbl = Label(self, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.forecastLbl.pack(side=TOP, anchor=W)
        self.update_weather()

    def update_weather(self):
        data = self._load_data()

        self._update_current_weather(data)
        city = data['query']['results']['channel']['location']['city']
        province = data['query']['results']['channel']['location']['region']
        self.locationLbl.config(text= city + ', ' + province)
        # self._update_forcasts(data)
        self.after(60000, self.update_weather)


    def _update_current_weather(self, data):
        # data['query']['results']['channel']['item']['condition'] current weather
        #            {'code': '29', 'date': 'Fri, 03 Aug 2018 09:00 PM PDT', 'temp': '64', 'text': 'Partly Cloudy'}
        temp = self.fah_to_cel(int(data['query']['results']['channel']['item']['condition']['temp']))
        condition = data['query']['results']['channel']['item']['condition']['code']
        self.temperatureLbl.config(text=str(temp) + chr(176) + "C")

        image = Image.open(self.icon_lookup(condition))
        image = image.resize((60, 60), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)

        self.iconLbl.config(image=photo)
        self.iconLbl.image = photo

    def _load_data(self):
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select * from weather.forecast where woeid=56690943"
        yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        return json.loads(result.decode('utf-8'))

    def icon_lookup(self, key_word):
        icon_lookup = {
            '0' : "assets/Tornado.png",
            '1' : "assets/Storm.png",
            '2' : "assets/Wind.png",
            '3' : "assets/Storm.png",
            '4' : "assets/Storm.png",
            '5' : "assets/RainAndSnow.png",
            '6' : "assets/Hail.png",
            '7' : "assets/Hail.png",
            '8' : "assets/Hail.png",
            '9' : "assets/Hail.png",
            '10': "assets/Hail.png",
            '11': "assets/Rain.png",
            '12': "assets/Rain.png",
            '13': "assets/Snow.png",
            '14': "assets/Snow.png",
            '15': "assets/Snow.png",
            '16': "assets/Snow.png",
            '17': "assets/Hail.png",
            '18': "assets/Hail.png",
            '19': "assets/Haze.png",
            '20': "assets/Haze.png",
            '21': "assets/Haze.png",
            '22': "assets/Haze.png",
            '23': "assets/Wind.png",
            '24': "assets/Wind.png",
            '25': "assets/Newspaper.png",
            '26': "assets/Cloud.png",
            '27': "assets/PartlyMoon.png",
            '28': "assets/PartlySunny.png",
            '29': "assets/PartlyMoon.png",
            '30': "assets/PartlySunny.png",
            '31': "assets/Moon.png",
            '32': "assets/Sun.png",
            '33': "assets/Moon.png",
            '34': "assets/Sun.png",
            '35': "assets/Hail.png",
            '36': "assets/Sunny.png",
            '37': "assets/Storm.png",
            '38': "assets/Storm.png",
            '39': "assets/Storm.png",
            '40': "assets/Rain.png",
            '41': "assets/Snow.png",
            '42': "assets/RainAndSnow.png",
            '43': "assets/Snow.png",
            '44': "assets/Haze.png",
            '45': "assets/Storm.png",
            '46': "assets/Snow.png",
            '47': "assets/Storm.png",
            '3200': "assets/Newspaper.png"
        }
        if key_word in icon_lookup:
            return icon_lookup[key_word]
        else:
            return icon_lookup["3200"]

    def fah_to_cel(self, i):
        return int((i - 32)*5/9)

class ForcastFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.temp_frame = Frame(self, bg="black")

        self.weather_icon_lbl = Label(self, bg="black")
        self.day_lbl = Label(self, font=("Helvetica", small_text_size), fg="white", bg="black")
        self.highest_temp_lbl = Label(self.temp_frame, font=("Helvetica", small_text_size), fg="white", bg="black")
        self.lowest_temp_lbl = Label(self.temp_frame, font=("Helvetica", small_text_size), fg="white", bg="black")

        self.day_lbl.pack(side=TOP)
        self.weather_icon_lbl.pack()
        self.temp_frame.pack(side=BOTTOM)
        self.lowest_temp_lbl.pack(side=LEFT)
        self.highest_temp_lbl.pack(side=RIGHT)

    def update_info(self, day, high, low, weather):
        self.day_lbl.config(text=day)
        self.highest_temp_lbl.config(text=high)
        self.lowest_temp_lbl.config(text=low)
        self.weather_icon_lbl.image = self.load_image(weather)
    def load_image(self, weather):
        image = Image.open(icon_lookup[weather])
        image = image.resize((50, 50), Image.ANTIALIAS)
        image = image.convert('RGB')
        return ImageTk.PhotoImage(image)

# data['query']['results']['channel']['item']['condition'] current weather
#            {'code': '29', 'date': 'Fri, 03 Aug 2018 09:00 PM PDT', 'temp': '64', 'text': 'Partly Cloudy'}
# data['query']['results']['channel']['item']['forecast'] forecast
#            array of {'code': '28', 'date': '03 Aug 2018', 'day': 'Fri', 'high': '69', 'low': '58', 'text': 'Mostly Cloudy'}
# data['query']['results']['channel'][location]
#             {'city': 'Langley', 'country': 'Canada', 'region': ' BC'}
