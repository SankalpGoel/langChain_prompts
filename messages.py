from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "moonshotai/Kimi-K2-Instruct-0905",   
    task = "text-generation"
)   

model = ChatHuggingFace(llm=llm)

