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



