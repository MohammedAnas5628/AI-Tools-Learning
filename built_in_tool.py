from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load API keys
load_dotenv()

# Initialize Search Tool
search_tool = TavilySearchResults(max_results=5)

# Initialize LLM
llm = ChatMistralAI(model="mistral-small-2506")

# Prompt
prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Using the search results below, answer the user's question clearly.

Question:
{question}

Search Results:
{search_results}
""")

chain = prompt | llm | StrOutputParser()

# User Query
query = input("Enter your query: ")

# Search the web
search_results = search_tool.run(query)

# ------------------------------
# Display the websites visited
# ------------------------------
print("\n========== Websites Visited ==========\n")

for i, website in enumerate(search_results, start=1):
    print(f"{i}. {website['title']}")
    print(f"   {website['url']}\n")

# ------------------------------
# Generate Final Answer
# ------------------------------
response = chain.invoke({
    "question": query,
    "search_results": search_results
})

print("\n========== Final Answer ==========\n")
print(response)