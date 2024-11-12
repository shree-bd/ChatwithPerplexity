import requests

API_KEY = "YOUR_PERPLEXITY_API_KEY"

def chat_with_perplexity(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "prompt": prompt,
        "model": "perplexity-pro"  # Adjust the model if needed
    }
    response = requests.post("https://api.perplexity.ai/completions", headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["text"].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_perplexity(user_input)
        print("Chatbot:", response)
