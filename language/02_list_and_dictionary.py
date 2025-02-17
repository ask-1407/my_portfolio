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

