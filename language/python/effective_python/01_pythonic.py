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
for i, flavor in enumerate(flavor_list,i):
    print(f"{i}: {flavor}")

# rangeを利用する場合の書き方
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f"{i+1}: {flavor}")



# 項目8 イテレータを並列に処理するにはzipを使う

"""
組み込み関数zipは２つ以上のイテレータを遅延評価ジェネレータでラップする。
zipジェネレータは各イテレータから次の値のタプルをyieldし，for文の内側で直接アンパックできる。
zipはラップしているイテレータを一つずつ処理するので無限に長い入力でもメモリがクラッシュせず利用可能。
ただし，長さが異なる場合は短いほうに合わせられるので注意が必要。zip_lonestを使えば長いほうに合わせられる。
"""

names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]

# zipによるイテレート ※長さは短いほうに合わせられる
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

# zip_longestの場合
from itertools import zip_longest
names.append('Rosalind')
for name, count in zip_longest(names, count):
    print(f"{name}: {count}")


# 項目9 forとwhileの後のelseは利用しない


"""
forの後のelseはループ終了直後に実行される。for文のなかにbreakがあるとelseがスキップされる。
ループして何かを探す場合に使えはするものの，基本的にこれは利用しないほうが望ましい。
ループのような単純構成要素は自明であるべきであり，for-elseの振る舞いは直感的でないため。
"""

# ２つの数が互いに素の数かどうかを調べるコード
# パターン1：探している条件が見つかり次第早めにループを抜ける方法
def coprime(a,b):
    for i in range(2, min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

assert coprime(4, 9)
assert not coprime(3, 6)

# パターン2: ループして探していたものが見つかったかどうかを示す結果変数を使う
def coprime_alternate(a, b):
    is_coprime = True
    for i in range(2, min(a,b) + 1 ):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime

assert coprime_alternate(4, 9)
assert not coprime_alternate(3, 6)

# for-elseを用いた場合
a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
    else:
        print('Coprime !')

# 項目10 代入式で繰り返しを防ぐ
"""
ウォルラス演算子「:=」を使うとif文のような代入ができなかった箇所変数の代入ができる.
ある範囲の行で同じ式や代入を複数回繰り返している場合は，代入式の利用を検討するべき。
Pythonにはswitch/case文do/whileループはないが代入式を用いてそれらの機能を書くことができる。
"""

# lemonが少なくとも一つ以上あることを確認したい
fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}

def make_lemonade():
    pass

def out_of_stock():
    pass

class OutOfBananas(Exception):
    pass


# 以下のように書くことはできるが，変数countがif文の最初のブロックのみで使われておらず読みづらい。
count = fresh_fruit.get('lemon', 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()

# ウォルラス演算子を利用することで明瞭さを向上できる。
if (count := fresh_fruit.get('lemon', 0)) >= 0:
    make_lemonade(count)
else:
    out_of_stock()

# 以下のようにpieces変数をもとに関数をキックする際にもウォルラス演算子が有効
# 使わない場合はこちら

pieces = 0 # elseで定義する方法もあるが冒頭に初期化されるほうが好まれる。
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas(count)

try: 
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()


# 利用した場合. count変数の強調がなくなる。
pieces = 0
if (count := fresh_fruit.get('banana',0)) >= 2:
    pieces = slice_bananas(count)

try:
    smoothies = make_smooothies(pieces)
except OutOfBananas:
    out_of_stock()

"""
Pythonにはswitch/caseがないので一般にはif/elif/elseを入れ子にすることで実現する
例えばバナナスムージー，アップルサイダー，レモネードの優先度となっている場合
"""

# walrus演算子を利用しない書き方. 変数countへの代入が逐次走り読みにくい。
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit.get('apple', 0)
    if count >= 4:
        to_enjoy = make_cider(count)
    else:
        count = fresh_fruit.get('lemon', 0)
        if count:
            to_enjoy = make_lemonade(count)
        else:
            to_enjoy = 'Nothing'

# walrus演算子を利用する場合 元より5行少なくなり，入れ子が改善されている。
if (count := fresh_fruit.get('banana', 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(count)
elif (count := fresh_fruit.get('appke', 0)) >= 4:
    to_enjoy = make_cider()
elif count := fresh_fruit.get('lemon', 0):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = 'Nothing'

"""
do/whileのような内容に対してもwalrus演算子の利用で短くて読みやすいコードがかける。
果物が届いたらジュースをビン詰めすることを考える。

whileループによる実装例。fresh_fruit = pick_fruit() が2回登場する。
"""
def pick_fruit():
    pass

def make_juice(fruit, count):
    pass

bottles = []
fresh_fruit = pick_fruit() # ループの最初の条件設定に利用
while fresh_fruit:
    for fruit, cunt in fresh_fruit.items():
        batch = make_juice(fruit = fruit, count = count)
        bottles.extend(batch)
    fresh_fruit = pick_fruit() # ループ後に配達されたジュースのリストを補充するために使う

# 条件付きbreakによる実装例。これでループを制御する。
bottles = []
while True: # ループ
    fresh_fruit = pick_fruit()
    if not fresh_fruit: # 付け足し
        break
    for fruit, cunt in fresh_fruit.items():
        batch = make_juice(fruit = fruit, count = count)
        bottles.extend(batch)

# walrus演算子利用の例。変数fresh_fruitが再度さ移入されwhileループないで条件を毎回チェックする必要例をなくすことができる
bottles = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit = fruit, count = count)
        bottles.extend(batch)

