from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.urls import reverse
from .models import Question
from random import choice
import time
from matplotlib.colors import cnames
hexcolors=list(cnames.values())

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # first get the choice
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'You did not select a choice, mate.', })
    else:
        selected_choice.votes = F('votes') + 1 # eliminate race conditions!
        selected_choice.save() # save
        selected_choice.refresh_from_db()
        # Always return an HttpResponse Redirect after sccessfully dealing with POST data
        # this prevents data from being posted twice if a user hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

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
    #time.sleep(60)
    return HttpResponse(holyshit)
