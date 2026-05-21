import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI(
    api_key=os.getenv('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com/v1"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role":"system","content":"You are a helpful assistant"},
        {"role":"user","content":"Hello"}
    ],
    stream=False,
    #reasoning_effort="high",
    #extra_body={"thinking":{"type":"enabled"}}
)
raw_answer = response.choices[0].message.content
print("原始回答：", raw_answer)
