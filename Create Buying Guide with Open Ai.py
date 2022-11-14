import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def intro_que(key):
  """
  This function will make a query to generate intro from OpenAi.
  """
  query = f"Write an introduction on “{key}” within 150 words."
  return str(query)

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

intro_query = intro_que('best wireless mouse')
introduction = query_ans(intro_query)
print(introduction)