from django.shortcuts import render
from django.views import generic
from tracnghiem.models import Question
# Create your views here.

class TracNghiemView(generic.ListView):
    template_name = 'tracnghiem/tracnghiem.html'
    context_object_name = 'list_of_questions'

    def get_queryset(self):
        return Question.objects.all()