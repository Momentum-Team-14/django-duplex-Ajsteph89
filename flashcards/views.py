from django.shortcuts import render, get_object_or_404
import flashcards
from flashcards.models import Flashcard, Subject
from .forms import SubjectForm
from django.shortcuts import redirect

# Create your views here.

def list_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'flashcards/list_subject.html', {'subjects': subjects})

def subject_new(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.save()
            return redirect('list_subject')
    else:
        form = SubjectForm()
    return render(request, 'flashcards/subject_new.html', {'form': form})



def card_questions(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    flashcards = subject.flashcards.all()
    return render(request, "flashcards/card_questions.html", {'flashcards': flashcards})


def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect('list_subject')