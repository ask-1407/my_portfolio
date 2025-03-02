# 項目11 シーケンスをどのようにスライスするか知っておく

"""
スライスでは冗長をさける。インデックスのstart・endに値を指定しない。
境界外のインデックスのstart・endが許される。
リストのスライスへの代入では元のシーケンスの指定範囲が，たとえ長さが違っていても参照されているもので置き換えられる。
"""

a = ['a','b','c','d','e','f','g','h']
# リストの先頭からスライスするときにはインデックスのゼロは省く。
assert a[:5] == a[0:5]
# 終端までスライスするときは末尾のインデックスは冗長になるので省く。
assert a[5:] == a[5:len(a)]

# スライスであれば指定値がリストの境界を超えていても出力される。
first_twenty_times = a[:20]
last_twenty_times = a[-20:]
print(first_twenty_times) # output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(last_twenty_times)

# ただし直接アクセスすると例外がでる
a[20] # IndexError: list index out of range

# スライスで得た場合，コピーが渡される。
b = a[3:]
print('Before:  ', b) # Before:   ['d', 'e', 'f', 'g', 'h']
b[1] = 99
print('After    ', b) # After     ['d', 99, 'f', 'g', 'h']
print('No change', a) # No change ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 代入に用いるとスライスは元のリストの指定範囲を置きかえる。スライスの長さは不一致でもよい。
print('Before:  ', a) # Before:   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[2:7] = [99, 22, 14]
print('After:   ', a) # After:   ['a', 'b', 99, 22, 14, 'h']

# 代入リストがスライスより長いとリストが長くなる。
print('Before ', 1) # Before  ['a', 'b', 99, 22, 14, 'h']
a[2:3] = [47, 11]
print('After', a) # After ['a', 'b', 47, 11, 22, 14, 'h']

# スライスのときにstartとendを共に省略するともとのリストの複製となる
b = a[:]
assert b == a and b is not a

# startもendもないスライスに代入を行うと参照していたリストの複製を使って内容が置き換わる。
b = a
print('Before a', a) # Before a ['a', 'b', 47, 11, 22, 14, 'h']
print('Before b', b) # Before b ['a', 'b', 47, 11, 22, 14, 'h']

a[:] = [101, 102, 103]
assert a is b # まだ同じリストオブジェクト
print('After a', a) # 内容はいまでは変わっている
print('After b', b) # aと同じ内容の同じリスト

# 項目12 1つの式ではストライドとスライスは同時に使わない

"""
スライスでstart, end ,strideをすべて指定すると非常に読みにくい
スライスでは制の増分値をstartやendのどちらか一方のみと使う。可能な限り負の増分値を使わない。
一つのスライスにstart，end，strideを一緒に使わない。
3つ全てが必要なときには代入を2度使うか組み込みモジュールのitertools.isliceを利用する。
"""

# somelist[start:end:stride]という形式でスライスの増分を定義できる
x = ['red','orange','yellow','green','blue','indigo','violet']
odds = x[::2] # 奇数のみを取得
evens = x[1::2] # 偶数のみを取得
print(odds) # ['red', 'yellow', 'blue', 'violet']
print(evens) # ['orange', 'green', 'indigo']

# ストライドは予期せぬ振る舞いを引き起こすことがある
# UTF-8バイト文字列で符号化したUnicodeではエラーが発生する

w = '寿司'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8') # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x9d in position 0: invalid start byte

# ストライドとスライスを同時に利用すると紛らわしくなる.
# できる限りストライドは制の値にし，startとendは省略する。
# 3つ全ての引数を使うときは2回のスライスを使うか，itertools.isliceを使う

# anti-pattern
x = ['a','b','c','d','e','f','g','h']
x[2::2] # ['c','e','g']
x[-2::-2] # ['g','e','c','a']
x[-2:2:-2] # ['g','e']
x[2:2:-2] # []

# good
y = x[::2] # ['a','c','e','g']
z = x[1::2] # ['b','d','f','h']

