from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Document
import os

@api_view(['POST'])
def upload_document(request):
    document_name = request.data.get('documentName')
    document_path = request.data.get('documentPath')
    created_at = request.data.get('createdAt')

    if not (document_name and document_path and created_at):
        return Response({"message": "All fields are required!"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    document = Document.objects.create(document_name=document_name, document_path=document_path, created_at=created_at)
    return Response({"documentId": document.id, "message": "Success upload the file!"}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_document(request, document_id):
    try:
        document = Document.objects.get(id=document_id)
        # 여기서는 단순히 파일 경로를 리턴할 것입니다. 만약 PDF 내용을 가져오려면 해당 경로의 파일을 읽어야 합니다.
        return Response({
            "status": status.HTTP_200_OK,
            "documentId": document.id,
            "documentName": document.document_name,
            "documentPath": document.document_path
        })
    except Document.DoesNotExist:
        return Response({"message": "Document not found"}, status=status.HTTP_404_NOT_FOUND)