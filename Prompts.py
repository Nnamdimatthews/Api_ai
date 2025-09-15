from google import genai
import config

client = genai.client(api_key=config.GEMI_API_KEY)

def generate_response(prompt):
    response = client.chat.completions.create(
        model="gemini-2.0-flash", # Change model name as needed
        contents = prompt
    )
    return response.text

def silly_prompt():
    print("Welcome to the AI Prompt Engineering Playground!")
    print("Here, you can experiment with different prompts to see how the AI responds.")
    print("Let's start by crafting a vague prompt, making it more specific, and then adding context.")
    vague_prompt = "Please enter a vague prompt (e.g., 'Tell me about space.')"

    print(vague_prompt)
    vague_response = generate_response(vague_prompt)
    print("V1\nYour vague prompt is:", vague_prompt)

specific_prompt = input("Wow, make your prompt more specific (e.g., 'Tell me about the planets in our solar system'): ")
print("\nYour specific prompt is:", specific_prompt)
specific_response = generate_response(specific_prompt)
print("Response to the specific prompt:", specific_response)

context_prompt = input("\nFinally, add some context to your prompt (e.g., 'As a science teacher, explain the planets in our solar system to a 10-year-old.'): ")
print("\nYour context-rich prompt is:", context_prompt)
context_response = generate_response(context_prompt)
print("Response to the context-rich prompt:", context_response)

print("\nGreat job! You've seen how refining your prompts can lead to more accurate and relevant responses from the AI.")
print("Feel free to experiment with different prompts and see how the AI responds!")
