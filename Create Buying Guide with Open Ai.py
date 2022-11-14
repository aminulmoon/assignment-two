import os
import openai
from dotenv import load_dotenv
from requests import post
load_dotenv()
import base64

wp_user = os.getenv('wp_user')
wp_password = os.getenv('wp_password')
credential = f'{wp_user}:{wp_password}'
token = base64.b64encode(credential.encode())
header = {'Authorization':'Basic '+token.decode('utf-8')}
api_endpoints = os.getenv('api_endpoint')
openai.api_key = os.getenv("OPENAI_API_KEY")


file = open('Keywords.txt')
keywords = file.readlines()
file.close()

for keyword in keywords:
  key = keyword.strip('\n')
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

  def paragraph_html(text):
    """
    This function will convert paragraph to HTML in Gutenberg formate.
    """
    code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return code


  def first_h2_html(key):
    """
    This function will convert H2 for Gutenberg.
    """
    code = f'<!-- wp:heading --><h2>Why {key} is important</h2><!-- /wp:heading -->'
    return code.title()


  def second_h2_html(key):
    """
    This function will convert H2 for Gutenberg.
    """
    code = f'<!-- wp:heading --><h2>What to know about {key}</h2><!-- /wp:heading -->'
    return code.title()


  def third_h2_html(key):
    """
    This function will convert H2 for Gutenberg.
    """
    code = f'<!-- wp:heading --><h2>What to look for in a {key} before buy</h2><!-- /wp:heading -->'
    return code.title()


  title = f'Best {key} Buying Guide For 2023'
  slug = f'best {key}'


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

  intro_query = intro_que(key)
  important_query = important_que(key)
  what_know_query = what_know(key)
  what_look_query = what_look(what_know)
  conclusion_query = conclusion_que(key)


  introduction = query_ans(intro_query)
  why_important = query_ans(important_query)
  what_to_know = query_ans(what_know_query)
  what_to_look = query_ans(what_look_query)
  conclusion = query_ans(conclusion_query)


  wp_title = title.title()
  wp_intro = paragraph_html(introduction)
  wp_first_h2 = first_h2_html(key)
  wp_why_important = paragraph_html(why_important)
  wp_second_h2 = second_h2_html(key)
  wp_what_to_know = paragraph_html(what_to_know)
  wp_third_h2 = third_h2_html(key)
  wp_what_to_look = paragraph_html(what_to_look)
  wp_conclusion_h2 = '<!-- wp:heading --><h2>Conclusion</h2><!-- /wp:heading -->'
  wp_conclusion = paragraph_html(conclusion)
  wp_slug = slug.strip().replace(' ','-')

  wp_content =f'{wp_intro}{wp_first_h2}{wp_why_important}{wp_second_h2}{wp_what_to_know}{wp_third_h2}{wp_what_to_look}{wp_conclusion_h2}{wp_conclusion}'

  def wp_posting(title,content,slug,excerpt):
    api_url = api_endpoints
    data = {
      'title': wp_title,
      'content': wp_content,
      'slug': wp_slug,
      'excerpt': introduction
    }
    response = post(api_url, headers=header, data=data )
    if response.status_code ==201:
      print('Post Successfull')
    else:
      print('Something Went Wrong')

  wp_posting(wp_title,wp_content,wp_slug,introduction)

