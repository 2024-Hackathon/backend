# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
import pdfplumber
import openai
from django.conf import settings

import openai
from dotenv import load_dotenv
import os
import pdfplumber

load_dotenv()  # 환경 변수 설정

# OpenAI API 키 설정
openai.api_key = os.getenv('GPT_KEY')

class GenerateQuestionsView(APIView):
    def post(self, request, *args, **kwargs):
        # Get the PDF file from the request
        pdf_file = request.FILES.get('pdf_file')
        if not pdf_file:
            return Response({'error': 'PDF file is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Read text from the PDF file
            with pdfplumber.open(pdf_file) as pdf:
                first_page = pdf.pages[0]
                text = first_page.extract_text()

            # Use the extracted text to generate quiz questions
            response = self.generate_questions(text)
            return Response({'questions': response}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def generate_questions(self, text):
        # Here you can add the API key setup if not globally set in settings
        # openai.api_key = settings.OPENAI_API_KEY

        prompt = f"Based on the following text, create three quiz questions with answers:\n\n{text}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )
        return response.choices[0].message["content"]

# Ensure the OpenAI API key is set in your settings.py
