from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Fucking brain!</h1> \
    Hello! You're at the polls index page. <br> \
    A product of my fucking mind. <br> \
    What a piece of shit...")
def fuck(request):
    return HttpResponse("<h1>Fuck Fuck Fuck a Duck</h1> \
    <h2> Screw a kangaroo </h2> \
    <h3> Finger bang an orangatan </h3> \
    <h4> Orgy at the zoo! </h4>")
