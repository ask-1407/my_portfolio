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

with open('test.csv','w', newline='') as csv_file: # windowsでは改行文字コードが\r\nとなるため読み込み時に2行改行される。newline=''を入れると解消される。
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()

# データ部分を書き込むにはwriterowメソッドに辞書型のデータを渡す。
with open('test.csv','w', newline='') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})

# DictReader関数を引数にcsvファイルを渡して読み込んでいく
with open('test.csv','r', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])

# 標準ライブラリosを使うと様々なファイル操作を実行できる
import os
print(os.path.exists('test.txt')) # 存在するならTrueを返す

# ファイルかどうかを確かめるにはisfileを，ディレクトリかどうかはisdirをつかう
print(os.path.isfile('test.txt'))
print(os.path.isdir('design')) 

# その他の操作
os.rename('test.txt', 'renamed.txt') # ファイル名の変更
os.symlink('renamed.txt','symlink.txt') # シンボリックリンクの作成
os.mkdir('test_dir') # ディレクトリ作成
os.rmdir('test_dir') # ディレクトリ削除 ※ディレクトリが空の時に利用できる。

# pathlibのtouchを使うと中身が空を作成できる。
import pathlib

pathlib.Path('empty.txt').touch()
os.remove('empty.txt') # ファイル削除
print(os.listdir('test_dir')) # 配下のディレクトリ表示

# glob関数でファイルの列挙が可能。
import glob
pathlib.Path('test_dir/test_dir2/empty.txt').touch()
print(glob.glob('test_dir/test_dir2/*'))

# shutil.copy()を使うとファイルのコピーができる
import shutil
shutil.copy('test_dir/test_dir2/empty.txt','test_dir/test_dir2/empty2.txt')

# shutil.rmtreeでディレクトリを削除できる(中身含む)
shutil.rmtree('test_dir')