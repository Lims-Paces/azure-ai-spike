import os
from openai import AzureOpenAI

from dotenv import load_dotenv
load_dotenv()

print('hello world')

client = AzureOpenAI(
    api_key = os.getenv('OPENAI_API_KEY'),
    azure_endpoint = os.getenv('OPENAI_ENDPOINT'),
    api_version = os.getenv('API_VERSION'),
)

messages = [
        {
            "role": "user",
            "content": "what is python",
        }
    ]

def create_chatbot(message):
    chat_completion = client.chat.completions.create(
    model="Tublian-gpt4o-deployment-test",
    messages=message
    )
    return chat_completion.choices[0].message.content


def main():
    print("Ask me questions, I am here to give answers")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        
        messages = [
            {
                "role": "user",
                "content": user_input,
            }
        ]
        
        response = create_chatbot(messages)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()





