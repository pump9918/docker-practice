import os
import requests
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()


def get_chatgpt_response(message):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Authorization': f'Bearer {openai_api_key}',
            'Content-Type': 'application/json'
        },
        json={
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': message}]
        }
    )
    return response.json()
