from django.shortcuts import render
from django.views import generic
from tracnghiem.models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

class TracNghiemView(generic.ListView):
    template_name = 'tracnghiem/tracnghiem.html'
    context_object_name = 'list_of_questions'

    def get_queryset(self):
        return Question.objects.all()

def change_user_score(user, score):
    user.profile.score_of_the_last_test = score
    user.profile.total_score += score
    user.profile.save()


def post(request):
    #return HttpResponse("<p>You've just submitted<p>")
    QUESTION = 'question'
    score = 0
    count_questions = 1
    question = QUESTION + str(count_questions)

    while question in request.POST:
        if Choice.objects.get(id=request.POST[question]).is_correct is True:
            score = score + 1
        count_questions = count_questions + 1
        question = QUESTION + str(count_questions)

    change_user_score(request.user,score)
    return HttpResponse("<p> your score  at this test is " +
                        str(score) +
                        " and your total... is "+str(request.user.profile.total_score) + "</p>")



class ResultView(generic.DetailView):
    template_name = 'tracnghiem/result.html'

    def get_queryset(self):
        return None;