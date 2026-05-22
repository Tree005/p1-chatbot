import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

url = "https://api.deepseek.com/v1/chat/completions"

#请求头

headers = {
    "Content-Type":"application/json",
    "Authorization":"Bearer " + api_key
}

#请求体
body = {
    "model":"deepseek-chat",
    "messages":[
        {"role":"user","content":"你好"} 
    ]
}
# 发请求
response = requests.post(url,json=body,headers=headers)

#打印原始返回
data = response.json()
print(data)
reply = data["choices"][0]["message"]["content"]
print("AI 回复：", reply)



































