# 7-4:一時ファイルの活用

# TemporaryFile関数を使うとPython側がI/Oバッファ上に一時ファイルを作成できる。
import tempfile
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# 実際に一時ファイルを作成したいときはNamedTemporaryFile関数を使う
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name) # 一時ファイルのパスを取得
    with open(t.name, 'w') as f:
        f.write('test')  

# 一時ディレクトリを作成するにはTemporaryDirectory関数を使う
with tempfile.TemporaryDirectory() as td:
    print(td) # 一時ディレクトリのパスを取得
temp_dir = tempfile.mkdtemp()

# 標準ライブラリのsuboprocessを使うとターミナル用のコマンドをPython上で実行できる。
import subprocess
subprocess.run(['ls', '-l'])

# run関数に引数にshell=Trueを指定するとリストを使わずに文字列コマンドを実行できる。
# LinuxやShellに詳しい人でないと難しいためコマンドがシンプルならリストを推奨する
subprocess.run('ls -al', shell=True)

# check=Trueを指定するとコマンドが正常に終了しなかった場合に例外を発生させる。
# リストに格納する方法ならPythonで例外が発生するのでそちらのほうがよい

subprocess.run('lsa', shell=True, check=True) # CallProcessError

# コマンドをリストに格納しつつパイプを使うにはPopenを使う
p1 = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'py'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)

# 時間にまつわるライブラリとバックアップファイル

import datetime
now = datetime.datetime.now()
print(now) # 2025-03-08 07:06:39.778548
print(now.isoformat()) # 2025-03-08T07:06:39.778548

# strftimeで表示形式をある程度設定可能
now = datetime.datetime.now()
print(now)
d = datetime.timedelta(weeks=-1)
print(now+d)

# time.sleepで指定した時間なにもしない
import time
time.sleep(2)

# time.time()でエポックタイムを表示できる
print(time.time())