# 項目13 スライスではなくcatch-allアンパックを使う
"""
代入のアンパックでアスタリスク付きの式を使い，アンパックするパターンの残りをまとめてリストにできる
アスタリスク月の式はどこにでも書くことができ，常に受け取る値のリストになる
リストを重複の内容に分割する場合，catch-allアンパックはスライスやインデックスを使うよりもエラーの危険が少ない。
ただしアスタリスク付きの式は常にリストを返すので，イテレータのアンパックは結果が全てメモリに収まる場合に利用すること。
"""

# アンパックを行うにはアンパックするシーケンスの長さが必要. 
car_ages = [0,9,4,8,7,20,19,1,6,15]
car_ages_descending = sorted(car_ages, reverse=True)
oldest, second_oldest = car_ages_descending # ValueError: too many values to unpack (expected 2)

# 以下のようにインデックスやスライスを使いたくなるが読みづらい. 変数の値が変わったときにシーケンスの更新が必要。
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others) # 20 19 [15, 9, 8, 7, 6, 4, 1, 0]

# このような状況ではアスタリスク付きの引数によるcatch-allアンパックを使うことで同様の結果が得られる。
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others) # 20 19 [15, 9, 8, 7, 6, 4, 1, 0]

# アスタリスク付きの引数はどこにでも書くことができる
oldest, *others, youngest = car_ages_descending
print(oldest, youngest, others) # 20 0 [19, 15, 9, 8, 7, 6, 4, 1]

*others, second_youngest, youngest = car_ages_descending
print(youngest, second_youngest, others) # 0 1 [20, 19, 15, 9, 8, 7, 6, 4]


# アスタリスク付きの式を含むアンパック代入では少なくとも一つ指定部分が必要。
*others = car_ages_descending # SyntaxError: starred assignment target must be in a list or tuple

# 一つのアンパックパターンの中に複数のアスタリスク付きの式を指定することもできない
first, *middle, *second_middle, last = [1,2,3,4] # SyntaxError: two starred expressions in assignment

# アンパックされる複数のレベルがある構造の中の異なる部分に対してcatch-allアンパックをする場合は複数のアスタリスク付きの式があってもよい。
# 以下のコードは筆者としては非推奨だが，理解できればアンパック代入におけるアスタリスク付きの式の振る舞いを理解できる。
car_inventory = {
    'Downtown': ('Silver Shadow', 'Pinto', 'DMC'),
    'Airport': ('Skyline', 'Viper', 'Gremlin', 'Nova'),
}
((loc1, (best1, *rest1)),
(loc2, (best2, *rest2))) = car_inventory.items()
print(f'Best at {loc1} is {best1}, {len(rest1)} others') # Best at Downtown is Silver Shadow, 2 others
print(f'Best at {loc2} is {best2}, {len(rest2)} others') # Best at Airport is Skyline, 3 others

# アスタリスク付きの式はlistインスタンスになり，アンパックされるシーケンス要素がない場合は空のリストになる。
short_list = [1,2]
first, second, *rest = short_list
print(first, second, rest) # 1 2 []

# アンパック構文をイテレータでアンパックすることもできる。
def generate_csv():
    yield ('Date', 'Make', 'Model', 'Year', 'Price')
    yield ('2020-10-10', 'Toyota', 'Corolla', 2019, 20000)
    yield ('2020-10-11', 'Honda', 'Civic', 2017, 15000)

it = generate_csv()
header, *rows = it # アスタリスク付きの式によりヘッダーをイテレータの残りと別々に処理できる
print('CSV Header:', header) # CSV Header: ('Date', 'Make', 'Model', 'Year', 'Price')
print('Row count:', len(rows))  # Row count: 2

# インデックスとスライスをりようしてジェネレータの結果を処理することもできるが行が複数になり見た目が複雑になる。
all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print('CSV Header:', header) # CSV Header: ('Date', 'Make', 'Model', 'Year', 'Price')
print('Row count:', len(rows))  # Row count: 2


