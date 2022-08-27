from django.shortcuts import render
import flashcards
from flashcards.models import Flashcard, Subject
from .forms import SubjectForm
from django.shortcuts import redirect

# Create your views here.

def base(request):
    return render(request, 'flashcards/base.html')

def list_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'flashcards/list_subject.html', {"subjects": subjects})

def subject_new(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.save()
            return redirect('base')
    else:
        form = SubjectForm()
    return render(request, 'flashcards/subject_edit.html', {'form': form})