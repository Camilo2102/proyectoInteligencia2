from openai import OpenAI

client = OpenAI(
    api_key="sk-proj-AG6ODNGho1SBTgI6hkDtT3BlbkFJmFJJKKJLW08Z5sVt1kn6",
)

def use_model(propmt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": propmt
            }
        ],
        model="gpt-3.5-turbo",
    )
    response = chat_completion.choices[0].message.content

    return response