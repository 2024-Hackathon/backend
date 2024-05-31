from django.urls import path
from .views import QuizCreateView

urlpatterns = [
    path('quiz/', QuizCreateView.as_view(), name='create-quiz'),
]
