from django.conf import settings
from django.shortcuts import render
import requests


def home(request):
    error = None
    if request.method == 'POST':
        url = (f"https://api.openweathermap.org/data/2.5/weather?q={request.POST['place']}&APPID"
               f"={settings.APP_ID}")
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = round(data['main']['temp'] - 273.15, 2)
            return render(request, 'home.html', {
                'temperature': temperature,
                'data': data
            })
        else:
            if not request.POST['place']:
                error = 'Empty!'
            else:
                error = f"Place \"{request.POST['place']}\" not found!<br />Please try again."
    return render(request, 'home.html', {'error': error})
