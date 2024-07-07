import os
from groq import Groq

# Initialize the client with the API key
client = Groq(
    api_key=os.environ.get("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"),
)

api_key = "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"

while True:
    # Prompt the user for input
    TEXTIN = input("Enter Prompt: ")

    # Create chat completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You only respond in python code no matter what",
            },
            {
                "role": "user",
                "content": TEXTIN,
            }
        ],
        model="llama3-8b-8192",
    )

    # Get the response from the chat completion
    response = chat_completion.choices[0].message.content

    # Print the response
    print("AI Response:\n", response)

    # Parse and execute the response as Python code
    try:
        exec(response)
    except Exception as e:
        print(f"Error executing AI code: {e}")
