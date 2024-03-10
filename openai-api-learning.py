# pip install openai

from openai import OpenAI

openAIClient = OpenAI()

response = openAIClient.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "who won 2011 cricket world cup?"}
  ]
)

ChatCompletion(id='chatcmpl-90ovsRjPUYirPdoVDVZkZvddHpN16', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='India won the 2011 Cricket World Cup. India defeated Sri Lanka in the final to win their second Cricket World Cup title.', role='assistant', function_call=None, tool_calls=None))], created=1709982812, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_4f0b692a78', usage=CompletionUsage(completion_tokens=26, prompt_tokens=26, total_tokens=52))