import pandas as pd
import openai
import os

S2_API_KEY = os.getenv('S2_API_KEY')
# Getting the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "sk-uibaSqnGRtJXAIybs1q5zUp2TrnBdiLo7gUdE1tbuKQYFrce"
openai.api_base="https://api.chatanywhere.tech/v1"
def summarize_keywords(response_text):
    # 使用ChatGPT总结回答中的关键词
    conversation_history = [{"role": "system", "content": "You are an assistant."},
                            {"role": "user", "content": f"Summarize the key words from the following text: {response_text},and return the three keywords as a List"}]
    summary_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        api_key="sk-uibaSqnGRtJXAIybs1q5zUp2TrnBdiLo7gUdE1tbuKQYFrce ",
        api_base="https://api.chatanywhere.tech/v1",
    )
    keywords = summary_response['choices'][0]['message']['content']
    keyword_list = [keyword.strip() for keyword in keywords.split(',')]
    return keyword_list


import requests

def find_basis_paper(query, num_papers_api=20):
    fields = 'title,url,abstract,citationCount,journal,isOpenAccess,fieldsOfStudy,year,journal'
    rsp = requests.get('https://api.semanticscholar.org/graph/v1/paper/search',
                        headers={'X-API-KEY': S2_API_KEY},
                           params={'query': query, 'limit': num_papers_api, 'fields': fields})
    rsp.raise_for_status()
    results = rsp.json()
    total = results["total"]
    if not total:
        print('No matches found. Please try another query.')

    print(f'Found {total} results. Showing up to {num_papers_api}.')
    papers = results['data']
    # df = pd.DataFrame(papers)
    return papers #[:result_limit]
# 关键词列表

def create_literature_review(papers):
    # 组织论文信息，生成文献综述的请求文本
    review_text = "Generate a literature review based on the following papers:\n"
    for paper in papers:
        title = paper['title']
        url = f"https://www.semanticscholar.org/paper/{paper['paperId']}"
        abstract = paper['abstract'] if 'abstract' in paper else "No abstract available."
        review_text += f"Title: {title}\nAbstract: {abstract}\nURL: {url}\n\n"

    # 使用OpenAI的ChatGPT模型来生成文献综述
    conversation_history = [{"role": "system", "content": "You are an assistant."},
                            {"role": "user", "content": review_text}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        api_key="sk-uibaSqnGRtJXAIybs1q5zUp2TrnBdiLo7gUdE1tbuKQYFrce ",
        api_base="https://api.chatanywhere.tech/v1",
    )
    return response['choices'][0]['message']['content']
def generate_literature_review(keywords):
    articles = find_basis_paper(keywords,num_papers_api=5)
    literature_review = create_literature_review(articles)
    return literature_review
