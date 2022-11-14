import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def intro_que(key):
  """
  This function will make a query to generate intro from OpenAi.
  """
  query = f"Write an introduction on “best{key}” within 150 words."
  return query


def important_que(key):
  """
  This function is for making query of 'why it is important'.
  """
  query = f'Why {key} is important?'
  return query


def what_know(key):
  """
  This function is for making query of 'what ot know about the item'.
  """
  query = f'Write in detail on "what to know about {key}"'
  return query


def what_look(key):
  """
  This function is for making query of 'What to look before buy'.
  """
  query = f'What to look for in a {key} before buy?'
  return query


def conclusion_que(key):
  """
  This function is for making query of conclusion.
  """
  query = f'Write a conclusion on best {key}.'
  return query


def query_ans(text):
  """
  This function is for generating text/article for any query from OpenAi.
  :param text: Provide the query variable here.
  :return: This will return answer for your query.
  """
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=text,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  data = response.get('choices')[0].get('text')
  return data

intro_query = intro_que('wireless mouse')
important_query = important_que('wireless mouse')
what_know_query = what_know('wireless mouse')
what_look_query = what_look(what_know)
conclusion_query = conclusion_que('wireless mouse')


introduction = query_ans(intro_query)
why_important = query_ans(important_query)
what_to_know = query_ans(what_know_query)
what_to_look = query_ans(what_look_query)
conclusion = query_ans(conclusion_query)


print(introduction)