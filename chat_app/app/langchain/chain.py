from mongodb import MongoDB
from langchain_openai import ChatOpenAI

#MongoDB 
mongo_connection_string = MongoDB().get_connection_string()

#OpenAI llm
openai_llm = llm = ChatOpenAI( 
    model="gpt-4o",
    temperature=0,
    max_tokens=None, 
    timeout=None, 
    max_retries=2,
)



