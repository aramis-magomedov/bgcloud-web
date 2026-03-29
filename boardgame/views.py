from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {'title': "Тест стилей"}
    return render(request, "boardgame/index.html", data)

def categories(request, cat_id):
    return HttpResponse(f"<h1 >Настолки по категориям {cat_id}</h1>")