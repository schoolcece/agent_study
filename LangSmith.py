import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

dotenv.load_dotenv()

prompt = PromptTemplate.from_template("{flower}的花语是？")
model = OpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

result = chain.invoke({"flower": "鹤望兰"})
print(result)