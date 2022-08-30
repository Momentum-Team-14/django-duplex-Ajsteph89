from pickle import NONE
from django.shortcuts import render, get_object_or_404
import flashcards
from flashcards.models import Flashcard, Subject
from .forms import SubjectForm, FlashcardForm
from django.shortcuts import redirect

# Create your views here.

def list_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'flashcards/list_subject.html', {'subjects': subjects})

def subject_new(request):
    if request.method == "POST":
        subject_form = SubjectForm(request.POST)
        if subject_form.is_valid():
            subject = subject_form.save(commit=False)
            subject.save()
            return redirect('list_subject')
    else:
        subject_form = SubjectForm()
    return render(request, 'flashcards/subject_new.html', {'subject_form': subject_form})


def subject_edit(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        subject_form = SubjectForm(request.POST, instance=subject)
        if subject_form.is_valid():
            subject = subject_form.save(commit=False)
            subject.save()
            return redirect('list_subject')
    else:
        subject_form = SubjectForm(instance=subject)
    return render(request, 'flashcards/subject_edit.html', {'subject_form': subject_form})


def card_questions(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    flashcards = subject.flashcards.all()
    return render(request, "flashcards/card_questions.html", {'flashcards': flashcards, 'subject': subject})


def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect('list_subject')


def card_new(request, pk=None):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        card_form = FlashcardForm(request.POST)
        if card_form.is_valid():
            card = card_form.save(commit=False)
            card.subject = subject
            card.user = request.user
            card.save()
            return redirect('card_questions', pk=pk)
    else:
        card_form = FlashcardForm()
    return render(request, 'flashcards/card_new.html', {'card_form': card_form})


def card_edit(request, pk1, pk2):
    card = get_object_or_404(Flashcard, pk=pk1)
    subject = get_object_or_404(Subject, pk=pk2)
    if request.method == "POST":
        card_form = FlashcardForm(request.POST, instance=card)
        if card_form.is_valid():
            card = card_form.save(commit=False)
            card.subject = subject
            card.user = request.user
            card.save()
            return redirect('card_questions', pk=pk2)
    else:
        card_form = FlashcardForm(instance=card)
    return render(request, 'flashcards/card_edit.html', {'card_form': card_form})


def delete_card(request, pk1, pk2):
    card = get_object_or_404(Flashcard, pk=pk1)
    card.delete()
    subject = get_object_or_404(Subject, pk=pk2)
    return redirect('card_questions', pk=pk2)