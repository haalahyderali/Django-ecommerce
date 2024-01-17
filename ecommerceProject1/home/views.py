from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def demo(request):
    return redirect('/shop')