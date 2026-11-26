import asyncio

from langchain.chat_models import init_chat_model
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)
from dotenv import load_dotenv
load_dotenv()


# Groq
groq_model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq",
    temperature=0,
    max_tokens=100,
    timeout=60,
    max_retries=2
)



messages = [
    SystemMessage(
        content="You are a helpful Python tutor."
    ),
    HumanMessage(
        content="What is a Python function?"
    ),
    AIMessage(
        content="A function is a reusable block of code."
    ),
    HumanMessage(
        content="Give me an example."
    ),
]

# response = groq_model.invoke(messages)
# print(response.content)


from langchain_core.messages import HumanMessage, AIMessage

history = [
    HumanMessage(content="My name is Asadullah."),
    AIMessage(content="Nice to meet you, Asadullah."),
    HumanMessage(content="What is my name?"),
]
async def async_model_request():
    response = await groq_model.ainvoke(history)
    print(response.content)

    questions = [
        "What is python?",
        "What is FastAPI?",
        "What is langchain?"
    ]

    response = await groq_model.abatch(questions)
    for message in response:
        print(message.content)

    for chunk in groq_model.stream("Explain AI Agents?"):
        print(chunk.text,end="",flush=True)

asyncio.run(async_model_request())