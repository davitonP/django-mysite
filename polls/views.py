from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Question, Choice
from django.views import generic
from django.utils import timezone

# Create your views here.
# def index(request):
#     last_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'last_question_list': last_question_list,
#     }
#     output = ', '.join([q.question_text for q in last_question_list])
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404(f'Question does not exist, Im sorry. {question_id}')
#     return render(request, 'polls/detail.html', {'question': question})

#     return HttpResponse(f'You are looking at question {question_id}.')

# def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})
#     # response = f'You are looking at the results of question {question_id}.'
#     # return HttpResponse(response)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
      selected_choice = question.choice_set.get(pk=request.POST[ "choice"])
    except (KeyError, Choice.DoesNotExist):
      return render (
          request,
          "polls:details.html",
          {
              "question": question,
              "error_message": "You didn't select a choice. :P" 
          }
      )
    else:
      selected_choice.votes += 1
      selected_choice.save()

      return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
      
    #   print('An exception occurred')
    # return HttpResponse(f'You are voting on question {question_id}.')

def new_question(request):
   new_question = request.POST['question']
   question = Question(question_text=new_question,pub_date = timezone.now() )
   question.save()
   return HttpResponseRedirect(reverse("polls:index"))

def new_choice(request):
   pk = request.POST['question_id']
   question = get_object_or_404(Question, pk=pk)
   
   choice_text = request.POST['choice']
   choice = Choice(question=question, choice_text=choice_text, votes=0)
   choice.save()

   return HttpResponseRedirect(reverse("polls:detail", args=(pk,)))
      

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

