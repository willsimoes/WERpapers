from django.http import HttpResponse
from django.shortcuts import render

context = {}

def index(request):
    return render(request, 'werpapers_manager/index.html', context)
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
