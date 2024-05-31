from django.shortcuts import render
from django.http import JsonResponse
from .models import Document
from .serializers import DocumentSerializer
from django.utils import timezone
from rest_framework.parsers import MultiPartParser, FormParser
from django.views import View

class DocumentUploadView(View):
    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):
        documentName = request.POST.get('documentName')
        file = request.FILES['file']
        documentPath = f"/path/to/docker/storage/{documentName}"
        
        # Save file to docker path
        with open(documentPath, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        # Save document info to database
        document_data = {
            'documentName': documentName,
            'documentPath': documentPath,
            'createdAt': timezone.now()
        }
        serializer = DocumentSerializer(data=document_data)
        
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "code": 201,
                "documentId": serializer.instance.id,
                "message": "Success upload the file!"
            }
            return JsonResponse(response_data, status=201)
        
        return JsonResponse(serializer.errors, status=400)
