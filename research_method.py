import pandas as pd
import openai
import os
# -*- coding: gb2312 -*-
# Configure the OpenAI API settings
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "sk-uibaSqnGRtJXAIybs1q5zUp2TrnBdiLo7gUdE1tbuKQYFrce"
openai.api_base="https://api.chatanywhere.tech/v1"


def generate_prompt_with_chatgpt(problem_description, literature_review):
    # Concatenate the problem description and literature review to form a prompt
    prompt = f"Given the problem description: {problem_description} and the relevant literature review: {literature_review}, suggest potential research methods."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an assistant."}, {"role": "user", "content": prompt}],
        api_key="sk-uibaSqnGRtJXAIybs1q5zUp2TrnBdiLo7gUdE1tbuKQYFrce ",
        api_base="https://api.chatanywhere.tech/v1",
    )
    return response['choices'][0]['message']['content']


def interactive_research_method_generation(problem_description,literature_review):
    # Generate the initial research methods
    initial_methods = generate_prompt_with_chatgpt(problem_description, literature_review)
    print("Suggested research methods:\n", initial_methods)

    while True:
        # Ask for user feedback and refine the suggestions if needed
        satisfaction = input("Are you satisfied with these research methods? (yes/no): ")
        if satisfaction.lower() == 'yes':
            print("Research methods accepted.")
            return initial_methods
            break
        else:
            feedback = input("Please provide details or modifications to refine the methods: ")
            # Update the problem description or literature review based on feedback
            problem_description += " " + feedback
            initial_methods = generate_prompt_with_chatgpt(problem_description, literature_review)
            print("Refined research methods:\n", initial_methods)


