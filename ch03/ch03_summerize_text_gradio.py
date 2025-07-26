##### 기본 정보 불러오기 ####
# Gradio 패키지 추가
import gradio as gr
# OpenAI 패키지 추가
import openai
import os
from dotenv import load_dotenv

# This script loads environment variables from a .env file
load_dotenv()
# os.getenv() 함수를 이용해 API 키를 변수에 저장합니다.
openai_api_key = os.getenv("OPENAI_API_KEY")

##### 기능 구현 함수 #####
def askGpt(prompt, apikey):
    client = openai.OpenAI(api_key=apikey)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    gptResponse = response.choices[0].message.content
    return gptResponse

def summarize_text(text):
    """텍스트를 요약하는 함수"""
    if not text.strip():
        return "요약할 텍스트를 입력해주세요."
    
    if not openai_api_key:
        return "OpenAI API 키가 설정되지 않았습니다."
    
    prompt = f'''
**Instructions** :
- You are an expert assistant that summarizes text into **Korean language**.
- Your task is to summarize the **text** sentences in **Korean language**.
- Your summaries should include the following :
    - Omit duplicate content, but increase the summary weight of duplicate content.
    - Summarize by emphasizing concepts and arguments rather than case evidence.
    - Summarize in 3 lines.
    - Use the format of a bullet point.
-text : {text}
'''
    
    try:
        result = askGpt(prompt, openai_api_key)
        return result
    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"

##### 메인 함수 #####
def main():
    # Gradio 인터페이스 생성
    with gr.Blocks(title="📃요약 프로그램") as demo:
        gr.Markdown("# 📃요약 프로그램")
        gr.Markdown("---")
        
        with gr.Row():
            with gr.Column():
                text_input = gr.Textbox(
                    label="요약할 글을 입력하세요",
                    placeholder="요약하고 싶은 텍스트를 여기에 입력하세요...",
                    lines=10,
                    max_lines=20
                )
                
                summarize_btn = gr.Button("요약", variant="primary")
                
            with gr.Column():
                output = gr.Textbox(
                    label="요약 결과",
                    lines=8,
                    max_lines=15,
                    interactive=False
                )
        
        # 버튼 클릭 이벤트 연결
        summarize_btn.click(
            fn=summarize_text,
            inputs=text_input,
            outputs=output
        )
        
        # Enter 키로도 실행 가능
        text_input.submit(
            fn=summarize_text,
            inputs=text_input,
            outputs=output
        )
    
    # 인터페이스 실행
    demo.launch(
        share=False,
        server_name="127.0.0.1",
        server_port=7860
    )

if __name__ == "__main__":
    main()
