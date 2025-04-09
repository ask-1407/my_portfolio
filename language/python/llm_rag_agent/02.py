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
- LLMが関数を実行するわけではない
"""