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