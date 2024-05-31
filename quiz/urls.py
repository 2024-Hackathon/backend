from django.urls import path
from .views import *

urlpatterns = [
    path('', GenerateQuestionsView.as_view(), name='generate-questions'),
]
