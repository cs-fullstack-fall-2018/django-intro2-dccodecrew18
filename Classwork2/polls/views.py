from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. Also thius the page where we make functions and pull from them
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def hello_name (request, name):
    return HttpResponse("Hello",name)
def times2 (request, number):
    return HttpResponse("The product times :",(2*number))
def sum (request,num1,num2):
    #for x in range (0,maxnum,2):
       # print("The sum of",num1,"and",num2,"is",(num1+num2))
        return HttpResponse("The sum of num1 and num2 is", (num1+num2 ))
        return HttpResponse("This is working great! Look at console for results !")