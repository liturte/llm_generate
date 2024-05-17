from generate_problem_prompt import *
from generate_lit_literature import *
from research_method import *
from generate_full_paper import *
import pandas as pd
import openai
import os


# Getting the API key from the environment variable
openai.api_key = "sk-uibaSqnGRtJXAIybs1q5zUp2TrnBdiLo7gUdE1tbuKQYFrce"
openai.api_base="https://api.chatanywhere.tech/v1"

gpt_response=interactive_prompt_generation()
Problem_description=gpt_response
key_words=summarize_keywords(gpt_response)
print(key_words)
literature_review = generate_literature_review(key_words)
print(literature_review)
research_method=interactive_research_method_generation(Problem_description,literature_review)
paper_content = generate_full_paper(Problem_description, literature_review, research_method)
generate_pdf(paper_content)