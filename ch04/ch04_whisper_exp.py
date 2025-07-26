from openai import OpenAI	
import os
from dotenv import load_dotenv
# This script loads environment variables from a .env file
load_dotenv()
# os.getenv() 함수를 이용해 API 키를 변수에 저장합니다.
openai_api_key = os.getenv("OPENAI_API_KEY")
# API 키 입력
client = OpenAI(api_key=openai_api_key)

# 녹음 파일 열기
audio_file = open("speech.mp3", "rb")

# whisper 모델에 음원 파일 넣기
transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file, response_format="text")

# 결과 보기
print(transcript)