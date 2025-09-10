from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system',"You are a helpful {domain} expert."),
    ('human', "Explain the concept of {concept} in a {style} manner, keeping the explanation {length}.")])

prompts = chat_template.invoke({
    'domain':'AI',
    'concept':'transformers',
    'style':'beginner-friendly',
    'length':'short (1-2 paragraphs)'})

print(prompts)