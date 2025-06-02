import os

from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool
from langchain_openai import OpenAI
from langchain_community.utilities import SerpAPIWrapper
import dotenv

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"]
os.environ["SERPAPI_API_KEY"]

prompt = hub.pull("hwchase17/react")
print(prompt)

llm = OpenAI()

search = SerpAPIWrapper()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="当模型没有相关知识时，用于搜索相关知识"
    ),
]

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke({"input": "当前Agent最新研究进展是什么"})