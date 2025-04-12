# 2.2 OpenAIのチャットAPIの基本

## Chat Completion API

"""
- 基本的にはChat Completion APIを使う。Completion APIはLegacyである。リクエストは以下のようになる。

```json
{
    "model":"gpt-4o-mini",
    "messages":[
        {"role":"system","content": "You are a helpful assistant."}
        {"role":"user","content": "こんにちは！私はジョンと言います."}
    ]
}
```
- `message` という配列の各要素にロールごとのコンテンツを入れる
- `role`にLLMに対する役割を与える。`assisant`として会話履歴を送ることも可能。
  - Chat Completion APIはステートレスなため，過去のリクエストの会話履歴を踏まえて応答する性能は持っていない。会話履歴を踏まえる場合，すべての履歴を送る必要がある。
"""

## Batch API

"""
- Batch API は非同期でモデルの出力を得ることができる。即座には得られないがChat Completion APIの半分の料金で利用することができる
"""

# 2.3 トークン

"""
- LLMはテキストをトークンという単位に分割して扱う。単語とは必ずしも一致しないが，英語の場合は1トークンで4文字から0.75単語程度とされる。日本語は英語よりも多くなる傾向があるので削減したいのであれば英語を利用することが望ましい。
- OpenAIが提供するTokenizerとtiktokenを使うとトークン数を把握することができる。tiktokenは以下のように使える。
"""

import tiktoken
text = "ここに解析したい文字をいれる"

encoding = tiktoken.encoding_for_model("pt-4o")
tokens = encoding.encode(text)
print(len(tokens)) # >>> token数が表示される。

# 2.5 Chat Completions APIハンズオン
"""
- openaiライブラリをインストールする。
- 環境変数`OPENAI_API_KEY`から取り出したAPIキーを使用してリクエストを送る。リクエストにはモデルとメッセージを最低限いれる。
"""

from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
  model = "gpt-4o-mini",
  messages = [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "こんにちは！私はジョンといいます"
    }    
  ]
)
print(response.to_json(indent=2))

"""
- GPT4o,GPT4o miniであれば画像入力も対応している。
"""

from openai import OpenAI

client = OpenAI()
image_url = "https://image_url/hoge.jpg"
response = client.chat.completions.create(
  model="gpt-4o-mini",
     messages=[
         {
             "role": "user",
             "content": [
                 {"type": "text", "text": "画像を説明してください。"},
                 {"type": "image_url", "image_url": {"url": image_url}},
             ],
         }
     ],
 )


print(response.choices[0].message.content)
# >>> 画像はxxxで....

# 2.6 Function Calling
"""
- 利用可能な関数とLLMに伝えておいてLLMに関数を使いたいという判断を指せる機能
- LLMが関数を実行するわけではなく，関数の実行はPython等を使って実装者で実行。
"""

# 天気を取得する関数を用意
import json

def get_current_weather(location, unit="fahrenheit"):
    if "tokyo" in location.lowet():
        return json.dumps({"location": "Tokyo", "unit": unit, "temperature": 20})

    elif "new york" in location.lower():
        return json.dumps({"location": "new york", "unit": unit, "temperature": 72})
        
    elif "paris" in location.lower():
        return json.dumps({"location": "paris", "unit": unit, "temperature": 22})

# LLMが利用できる関数の一覧を定義
# NOTE functionsというパラメータがリリース当初はあるが，現時点では非推奨。
tools = [
     {
         "type": "function",
         "function": {
             "name": "get_current_weather",
             "description": "Get the current weather in a given location",
             "parameters": {
                 "type": "object",
                 "properties": {
                     "location": {
                         "type": "string",
                         "description": "The city and state, e.g. San Francisco, CA",
                     },
                     "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                 },
                 "required": ["location"],
             },
         },
     }
 ]

from openai import OpenAI

client = OpenAI()
messages = [
    {"role": "user", "content": "今の東京の天気は？"}
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages = messages,
    tools = tools,
)
print(response.to_json(indent=2))

"""
{
  "id": "chatcmpl-9jj2wv14w0fYHr6CUAfe0MW2zL7nT",
  "choices": [
    {
      "finish_reason": "tool_calls",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": null,  ← 今までの実行例ではLLMが生成したテキストはここに含まれていた
        "role": "assistant",
        "tool_calls": [
          {
            "id": "call_if3ni88ahchw2egXtxZNxA7",
            "function": {
              "arguments": "{\"location\":\"Tokyo\"}", 
              "name": "get_current_weather"
            },
            "type": "function"
          }
        ]
      }
    }
  ],
  "created": 1720684945,
  "model": "gpt-4o-2024-05-13",
  "object": "chat.completion",
  "system_fingerprint": "fp_298125635f",
  "usage": {
    "completion_tokens": 15,
    "prompt_tokens": 81,
    "total_tokens": 96
  }
}

"""

# パラメータtool_choiceを使うとLLMは関数を呼び出すような応答をせず，通常のテキストを返す。
# デフォルトはtoolsを与えなかった場合はnone，toolsを与えた場合はautoとなる
# Structured Outputs機能をつかうと指定したJSON Schemaでの出力を保証する