from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4")

result = model.invoke("What is the capital of India")

print(result)

# This time it returns json hence we mmust return result.content

print(result.content)