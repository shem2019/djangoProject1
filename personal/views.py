from django.shortcuts import render
from personal.models import Question
#create views here
def home_screen_view(request):

   # list_of_values=[]
   # list_of_values.append("first entry")
    #list_of_values.append("second entry")
    #list_of_values.append("Third entry")
    #list_of_values.append("fourth entry")
    #list_of_values.append("fifth entry")

    context = {}
    questions= Question.objects.all()
    context['questions']=questions
    return render(request,"personal/Home.html",context)


# Create your views here.
