import pandas as pd
import openai
import os


# Getting the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "sk-uibaSqnGRtJXAIybs1q5zUp2TrnBdiLo7gUdE1tbuKQYFrce"
openai.api_base="https://api.chatanywhere.tech/v1"
import pandas as pd
import openai
import os


def generate_prompt_with_chatgpt(messages):
    # Use ChatGPT with the maintained conversation history to generate a new prompt
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        api_key="sk-uibaSqnGRtJXAIybs1q5zUp2TrnBdiLo7gUdE1tbuKQYFrce ",
        api_base="https://api.chatanywhere.tech/v1",

    )
    return response['choices'][0]['message']['content']


def get_response_to_prompt(prompt, conversation_history):
    # 基于最终prompt使用chat模型生成回应
    conversation_history.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        api_key="sk-uibaSqnGRtJXAIybs1q5zUp2TrnBdiLo7gUdE1tbuKQYFrce ",
        api_base="https://api.chatanywhere.tech/v1",

    )
    return response['choices'][0]['message']['content']


def interactive_prompt_generation():
    conversation_history = [{"role": "system", "content": "You are an assistant."}]

    while True:
        user_input = input("Please describe the topic you want a prompt for: ")
        conversation_history.append({"role": "user", "content": user_input})
        prompt = f'based on user {user_input}, summerize the research problem, and formulate the research questions'
        chatgpt_response = get_response_to_prompt(prompt, conversation_history)
        print("ChatGPT's response to the prompt:\n", chatgpt_response)
        while True:
            satisfaction = input("Are you satisfied with the response? (yes/no): ")
            if satisfaction.lower() == 'yes':
                print("Prompt and response saved successfully.")
                return chatgpt_response
                break
            else:
                modifications = input("Please provide more details or modifications to refine the response: ")
                user_input += " " + modifications
                prompt = f"Based on the refined user input, generate a response: {user_input}"
                chatgpt_response = get_response_to_prompt(prompt, conversation_history)
                print("ChatGPT's response to the prompt:\n", chatgpt_response)
        break


def save_prompt(prompt):
    with open("saved_prompt.txt", "w") as file:
        file.write(prompt)
