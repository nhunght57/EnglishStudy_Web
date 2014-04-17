from django.shortcuts import render
from django.views import generic
from tracnghiem.models import Question
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

class TracNghiemView(generic.ListView):
    template_name = 'tracnghiem/tracnghiem.html'
    context_object_name = 'list_of_questions'

    def get_queryset(self):
        return Question.objects.all()


def post(request):
    return HttpResponse("<p>You've just submitted<p>")


class ResultView(generic.DetailView):
    template_name = 'tracnghiem/result.html'

    def get_queryset(self):
        return None;