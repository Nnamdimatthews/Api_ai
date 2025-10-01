from google import genai
from google.genai import types
import config

client =  genai.Client(api_key=config.API_KEY)

def generate_text(prompt, temperature=0.3):
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        cofig_params = types.Generate.ContentConfig(temperature=temperature)
        response = client.generate_content(
            model="gemini-2.0-flash",
            contents=contents,
            config=cofig_params
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    
def run_activity():
    catergory = input("Enter a category (e.g., fruit, city, animal): ")
    items = input(f"Enter a specific {catergory}: ")

    print("\n--- Zero-Shot ---")
    zero_shot_prompt = f"Is {items} a {catergory}? Answer yes or no."
    print(f"Prompt: {zero_shot_prompt}")
    print("Response:", generate_text(zero_shot_prompt))

    print("\n--- One-Shot ---")
    one_prompt = f"""Determine if the following belongs to the category.

Example:
Category: fruit
Item: apple
Answer: yes, apple is a fruit.

Now you try:
Category: {catergory}
Item: {items}
Answer:"""
    print(f"Response:", generate_text(one_prompt))

    print("\n--- Few-Shot ---")
    few_prompt = f"""Determine if the item belongs to the category.

Example 1:
Category: fruit
Item: banana
Answer: yes, banana is a fruit.

Example 2:
Category: fruit
Item: carrot
Answer: no, carrot is not a fruit. It is a vegetable.

Example 3:
Category: vehicle
Item: car
Answer: yes, car is a vehicle.

Now you try:
Category: {catergory}
Item: {items}
Answer:"""
    print(f"Response:", generate_text(few_prompt)) 

    print("\n--- Creative Few-Shot ---")
    creative_prompt = f"""Write a one-sentence story about the given word.
    
    Example 1:
    Word: Sonic
    Story: Sonic the Hedgehog raced through the city, his blue quills a blur as he saved the day.
    
    Example 2:
    Word: Tails
    Story: Tails, the clever fox with two tails, soared above the treetops, inventing gadgets to help his friends.
    
    Example 3:
    Word: Knuckles
    Story: Knuckles, the strong echidna, guarded the Master Emerald with unwavering determination and courage.
    
    Example 4:
    Word: Cream & Cheese
    Story: Cream the Rabbit and her loyal Cheese, hopped through meadows, spreading joy and kindness wherever they went.
   
    Example 5:
    Word: Amy
    Story: Amy Rose, with her trusty hammer, chased after Sonic, her heart full of admiration and adventure
    
    Word: {items}
    Story:"""
    print(f"Response:", generate_text(creative_prompt, temperature=0.7))

    print("\n--- Reflection Question ---")
    print("Q1. How did the different prompting techniques affect the responses?")
    print("Q2. In what scenarios might one-shot or few-shot prompting be more effective than zero-shot?")
    print("Q3. How can you apply these techniques in real-world applications?")

if __name__ == "__main__":
    run_activity()