from django.db import models

# Create your models here.
class Quiz(models.Model):
    quizId = models.AutoField(primary_key=True, null=False)
    quizTitle = models.CharField(max_length=200, null=False)
    correctAnswer = models.CharField(max_length=150, null=False)
    solution = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.quizId
