# 7-2 ファイルの便利な活用方法

# 以下の文字列を題材にする
s= """
Hi $name,
$contents
Have a good day
"""
# 標準ライブラリstringにあるTemplate関数を用いる
# substituteメソッドの引数に$で始まる部分に代入する文字列を指定する
# substituteの返り値をだすと，文字列の中の＄nameと$contentsが置き換わっている。
import string
t = string.Template(s)
contents = t.substitute(name='Mike',contents='How are you?')
print(contents)

"""
Hi Mike,
How are you?
Have a good day
"""

# formatメソッドやf-stringを使っても文字列の一部に他の値を入れることはできる。
# Template関数を使うと元となる文字列を読み込み専用にすることができる。他チームが作成した文章を扱う際に有効。


# CSVファイルへの書き込み
import csv



