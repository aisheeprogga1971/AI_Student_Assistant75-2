from openai import OpenAI

client = OpenAI(api_key="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")

def ask_ai(question):
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}]
    )
    return res.choices[0].message.content

def evaluate_writing(text):
    prompt = f"Evaluate this writing and give score + feedback:\n{text}"

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content