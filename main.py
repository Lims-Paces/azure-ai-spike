import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential
from azure.mgmt.quota import QuotaMgmtClient
from dotenv import load_dotenv

load_dotenv()

print('hello world')

client = AzureOpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    azure_endpoint=os.getenv('OPENAI_ENDPOINT'),
    api_version=os.getenv('API_VERSION'),
)

subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
resource_group = "openai-experiment"
location = "eastus"
subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
resource_name='tublian-openai-experiment-2'

credential = DefaultAzureCredential()

# def check_quotas():
#     client = QuotaMgmtClient(
#         credential=DefaultAzureCredential(),
#     )

#     response = client.usages.list(
#         scope=f"subscriptions/{subscription_id}/providers/Microsoft.Quota/locations/eastus",
#     )
#     for item in response:
#         print(item)
    # client = QuotaMgmtClient(
    #     credential=DefaultAzureCredential(),
    # )
    # # scope=f"/subscriptions/{subscription_id}/providers/Microsoft.Compute/locations/{location}/providers/Microsoft.Quota/quotas/{resource_name}"
    # scope = f"/subscriptions/{subscription_id}/providers/Microsoft.Quota/locations/{location}"
    # response = client.quota.get(
    #     resource_name=resource_name,
    #     # scope=f"subscriptions/{subscription_id}/providers/Microsoft.Compute/locations/eastus",
    #     scope=scope
    # )

    # print(response)

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
    # check_quotas()
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







