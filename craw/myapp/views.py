from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import HttpResponse

# Create your views here.
# def card_crawling(request):
    

def index(request):
    
    context = {
        
    }
    return render(request,'myapp/index.html',context)