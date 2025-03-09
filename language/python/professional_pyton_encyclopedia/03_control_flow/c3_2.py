# 値の判定
is_ok = 0

if is_ok: # 0以外の数値ならTrueとなる
    print('OK') # 
else:
    print('NO')

is_ok = ''

if is_ok: # 空の文字列ならFalse
    print('OK') # 
else:
    print('NO')

# Noneを判定するテクニック

is_empty = None
if is_empty is None: # Noneであることを判定
    print('None')

if is_empty is not None: # Noneでないことを判定
    print('None')

# 複数のリストをまとめるときにはZIP関数が使える
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple','banana','beer']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip[days, fruits, drinks]:
    print(day, fruit, drink)

# デフォルト引数でリストや辞書を使うときの注意事項
"""
空のリストをデフォルト引数で使いたいときはNoneを指定する。
関数の中でリストの変数がNoneである場合は初期化を行う。
これはリストが参照渡しであるため、複数回実行すると同じリストのアドレスが参照されてしまうためである。
"""
def sample_func(x, l=[]): #　リストlにxをappendする関数
    if l is None:
        l = [] # ここがないと複数回呼び出したときにバグの温床になる
    l.appemd(x)
    return l

r = sample_func(100)
print(r)
# この関数にxとlを両方渡すと動作する。

