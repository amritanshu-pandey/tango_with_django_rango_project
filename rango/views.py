from django.shortcuts import render
#from django.http import HttpResponse
from rango.models import Category


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories':category_list}
    return render(request,"rango/index.html",context_dict)
    #return HttpResponse("Rango says hey there world!<br><a href='/rango/about/'>About</a>")

def about(request):
    context_dict = {"message":"Here is the about page!!"}
    #return HttpResponse("Rango says here is the about page!<br><a href='/rango/'>Rango</a>")
    return render(request, "rango/about.html", context_dict)

