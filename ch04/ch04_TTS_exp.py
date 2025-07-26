# -*- coding: utf-8 -*-
from openai import OpenAI
import os
from dotenv import load_dotenv
# This script loads environment variables from a .env file
load_dotenv()
# os.getenv() 함수를 이용해 API 키를 변수에 저장합니다.
openai_api_key = os.getenv("OPENAI_API_KEY")
# API 키 입력
client = OpenAI(api_key=openai_api_key)

# 생성할 파일명
speech_file_path = "speech.mp3"

# 한글 텍스트를 UTF-8로 명시적으로 인코딩
text_to_speech = "오늘은 사람들이 좋아하는 것을 만들기에 좋은 날입니다!"

# 스트리밍 응답을 사용하여 파일 저장 (권장 방법)
with client.audio.speech.with_streaming_response.create(
    model="tts-1",
    voice="alloy",
    input=text_to_speech,
) as response:
    response.stream_to_file(speech_file_path)

print(f"음성 파일이 '{speech_file_path}'로 저장되었습니다.")