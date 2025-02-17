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