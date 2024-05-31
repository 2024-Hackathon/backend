import openai
from dotenv import load_dotenv
import os
import pdfplumber

load_dotenv()  # 환경 변수 설정

# OpenAI API 키 설정
openai.api_key = os.getenv('GPT_KEY')

def read_pdf(file_path):
    # PDF 파일 열기
    with pdfplumber.open(file_path) as pdf:
        first_page = pdf.pages[0]  # 첫 페이지 읽기
        text = first_page.extract_text()  # 텍스트 추출
    return text

def get_completion(prompt, model="gpt-4"):
    # 대화 메시지 생성
    messages = [{"role": "user", "content": prompt}]
    # OpenAI의 대화 생성 API 호출
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    # 생성된 대화 반환
    return response.choices[0].message["content"]

# 사용자의 홈 디렉토리 경로를 얻기
home_path = os.path.expanduser('~')
# PDF 파일 경로 설정
file_path = os.path.join(home_path, 'desktop', 'test.pdf')

# PDF에서 텍스트 읽기
pdf_text = read_pdf(file_path)
# 읽은 텍스트를 프롬프트로 사용하여 대화 생성
response = get_completion(pdf_text)

def generate_questions(text, model="gpt-4"):
    # 질문 생성을 위한 프롬프트 준비
    prompt = f"Based on the following text, create three quiz questions with answers:\n\n{text}"
    # 질문 생성 요청
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    # 생성된 질문 반환
    return response.choices[0].message["content"]

# 읽은 텍스트를 기반으로 퀴즈 질문 생성
quiz_questions = generate_questions(response)
# 생성된 퀴즈 질문 출력
print(quiz_questions)
# # 생성된 대화 출력
# print(response)
