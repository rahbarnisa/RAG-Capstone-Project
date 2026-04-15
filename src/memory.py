chat_history = []

def add_to_memory(user_input, bot_response):
    chat_history.append({
        "user": user_input,
        "bot": bot_response
    })

def get_memory():
    return chat_history