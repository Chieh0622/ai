# 參考 https://github.com/ccc112b/py2cs/blob/master/03-%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/A4-groq/hello/groqChat.py
import os
import sys
from groq import Groq

client = Groq(
    api_key="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",
)

def chat():   
    while True:
        question = input("問題: ") + "，中文回答"

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
                ],
                model="llama3-8b-8192",
            )
        
        response = chat_completion.choices[0].message.content
        print("groq:", response)

if __name__ == "__main__":
    chat()
