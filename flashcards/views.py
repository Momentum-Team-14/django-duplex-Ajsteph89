from django.shortcuts import render

from flashcards.models import Flashcard, Subject

# Create your views here.

def list_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'flashcards/list_subject.html', {"subjects": subjects})