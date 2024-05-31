from django.db import models
from .models import Quiz

# Create your models here.
class Answer(models.Model):
    answerId = models.AutoField(primary_key=True)
    quizId = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)

    def _str_(self):
        return self.answer