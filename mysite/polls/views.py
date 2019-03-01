from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>A Simple Poll App!</h1> \
    Hello! You're at the polls index page. <br>")

def zoofun(request, **kwargs):

    html_text = "<h1>Fuck Fuck Fuck a Duck</h1> \
    <h2> Screw a kangaroo </h2> \
    <h3> Finger bang an orangatang </h3> \
    <h4> Orgy at the zoo! </h4>"

    if kwargs['censor']:
        html_text = html_text.replace("Screw", "*****")
        html_text = html_text.replace("Fuck Fuck Fuck", "**** **** ****")
        html_text = html_text.replace("Finger bang", "****** ****")
        html_text = html_text.replace("Orgy", "****")
    return HttpResponse(html_text)
