from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from weather_checker.models import Weather

# Create your views here.
from django.http import HttpResponse, HttpRequest
import requests
from weather_checker.models import ZipCode
from datetime import datetime


class Weather(object):

    def __init__(self, updated_time, temperature, humidity, windspeed):
        self.updated_time = updated_time
        self.temperature = temperature
        self.humidity = humidity
        self.windspeed = windspeed


def index(request):
    return render(request, 'weather/weather.html')


@csrf_exempt
def weather_details(request):
    zipcode = ''
    if request.method == 'POST':
        zipcode = request.POST.get('zipcode')
        country = request.POST.get('country')

        # date_to_check = request.POST.get('date')

   # zipcode_object = ZipCode()
 #   zipcode_object.zip = zipcode
 #    zipcode_object.country = country
 #
 #    zipcode_object.save()



    print('zipcode is ' + zipcode)
    result = requests.get( url_generator(zipcode, False))
    result = result.json()
    print('result is ' + str((result['main']['temp']-273)*5/9 + 32))

    temperature = (result['main']['temp']-273)*5/9 + 32
    humidity = result['main']['humidity']
    windspeed = result['wind']['speed']*2.23
    dt = result['dt'] - 5*3600
    print(dt)
    updated_time = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')

    print(str(temperature) + ", " + str(humidity) + "," + str(windspeed))

    context = {}
    context['updated_time'] = updated_time
    context['zipcode'] = zipcode
    context['temperature'] = "%.1f"%temperature
    context['humidity'] = humidity
    context['windspeed'] = "%.1f"%windspeed

    # query all towns where the zip code is zipcode
    # towns = ZipCode.objects.filter(zip=zipcode)
    # context['towns'] = towns


    weather_list = []
    forecast_result = requests.get(url_generator(zipcode, True)).json()

    for weather in forecast_result['list']:
        dt = weather['dt'] -5*3600
        updated_time = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')
        temperature = "%.1f" % ((weather['main']['temp']-273)*5/9 + 32)
        humidity = weather['main']['humidity']
        windspeed = "%.1f" % (weather['wind']['speed']*2.23)
        weather = Weather(updated_time = updated_time, temperature = temperature,humidity = humidity,windspeed = windspeed)
#        weather.save()
        weather_list.append(weather)

    context['weather_list'] = weather_list

    return render(request, "weather/weather_details.html", context)



def url_generator(zipcode, isForecast ):

    # for example
    # http://api.openweathermap.org/data/2.5/weather?zip=10533,us&APPID=2781183c04ce2d6c9f76cd423f747bd2
    url_base = 'http://api.openweathermap.org/data/2.5/'
    slug = ''
    if isForecast:
        slug = 'forecast'
    else:
        slug = 'weather'

    url = url_base + slug + '?'
    appId = '2781183c04ce2d6c9f76cd423f747bd2'

    test_url = url + 'zip=' + zipcode + ',us&APPID=' + appId

    print('the url is ' + test_url)

    return test_url


def show_list(request):


   pass