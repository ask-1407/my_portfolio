# 項目6: インデックスではなく複数代入アンパックを使う

"""
アンパックを用いることで以下のメリット
1.  行数が少なく見た目がスッキリする ※イテラブルなものなら可能
2. 
3.
"""
item = ("butter", "snack")
first, second = item
print(first, "and", second) # output: butter and snack


# バブルソートの実装でもアンパックを用いると一行でスワップが実装可能。
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1] # swap

names = ["pretzels", "cattots", "argula", "bacon"]
bubble_sort(names)
print(names) # output: ['argula', 'bacon', 'cattots', 'pretzels']

"""
スワップの動作は代入演算子右側のa[i],a[i-1]がまず評価されて，値が一時的な無名のタプルに格納。
次に代入演算子の左側のアンパック化ターンを使ってタプルの値を取り出してそれぞれの変数に代入する。
最後に一時的な無名のタプルが廃棄される。
"""


# アンパックを用いないパターン. if内のswapが三行となっている。
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp



# ジェネレータ式におけるターゲットリストにも使える。スナック食品リストのイテレーション
snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
for rank, (name, calories) in enumerate(snacks, 1):
    print(f"#{rank}: {name} has {calories} carolies")


# anti-pattern. snacks変数の構造の深さごとにインデックスを使っているため文字が余計に必要
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f"#{i+1}: {name} has {calories} carolies")


# 項目7 rangeではなくenumerateを使う

"""
組み込み関数enumerateは遅延評価ジェネレータでイテレータをラップする.
ループのインデックスとイテレータの次の値をyieldする。
enumerateにてyieldされる各対はfor文でうまくアンパックできる。
rangeとlenを組み合わせて書くよりも関係に書くことが可能。
また，enumerateの第二引数でカウンタを開始する数を指定できる。
"""

flavor_list = ["valilla", "chocolate", "pecan", "strawberry"]
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f"{i+1}: {flavor}")


for i, flavor in enumerate(flavor_list,i):
    print(f"{i}: {flavor}")