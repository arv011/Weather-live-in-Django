from django.shortcuts import render
import requests
from .forms import weatherform
# Create your views here.
def weather_response(weather):
    try:
        name = weather['name']
        country = weather['sys']['country']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']

        # final_str = 'City: %s \nCountry: %s \nConditions: %s \nTemperature (°F): %s' % (name,country, desc, temp)
        final_str = {'Name':name, 'country':country, 'dec':desc, 'temp': temp, 'humidity':humidity}
    except:
        final_str = 'problem! cannot retrive the data please enter correct information'
    return final_str

def get_weather(city):
    weather_key= '61ee9339d9dfce23e98fb66ae8637bed'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'metric'}
    response=requests.get(url,params=params)
    weather_current=response.json()
    return weather_response(weather_current)
    

def getdataweather(request):
    form = weatherform()
    x = False
    rem = {'forms':form, 'sig':x}
    if request.method == 'POST':
        x = True
        form = weatherform(request.POST)
        if form.is_valid():
            pincode = form.cleaned_data['pincode']
            city_name = form.cleaned_data['city']
            print(city_name)
            if pincode == '':
                rem['weather'] = get_weather(city_name)
            if city_name == '':
                rem['weather'] = get_weather(pincode)
            if (city_name == '') and (pincode == ''):
                rem['weather'] = 'Please Insert city or pincode'
            else:
                rem['weather'] = get_weather(city_name)
        rem['sig']=x
    return render(request,'home.html', rem)
    
    