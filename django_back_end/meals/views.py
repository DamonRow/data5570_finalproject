from django.shortcuts import render
from django.http import HttpResponse

def meal_search_view(request):
    return HttpResponse("This is the meal search page!")


# Create your views here.
