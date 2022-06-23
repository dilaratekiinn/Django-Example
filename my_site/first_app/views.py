from curses.ascii import HT
from pydoc_data.topics import topics
from unittest import result
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls import reverse
# Create your views here.

def simple_view(request):
     return render (request,'first_app/example.html') #.html
      

