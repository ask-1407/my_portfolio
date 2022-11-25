# my_portfolio

NLP_BERT.ipynbについて
ヘイトスピーチ検出の分析コンペティションに参加した際のコードです。
教師データ(約5000個)のテキストに対して1/0のラベルが振り分けられており、これをもとにモデルを作成し
テストデータ(約3000)を振り分けるというものです。

前処理としては改行コードの削除、半角全角の統一を実施しました。
BERTを採用した理由としてはこの分野ではSoTAであること、当初LightGBMで実装したものの思うようなスコアを得られなかったことがあげられます。

ReadME執筆時点ではF1スコアは0.56くらいなのでもう少し前処理を加える(ストップワード除去、形態素解析)や
ハイパラチューニングを実施することでスコアを伸ばせるのではないかと考えています。
