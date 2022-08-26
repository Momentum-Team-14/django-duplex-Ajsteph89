from django.contrib.auth.models import AbstractUser as BaseUser
from django.db import models

# Create your models here.
class User(BaseUser):
    pass


class Subject(models.Model):
    subject = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.subject}'

class Flashcard(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name= 'flashcards')
    question = models.TextField()
    answer = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'flashcards')

    def __str__(self):
        return f'{self.question}, {self.answer}'
