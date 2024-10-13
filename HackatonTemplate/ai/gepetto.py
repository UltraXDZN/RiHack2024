import openai
import os


def getTopic(message: str) -> str:
    # Set up the OpenAI API client
    openai.api_key = os.getenv("OPENAI_API_KEY")

    system = "You are an AI topic detector. For a provided text in Croatian language from an online forum post, you will output one of the following topics that best describes that post. The topics are: 'Sport i Zabava', 'Moda i Umjetnost', 'Politika i Društvo', 'Znanost i IT', 'Životni stil', 'Biljke i životinje', 'Interaktivni sadržaj'. Your answer must contain the topics name and nothing else."
    model_name = "gpt-3.5-turbo"

    # Define the system message and user message
    system_message = {
        "role": "system",
        "content": system,
    }
    user_message = {
        "role": "user",
        "content": message,
    }

    # Create the prompt
    messages = [system_message, user_message]

    # Send the prompt to the OpenAI API
    response = openai.chat.completions.create(model=model_name, messages=messages)

    # Print the response
    topic = response.choices[0].message.content

    return topic
