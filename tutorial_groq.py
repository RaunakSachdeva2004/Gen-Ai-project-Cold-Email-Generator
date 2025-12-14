from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model = "llama-3.3-70b-versatile", temperature=0.7)

resp = llm.invoke("WHo was the first perosn in space?")
print(resp.content)