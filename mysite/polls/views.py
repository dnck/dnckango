from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question
from random import choice
from matplotlib.colors import cnames
hexcolors=list(cnames.values())

# old index
# def index(request):
#     return HttpResponse("<h1>A Simple Poll App!</h1> \
#     Hello! You're at the polls index page. <br>")

# second index
# def index(request):
#     latest_question_list = Question.objects.order_by('pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {'latest_question_list': latest_question_list, }
#     return HttpResponse(template.render(context, request))
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     #return HttpResponse(output)

# short index using shortcuts
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # render takes the request, a template, and a context
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist!")
    return render(request, 'polls/detail,html', {'question': question})
    #return HttpResponse("You're looking at question {}".format(question_id))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("You're looking at results for question {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("You're voting for question {}".format(question_id))

# This function demonstrates the use of kwargs in the paths or urlpatterns in the polls app
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

# This function demonstrates some silly stuff with color in an html response
def holyshit(request):
    holyshit=''
    for x in range(256):
        holyshit = holyshit+'<h1 style="color:{}">Holy shit!</h1>'.format(choice(hexcolors))
    return HttpResponse(holyshit)
