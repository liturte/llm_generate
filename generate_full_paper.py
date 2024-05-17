import os
import openai
from fpdf import FPDF
openai.api_key = "sk-uibaSqnGRtJXAIybs1q5zUp2TrnBdiLo7gUdE1tbuKQYFrce"
openai.api_base="https://api.chatanywhere.tech/v1"


def generate_full_paper(problem_description, literature_review, research_method):
    combined_input = f"Problem Description: {problem_description}\n\nLiterature Review: {literature_review}\n\nResearch Method: {research_method}\n\nGenerate a research paper that includes an abstract, introduction, methods, results and discussion, and conclusion based on the above information."

    conversation_history = [
        {"role": "system", "content": "You are an assistant."},
        {"role": "user", "content": combined_input}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        api_key="sk-uibaSqnGRtJXAIybs1q5zUp2TrnBdiLo7gUdE1tbuKQYFrce ",
        api_base="https://api.chatanywhere.tech/v1",
    )

    return response['choices'][0]['message']['content']


def generate_pdf(paper_content):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # 分割生成的文章为多段，并添加到PDF中
    for line in paper_content.split('\n'):
        pdf.multi_cell(0, 10, txt=line)

    pdf.output("generated_paper.pdf")