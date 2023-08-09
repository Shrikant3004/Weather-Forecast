from django.shortcuts import render,HttpResponse
from datetime import datetime
import requests
# Create your views here.
url = 'http://api.openweathermap.org/data/2.5/weather?appid=d512d72c5f64df8a32b48b90a281a3b5&q=Bhubaneswar'
result = requests.get(url).json()

def index(request):
    date = {'date': datetime.today().date(),
            'weather': result['weather'][0]['main'],
            'temp':round(result['main']['temp']-273,1),
            'cloudy':result['clouds']['all'],
            'humid':result['main']['humidity'],
            'wind':result['wind']['speed'],
            'feels_like':round(result['main']['feels_like']-273,1)
           } 
    return render(request,'index.html',date)
def about(request):
    return render(request,'about.html')
def forecast(request):
    return render(request,'forecast.html')