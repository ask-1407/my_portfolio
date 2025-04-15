# プロンプトのテンプレート化は以下のように行う。

prompt="""

以下の料理のレシピを考えてください

料理名: {dish}
"""

# レシピを考える関数
def generate_recipt(dish: str) -> str:
    response =client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {
                "role": "user",
                "content": prompt.format(dish=dish)
            }
        ]
    )
    return response.choices[0].message.content.strip()

recipe = generate_recipt("カレー")
print(recipe)

# 入力データと命令は独立指せるのが望ましい。「"""」や「###」で区切るととも多い。

# 前提条件や外部情報などを文脈(context)として与えるとそれに従った回答を得ることができる。


