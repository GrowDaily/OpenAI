# pip install openai

from openai import OpenAI
import pandas as pd

openAIClient = OpenAI()

response = openAIClient.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": """you are a data analyst, 
     for any given topic you will give top  2 characteristics"""},
    {"role": "user", "content": "dessert"},
    {"role": "user", "content": "ocean"},
    {"role": "user", "content": "mountains"}
  ]
)

response.choices[0].message.content

pd.DataFrame(response.choices)