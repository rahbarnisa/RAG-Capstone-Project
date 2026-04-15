#retrieval
def retrieve_documents (query, db, k=3):
    results = db.similarity_search(query, k=k)
    return results

# Context + Citation builder
def build_context(docs):
    context = ""
    sources = []

    for doc in docs:
        context += doc.page_content + "\n\n"

        source_info = f"{doc.metadata['source']} - page {doc.metadata['page']}"
        if source_info not in sources:
           sources.append(source_info)

    return context, sources

#LLM answer generator
from openai import OpenAI
from src.prompts import SYSTEM_PROMPT

client = OpenAI()

#def generate_answer(query, context, sources):
    #response = client.chat.completions.create(
        #model="gpt-4o-mini",
        #messages=[
           # {"role": "system", "content": SYSTEM_PROMPT},
           # {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
       # ]
 #   )
    
    #answer = response.choices[0].message.content

    #final_answer = answer + "\n\nSources:\n" + "\n".join(sources)

   # return final_answer

#Update Answer Generator
#Now modify generate_answer in:

#def generate_answer(query, context, sources, memory):
    #history_messages = format_chat_history(memory)

    #response = client.chat.completions.create(
        #model="gpt-4o-mini",
        #messages=[
            #{"role": "system", "content": SYSTEM_PROMPT},
            #*history_messages,
           # {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
       # ]
   # )

    #answer = response.choices[0].message.content

   # final_answer = answer + "\n\nSources:\n" + "\n".join(sources)

    #return final_answer

#Format Memory for LLM
#We need to convert memory into messages.
# So we Add this to rag_pipeline.py:
def format_chat_history(memory):
    messages = []

    for item in memory:
        messages.append({"role": "user", "content": item["user"]})
        messages.append({"role": "assistant", "content": item["bot"]})

    return messages

#Ticket github modification code
tools = [
    {
        "type": "function",
        "function": {
            "name": "create_support_ticket",
            "description": "Create a support ticket when user has an issue",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "description": {"type": "string"}
                },
                "required": ["title", "description"]
            }
        }
    }
]

#updated answer_generator for ticketing
import json
from src.ticketing import create_github_issue

def generate_answer(query, context, sources, memory):
    history_messages = format_chat_history(memory)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            *history_messages,
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
        ],
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    # If model decides to call function
    if message.tool_calls:
        tool_call = message.tool_calls[0]

        if tool_call.function.name == "create_support_ticket":
            args = json.loads(tool_call.function.arguments)

            issue_url = create_github_issue(
                title=args["title"],
                description=args["description"]
            )

            return f"✅ Support ticket created: {issue_url}"

    # Normal response
    answer = message.content
    final_answer = answer + "\n\nSources:\n" + "\n".join(sources)

    return final_answer