# 項目14 key引数を使い複雑な基準でソートする
"""
list型のsortメソッドはリストの内容を文字列，整数，タプルなどの自然な順序で並べ替えるのに使える。
sortメソッドは特殊メソッドをつかって順序付けするメソッドを定義しないとオブジェクトで動作しないが一般的にはこれはあまりない。
sortメソッドのkeyパラメータを使い，list各要素をソートする値を返すヘルパー関数を与えることができる。
key関数でtupleを返すことにより複数のソート基準を組み合わせることができる。
マイナス演算子を使えない型ではsortメソッドを様々なkey関数とreverse値に対して，
最も低いランクのsort呼び出しから最も高いランクのsort呼び出しまでの順に複数回呼び出すことで組み合わせたソートができる。
"""

# listには要素の順序に従って整列するsortメソッドが存在する。
numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers) # [11, 68, 70, 86, 93]

# オブジェクトに対してsortメソッドを適用してもエラーが発生する。
# 理由はクラスで定義されていない比較のための特殊メソッド(__lt__ メソッド)をsortメソッドが呼び出すため。
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'
    
tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25),
]

tools.sort() # TypeError: '<' not supported between instances of 'Tool' and 'Tool'

# sortメソッドは関数を引数として期待するkeyパラメータが使える。以下はToolsのname属性を使ってソートする例。
print('Unsorted:', tools) # Unsorted: [Tool('level', 3.5), Tool('hammer', 1.25), Tool('screwdriver', 0.5), Tool('chisel', 0.25)]
tools.sort(key = lambda x: x.name)
print('Sorted:', tools) # Sorted: [Tool('chisel', 0.25), Tool('hammer', 1.25), Tool('level', 3.5), Tool('screwdriver', 0.5)]

# 重さ(weight)でもソート可能。
tools.sort(key = lambda x: x.weight)
print('By weight:', tools) # By weight: [Tool('chisel', 0.25), Tool('screwdriver', 0.5), Tool('hammer', 1.25), Tool('level', 3.5)]

# 文字列のような基本型ならソートの前に値の変換ができる。
places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('Case sensitive:', places) # Case sensitive: ['New York', 'Paris', 'home', 'work']
places.sort(key = lambda x :x.lower())
print('Case insensitive:', places) # Case insensitive: ['home', 'New York', 'Paris', 'work']

# tupleはデフォルトで比較可能で，sortメソッドが必要とする__lt__のような特殊メソッドをもつ
saw = (5, 'circular saw')
jackhammer = (40, 'jackhammer')
assert not (jackhammer < saw) # 期待通り

drill = (4, 'drill')
sander = (4, 'sander')
assert  drill[0] == sander[0] # 同じ重さ
assert  drill[1] < sander[1] # 英字順で小さい
assert  drill < sander # 先頭要素から評価する。

# 
power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]

# 以下のコードではtupleの比較方式を利用して，工具の重さ順でソートする。
power_tools.sort(key = lambda x: (x.weight, x.name))
print(power_tools) # [Tool('drill', 4), Tool('sander', 4), Tool('circular saw', 5), Tool('jackhammer', 40)]

# Key関数でtupleを返す場合，ソートの方向がすべて同じ方向である必要がある。
power_tools.sort(key = lambda x: (x.weight, x.name), reverse = True)
print(power_tools) # [Tool('drill', 4), Tool('sander', 4), Tool('circular saw', 5), Tool('jackhammer', 40)]

# 数値についてはマイナス単項演算子でソートの昇順・降順を反転できる。コード量が少ないので推奨。
power_tools.sort(key = lambda x: (-x.weight, x.name))
print(power_tools) # [Tool('jackhammer', 40), Tool('circular saw', 5), Tool('drill', 4), Tool('sander', 4)]

# ただし全ての型には使えない。
power_tools.sort(key=lambda x:(x.weight, -x.name), reverse=True) # TypeError: bad operand type for unary -: 'str'

# list型のsortメソッドはKey関数が互いが等しいという値を返したときは入力のリストでの順番を保持する
power_tools.sort(key = lambda x: x.name) # 名前昇順
power_tools.sort(key = lambda x: x.weight, reverse=True) # 重さ降順
print(power_tools) # [Tool('jackhammer', 40), Tool('circular saw', 5), Tool('drill', 4), Tool('sander', 4)]

