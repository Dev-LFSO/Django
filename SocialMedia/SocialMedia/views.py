from django.shortcuts import render
from datetime import datetime

# Create your views here.

def home(request):
    #news = GoogleNews(lang='pt')
    #news.enableException(True)
    #news_list = news.get_news('APPLE')
    #print(news_list)
    return render(request, 'home.html')

