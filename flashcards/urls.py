from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_subject, name='list_subject'),
    path('subject/new/', views.subject_new, name='subject_new'),
    path('delete_subject/<int:pk>', views.delete_subject, name='delete_subject'),
    path('card_questions/<int:pk>', views.card_questions, name='card_questions'),
    path('flashcard/new/<int:pk>', views.card_new, name='card_new'),
]