# 項目15 dictの挿入順序に依存する場合は注意する
"""
- Python3.7以降はdictインスタンスの内容をイテレーションするとキーが最初に挿入された順番が保持される。
- Pythonではdictインスタンスではないが辞書のように振る舞うオブジェクトを定義できる。
- 辞書的クラスでの注意事項は3つ。①挿入順序に依存しないコードを書く，②実行時にdict型か明示的にチェックする，③型ヒントと静的解析でチェックする
"""

# Python3.7以降ではdictの挿入順序が保持される
baby_names = {
    'cat': 'kitten',
    'dog': 'puppy',
}
print(baby_names) # {'cat': 'kitten', 'dog': 'puppy'}
print(list(baby_names.keys())) # ['cat', 'dog']

# Pythonでは標準プロトコルをエミュレートするコンテナ型を定義できる。
# Pythonは動的型付け言語であるため殆どのコードは厳格なクラス階層に基づく代わりに，オブジェクトの振る舞いがデファクトの型にもとづくダックタイピングに依存している。
votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863,
}

# 
def populate_ranks(votes, ranks):
    """投票データを処理して動物の順位を空の辞書に登録する"""
    names = list(votes.keys())
    names.sort(key = votes.get, reverse = True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner(ranks):
    return next(iter(ranks))

ranks = {}
populate_ranks(votes, ranks)
print(ranks) # {'otter': 1, 'fox': 2, 'polar bear': 3}
winner = get_winner(ranks)
print(winner) 

# collections.abcをつかって新たな辞書クラスを作り英字順にイテレートする
from collections.abc import MutableMapping
class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key
    
    def __len__(self):
        return len(self.data)

# get_winner()の実装が辞書のイテレーションで挿入順序がpopulate_ranlsに一致していると仮定しているため所望の結果にはならない。
sorted_ranks = SortedDict()
populate_ranks(votes,sorted_ranks)
print(sorted_ranks.data)
winner  = get_winner(sorted_ranks) # {'otter': 1, 'fox': 2, 'polar bear': 3}
print(winner) # 'fox'

# 解決方法1 get_winner関数を再実装してranks辞書が特定のイテレーション順になっていることを仮定しない。
def get_winner(ranks):
    for name, ranks in ranks.items():
        if rank == 1:
            return name
        
winner = get_winner(sorted_ranks)
print(winner) # otter

# 解決方法2 関数の先頭でranksの型が期待通りかをチェックして，そうでないなら例外をだす。
def get_winner(ranks):
    if not isinstance(ranks, dict):
        raise TypeError('must provide a dict instance')
    return next(iter(ranks))

get_winner(sorted_ranks) # TypeError: must provide a dict instance'

# 解決方法3 型ヒントを使ってget_winnerに渡される値がdictインスタンスで辞書的な振る舞いをするMutableMappingでないことを確認する
from typing import Dict, MutableMapping
def populate_ranks(votes: Dict[str, int], ranks:Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))

# $python3 -m mypy --strict example.py

# 項目16 辞書の欠損キーの処理にはgetを使う
"""
辞書の欠損キーを検出するにはin式，KeyError例外，getメソッド，setdefaultメソッドが使える。
getメソッドはカウンタのような基本的な型からなる辞書が最適。
辞書の値の生成コストがかかる場合や例外が送出される可能性がある場合は代入式と一緒に使うのが望ましい。
dictのsetdefaultが最良と思われる場合はdefaultdictを使うことを検討する。
"""

counters = {
    'pumpernickel': 2,
    'sourdough': 1,
}

# ifでキーが存在する場合にTrueを返すin式を使う。
key = 'what'
if key in counters:
    count = counters[key]
else:
    count = 0
counters[key] = count + 1

# KeyError例外を送出する方法でもできる。一回だけアクセスするので効率がいい。
try:
    count = counters[key]
except KeyError:
    count = 0
counters[key] = count + 1

