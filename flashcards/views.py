from django.shortcuts import render

from flashcards.models import Flashcard

# Create your views here.
def card_list(request):
    cards = Flashcard.objects.all()
    return render(request, 'flashcards/card_list.html', {"cards": cards})