from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_subject, name='list_subject'),
    path('subject/new/', views.subject_new, name='subject_new'),
    path('subject/questions/>', views.questions, name='questions')
]