from openai import OpenAI

def deepseek_chat(prompt: str):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",
            "X-Title": "<YOUR_SITE_NAME>"
        },
        model="deepseek/deepseek-chat",
        messages=[
            {"role": "system", "content": prompt},
        ]
    )

    response = completion.choices[0].message.content

    return response

tts_client = OpenAI(
    api_key="glados-local-no-auth",
    base_url="http://localhost:10203/v1"
)