# getメソッドを用いるとはるかに短くてすむ. 単純な型の辞書ならこれがもっともよい。
count = counters.get(key, 0)
counters[key] = count + 1

# 辞書がリストのような複雑な場合を考える
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}

# in式を使う場合キーがある場合には2回アクセス，ない場合はアクセスと代入が1回ずつ必要
key = 'brioche'
who = 'Elmer'
if key in votes:
    names = votes[key]
else:
    votes[key] = names = []
names.append(who)
print(votes)

# ValueがリストのときにもKeyError例外は有効。
# キーがあれば1回のアクセス，なければアクセス・代入が一回ずつなので効率がよい。
try:
    names = [votes]
except KeyError:
    votes[key] = names = []

# getメソッドでもよい
names = votes.get(key)
if names is None:
    votes[key] = names = []
names.append(who)

# walrus演算子を利用するとさらに短くできる
if (names := votes.get(key)) is None:
    votes[key] = names = []
names.append(who)

# setdefaultを使うと更に簡潔にかける。
names = votes.setdefault(key,[]) # 辞書のキーを取得し，キーがないときは該当キーにデフォルト値を割り当てる。
names.append(who)

# ただし，setdefaultという名前からは値を取得することが判別できずPythonに詳しくない人にはわかりづらい。
# また，setdefaultに渡されるデフォルト値は欠損キーの場合は辞書に複製されるのではなく直接代入される
data = {}
key = 'foo'
value = []
data.setdefault(key,value)
print('Before:', data) # Before: {'foo': []}
value.append('hello')
print('After:', data) # After: {'foo': ['hello']}

# setdefaultはどんなキーであっても新たにデフォルト値を作成しておかなければならない。呼び出すたびに作成するのでパフォーマンス上のオーバーヘッドになる
# 欠損した辞書キーを扱うのにsetdefaultが最短となるのは「デフォルト値の作成が安価で変更可能かつ例外の起こる可能性がない」ときに限り（e.g. list)
# なお，defaultdictのほうがよい。（詳細は後述）

# 項目17 内部状態の欠損要素を扱うにはsetdefaultではなくdefaultdictを扱う。
"""
辞書を作って任意のキー集合を処理するとき，collectionsモジュールのdefaultdictを使う。
辞書のキーを指定されその要素を自分で作成することができない状況ならgetを使って要素にアクセスする。
より短いコードになるsetdefaultの使用を検討することもある。
"""

visits = {
    'Mexico': {'Tulum', 'Puerto Vallarta'},
    'Japan': {'Hakone'},
}

# setdefaultを使って新たな要素を集合に追加することができる。
visits.setdefault('France', set()).add('Arles')

if (japan := visits.get('Japan') ) is None:
    visits['Japan'] = japan = set()
japan.add('Kyoto')

print(visits) # {'Mexico': {'Tulum', 'Puerto Vallarta'}, 'Japan': {'Kyoto', 'Hakone'}, 'France': {'Arles'}}

# 自作の場合でも同様のことができる。
# 注意点：この実装例では呼び出しのたびに新たなsetインスタンスを作っているので非効率。
class Visits:
    def __init__(self):
        self.data = {}

    def add(self, country, city): # 上述の例をヘルパーメソッドでラップしている
        city_set = self.data.setdefault(country, set())
        city_set.add(city)

visits = Visits()
visits.add('Russia','Yekaterinburg')
visits.add('Tanzania','Zanzibar')
print(visits.data) # >>> {'Russia': {'Yekaterinburg'}, 'Tanzania': {'Zanzibar'}}

# collections.defaultdictにはキーが存在しない場合のデフォルト値を自動格納してこのユースケースを単純化する機能がある。
from collections import defaultdict
class Visits:
    def __init__(self):
        self.data = defaultdict(set)
    
    def add(self, country, city):
        self.data[country].add(city) # addの実装が短くなる。

visits = Visits()
visits.add('England', 'Bath')
visits.add('England', 'London')
print(visits.data) # >>> defaultdict(<class 'set'>, {'England': {'Bath', 'London'}})



