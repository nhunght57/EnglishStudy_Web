# This file is to generate the html page response

# The get_object_or_404() function takes a Django model as its first argument
# and an arbitrary number of keyword arguments, which it passes to the get()
# function of the modelâ??s manager. It raises Http404 if the object doesnâ??t exist.
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views import generic
#from django.template import RequestContext, loader

from polls.models import Question, Choice

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'all_question_list'

    def get_queryset(self):
        # Return questions (not including those one from future)
        # return Question.objects.all()
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        # if the question has publish date in the future then exclude it
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def index(request):
#     template = 'polls/index.html'
#
#     all_question_list = Question.objects.all()
#     context = {'all_question_list': all_question_list}
#     #response = ', '.join([p.question_text for p in all_question_list])
#
#     #return HttpResponse('<h2>Đờ mờ</h2>')
#     return render(request, template, context)
#
# def detail(request, question_id):
#     template = 'polls/detail.html'
#
#     # The following code uses try/except to check for an question id
#     # try:
#     #     question = Question.objects.get(pk = question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404
# 
#     # But this can be used instead
#     # get_object_or_404 raises Http404 if the object doesn't exist
#     question = get_object_or_404(Question, pk=question_id)
#
#     return render(request, template, {'question':question})
#
# def results(request, question_id):
#     template = 'polls/results.html'
#     question = get_object_or_404(Question, pk=question_id)
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response %question_id)
#     return render(request, template, {'question': question})

def vote(request, question_id):
    template = 'polls/detail.html'

    p = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, template, {
            'question': p,
            'error_message': "You didn't select a choice.",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))