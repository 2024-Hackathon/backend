from django.shortcuts import render
from django.http import JsonResponse
from .models import Quiz
from .serializers import QuizSerializer
from django.views import View
from rest_framework import status
from rest_framework.parsers import JSONParser

## 요청 받아 처리 
class QuizCreateView(View):
    def post(self, request):
         # request.body를 JSON으로 파싱
        data = JSONParser().parse(request)
        
        # 'documentsId'와 'quiz' 데이터를 가져옴
        documents_id = data.get('documentsId', None)
        quiz_data = data.get('quiz', {})
        
        # 데이터가 유효한지 확인
        if not documents_id or not quiz_data:
            return JsonResponse({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        
        # QuizSerializer를 사용하여 데이터 검증 및 저장
        quiz_serializer = QuizSerializer(data=quiz_data)
        if quiz_serializer.is_valid():
            quiz_serializer.save()
            response_data = {
                "code": 201,
                "message": "질문과 답을 생성했습니다.",
                "quizId": quiz_serializer.instance.id
            }
            return JsonResponse(response_data, status=status.HTTP_201_CREATED)
        
        return JsonResponse(quiz_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
