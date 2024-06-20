# 參考 https://github.com/LeeYi-user/ai/blob/master/homework/10/react.py
import os
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq

os.environ["TAVILY_API_KEY"] = "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"

tools = [TavilySearchResults(max_results=1)]

prompt = hub.pull("hwchase17/react")

llm = ChatGroq(api_key="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")

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

input_data = {
    "input": "太武山多高? 用中文回答"
}

response = agent_executor.invoke(input_data)

print("Response:", response)
