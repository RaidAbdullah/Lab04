from django.shortcuts import render
from django.http import HttpResponse

tax = 0.15
# Create your views here.
def index (request):
    return render(request,'tax/index.html')

def calc_tax (request , number):
    price = number + (number * tax)
    return HttpResponse(f"The price after the tax is {price}")

def tax_rate (request):
    return render(request,'tax/tax_rate.html',{'tax':tax})


