from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question, Suggestion
from django import forms

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions (not including those published in the future). """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        
    

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published et.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# class SuggestionView(generic.DetailView):
#     model = Suggestion
#     # def 
#     # return(HttpResponse("At suggestions"))
#     template_name = 'polls.suggestion.html'

def suggestion(request):
    suggestion_list = Suggestion.objects.all()
    # response = "You're looking at the suggestions"
    # return HttpResponse(response)
    context = {'suggestion_list': suggestion_list,
    'form': SuggestionForm}
    return render(request, 'polls/suggestion.html', context)

def addSuggestion(request):
    # if(request.method == 'Suggestion'):
    if request.POST.get('suggestion_text'):
        new_suggestion = Suggestion()
        new_suggestion.suggestion_text = request.POST.get('suggestion_text')
        new_suggestion.save()
        suggestion_list = Suggestion.objects.all()
        context = {'suggestion_list': suggestion_list,
        'form': SuggestionForm}

        return render(request, 'polls/suggestion.html', context)
    else:
        return render(request, 'polls/suggestion.html')


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ('suggestion_text',)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


# # def index(request):
# #     return HttpResponse("Hello, world. You're at the polls index.")


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
    
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")

#     # return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', { 'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


    # return HttpResponse("You're voting on question %s." % question_id)

# def suggest(request):
#     suggestion = get_object_or_404(Suggestion)
#     try:
