from django.urls import path
from .views import upload_document, get_document

urlpatterns = [
    path('upload/', upload_document, name='upload_document'),
    path('upload/<int:document_id>/', get_document, name='get_document'),
]