import os

import dotenv
from openai import OpenAI

dotenv.load_dotenv()
os.environ["OPENAI_API_KEY"]
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_format={"type": "json_object"},
    messages = [
        {"role": "system", "content": "你是一个帮助用户了解鲜花信息的智能助手，并能够输出JSON格式的内容"},
        {"role": "user", "content": "母亲节送什么花最好？"}
    ]
)

# print(response)

print(response.choices[0].message.content)