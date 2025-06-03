import os

import dotenv
from langchain.chains.question_answering.map_reduce_prompt import messages
from langchain.chains.question_answering.map_rerank_prompt import output_parser
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
os.environ["OPENAI_API_KEY"]

# 创建聊天提示词模板
prompt = ChatPromptTemplate.from_template("请讲一个关于{topic}的故事")

model = ChatOpenAI(model="gpt-4")

# 输出解析器
output_parser = StrOutputParser()

# 通过管道链接各个处理步骤创建处理链
chain = prompt | model | output_parser

message = chain.invoke({"topic": "耐克鲨鱼"})

print(message)