# 7-3 圧縮ファイルの利用

# tarを開く
import tarfile
with tarfile.open('test.tar.gz','w:gz') as tr:
    tr.add('test_dir')


# tarファイルをPythonスクリプトで展開するにはモードをr:gzで開く
with tarfile.open('test.tar.gz','r:gz') as tr:
    tr.extractall('test_dir')

# ファイルを展開せずにread()で見ることもできる
with tarfile.open('test.tar.gz','r:gz') as tr:
    with tr.extractall('test_dir/sub_dir/sub_test.txt') as f:
        print(f.read())

# ZIPを扱うにはzipfileを利用する
import zipfile
with zipfile.ZipFile('test.zip', 'w') as z:
    z.write('test_dir') # ディレクトリのみでは空が圧縮される
    z.write('test_dir/test.txt')

# 対象のディレクトリやファイルをまとめて指定したいときはglobを利用する
import glob
with zipfile.ZipFile('test.zip', 'w') as z:
    for f in glob.glob('test_dir/**', recursive=True): # recursiveでtest_dir配下を再帰的に取得する。
        z.write(f)
    
# zipファイルをPython処理で展開するにはモードをrに指定してopenし，extractallを利用する。
with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('zzz2')

# ファイルを展開せずに中身を確認することもできる
with zipfile.ZipFile('test.zip', 'r') as z:
    with z.open('test_dir/test.txt') as f:
        print(f.read())