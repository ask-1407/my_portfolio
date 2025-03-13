# 7.1 効率化のためのSparkの最適化とチューニング

## 7.1.1 Apache Spark Configurationの表示と設定
Sparkのプロパティを取得・設定する方法は3つある.

1. 設定ファイルのセットを使用
   1. Sparkをインストールした場所(`SPARK_HOMEディレクトリ`)にはいくつかの設定ファイルがある。
   2. これらの各ファイルのデフォルト値を変更し，接尾辞である.templateを付けずに保存すると新しい値を適用される。
   3. なお`conf/spark-defaults.conf`の設定変更はSparkクラスタに送信される。
2. Sparkアプリケーションで直接Sparkの設定を指定
   1. spark-submitで--confフラグを使用して指定できる。
      1. コマンドラインでやる：`spark-submit --conf spark.sql.shuffle.partitions=5`
      2. pythonでやる場合
        ```python
            from pyspark.sql import SparkSession

            # SparkSessionの作成
            spark = SparkSession.builder.appName("ExampleApp").getOrCreate()

            # プロパティを設定
            spark.conf.set("spark.sql.shuffle.partitions", "50")

            # プロパティを取得
            shuffle_partitions = spark.conf.get("spark.sql.shuffle.partitions")

            print(f"spark.sql.shuffle.partitions: {shuffle_partitions}")

            # すべてのプロパティを取得
            all_conf = spark.conf.getAll()
            for key, value in all_conf.items():
                print(f"{key}: {value}")
        ```

3. Spark shellを介した方法
   1. SparkSessionはSparkのエントリポイントとなっているたあめこおからほぼ全ての設置にアクセスできる。
      1. 以下のようにかけば，Spark SQL固有のSpark Configのみを表示することもできる。
         1. `spark.sql("SET -v").select("key", "value"),show(n=5, truncate=False)`
      2. Spark UIの`Enviroment`タブから現在の設定にもアクセス可能。
      3. 変更可能なConfigはAPIで新しい値に設定可能。
         1. `spark.conf.get("spark.sql.shuffle.partitions")`
         2. `spark.conf.set("spark.sql.shuffle.partitions",5)`

## 7.1.2 大規模ワークロードのためのスケール
Sparkでリソースの枯渇やパフォーマンスの低下によるジョブの失敗をさけるために調整できる設定がある。
ここではリソースの使用率最適化，Task並列化，大量のTaskのボトルネックを回避するための調整について述べる。

- 静的リソース割り当てと動的リソース割り当て
  - `spark-submit`のコマンドライン引数で計算資源を指定すると，上限が設定される。
  - つまりワークロードが想定以上でTaskがDriverにキューイングされ後でより多くのリソースが必要になったとき，余分のリソースを割り当てられないことを意味する。
  - 代わりに動的リソース割り当て設定を使用すると需要の増減に応じてSpark Driverがコンピュートリソースを要求することができる。
  - データフロー量が不均一なストリーミングもしくはオンデマンドのデータ分析でピーク時に大量のSQLクエリを要するときに有効
  - `spark.dynamicAllocation`という値を設定することで利用可能。デフォルトでは`spark.dynamicAllocation = False`となっている。
- ExecutorのメモリとShuffleサービスの設定
  - 単に動的リソース割り当てを有効にするだけでは不十分。
  - Executorがメモリ不足に陥ったり，JVM GCに悩まされたりしないようにExecutorのメモリがどのように配置・使用されているかを理解する必要がある。
  - `spark.executor.memory`でExecutorのメモリを制御できる
    - 実行メモリ，ストレージメモリ，予約メモリの3つに分かれている。デフォルトでは60%,40％となっており300MBの予約メモリを確保している。
    - 実行メモリはSparkの`shuffle`,`join`,`sort`,`aggregation`に使用される。
    - `spark.memory.fraction`の値(デフォルト0.6)を変えると実行メモリの割り振りを調整できるが，クエリによって必要なメモリ量が異なるので実行メモリに割り当てる適切な値をチューニングするのは難しい。
    - ストレージメモリは主にユーザーのデータ構造やDataFrameから長谷井したpartitionのcacheに使用できる。



