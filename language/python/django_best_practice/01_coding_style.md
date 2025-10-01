出展: https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#model-style

# Pre-commit checks 
- pre-commitを利用することでコードをCommitする前に簡単な問題（コードのスタイルやフォーマット、あるいは基本的な構文の誤り）を検出・修正できる。
- これによりレビュワーはコードの変更に集中することができる。CIの実行回数を減らすことにも貢献する。
- 利用するには以下のコマンドでpre-commitとGitフックをインストールする。
```bash
$ python -m pip install pre-commit
$ pre-commit install
```

# Python style
- 全てのファイルはblackによってフォーマットされているべきである。
- インデントと空白の問題を回避するため、EditorConfig をサポートするテキストエディタの使用を推奨。
  - Python ファイルではインデントに 4 文字のスペースを使用し、HTML ファイルでは 2 文字のスペースを使用。
- 特に指定がない限りはPEP8に従う
  - flake8でチェックが可能だが一部チェックできないエラーもあるため注意すること
  - PEP8はあくまでガイドラインであるため、周囲のコードスタイルを尊重すること
- 文字列変数の補間では、コードの可読性を最大限に高めることを目的に、% フォーマット、f 文字列、または str.format() を適宜使用できる。
  - 可読性の最終的な判断は、 Merger’s discretio(コードをマージする権限を持つ人)に委ねられます。
  - 目安として、f 文字列では単純な変数およびプロパティへのアクセスのみを使用し、より複雑なケースでは事前にローカル変数の代入を行う必要があります。
```python
# Allowed
f"hello {user}"
f"hello {user.name}"
f"hello {self.user.name}"

# Disallowed
f"hello {get_user()}"
f"you are {user.age * 365.25} days old"

# Allowed with local variable assignment
user = get_user()
f"hello {user}"
user_days_old = user.age * 365.25
f"you are {user_days_old} days old"
```
- エラーメッセージやログメッセージなど、翻訳が必要となる可能性のある文字列には、f 文字列を使用しない。一般的に `format()` はより冗長なため、他のフォーマット方法が推奨されます。
- フォーマット方法を調整するために、既存のコードに関係のないリファクタリングを行う時間を無駄にしないでください。


# Imports
# Template style
# View style
# Model style
# Use of django.conf.settings
# Miscellaneous
# JavaScript style