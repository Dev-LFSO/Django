from django.shortcuts import render
from datetime import datetime
from GoogleNews import GoogleNews

# Create your views here.

def home(request):
    googlenews = GoogleNews(period='1d')
    today = datetime.today().strftime('%d/%m/%Y')
    googlenews.set_time_range('01/01/2024', today)
    googlenews.search('world')
    news_list = googlenews.result()[0:9]
    for news in news_list:
        try:
            news['datetime'] = news['datetime'].strftime('%H:%M - %d/%m/%Y')
        except AttributeError:
            pass
    return render(request, 'home.html' , {'news_list':news_list})

