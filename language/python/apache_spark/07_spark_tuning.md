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
  - 単に動的リソース割り当てを有効にするだけでは不十分。Executorがメモリ不足に陥ったり，JVM GCに悩まされたりしないようにExecutorのメモリがどのように配置・使用されているかを理解する必要がある。
  - `spark.executor.memory`でExecutorのメモリを制御できる
    - 実行メモリ，ストレージメモリ，予約メモリの3つに分かれている。デフォルトでは60%,40％となっており300MBの予約メモリを確保している。
    - 実行メモリはSparkの`shuffle`,`join`,`sort`,`aggregation`に使用される。
    - `spark.memory.fraction`の値(デフォルト0.6)を変えると実行メモリの割り振りを調整できるが，クエリによって必要なメモリ量が異なるので実行メモリに割り当てる適切な値をチューニングするのは難しい。
    - ストレージメモリは主にユーザーのデータ構造やDataFrameから派生したpartitionのcacheに使用できる。
    - `map`と`shuffle`の操作中，Sparkはローカルディスクのshuffleファイルへの書き込みと読み取りを行うため激しいI/O操作が発生する。デフォルトのconfigは大規模なSpark Jobに最適でないためボトルネックになる可能性がある。以下の設定をみるとよし

| Configuration | 説明 |
| ---- | ---- |
| spark.driver.memory | Spark DriverがExecuterからデータを受け取るために割り当てられるメモリ量 |
| spark.shuffle.file.buffer | shuffle時にデータをバッファリングする一時的なメモリ領域サイズ。推奨1MB |
| spark.file.transferTo | false に設定するとSpark はファイルバッファを使用してファイルを転送し、最終的にディスクに書き込むため結果的にI/O 活動を減少させる. |
| spark.shuffle.unsafe.file.output.buffer | Shuffle中にファイルをMergeする際に可能なバッファリング量を制御する。 |
| spark.io.compression.lz4.blockSize | ブロックの圧縮サイズを大きくすることでshuffleファイルのサイズを小さくできる。<br>デフォルト32KBだが512KBまで増やせる。 |
| spark.shuffle.service.index.cache.size | シャッフル処理におけるインデックスファイルの読み取りに使うメモリの割り当て量を調整する<br>インデックスファイルはどのデータがどこに保存されているかを保持しているもので，タスクがこれを参照すると必要なデータがどこにあるかを特定できる |
| spark.shuffle.registration.timeout | 外部シャッフルサービスへの登録のタイムアウト。デフォルトは5000㎳で12000㎳まで増やせる。 |
| spark.shuffle.registration.maxAttempts | 外部シャッフルサービスへの登録に失敗した場合、maxAttempts回数だけリトライする。デフォルト3で5マデ増やせる |


- 並列処理の最大化
  - Sparkの効率性は複数のTaskを大規模に系列に実行する能力に依存する。並列処理の性能最大化には「Sparkがストレージからデータをメモリに読み込む方法」「Sparkにとってのpartition」を理解する必要がある
  - partition
    - partitionとは，設定可能かつ読み取り可能な塊やブロックのサブセットに配置する方法のことをさす。 これらのデータセットは必要に応じてプロセス内の1つ以上のスレッドによって独立して並行して読み取りまたは処理ができる
    - 大規模ワークロードの場合，Spark Jobは多くのStageを持ち，各Stageの中には多くのTaskが存在する。Sparkは1コアごと，Taskごとにスレッドをスケジュールし，各Taskは個別のparitionのデータを処理する
    - 並列性を最大化するにはExecutorのコア数と同じ数のpartitionが理想的である。コア数より多くのpartitionがあると全てのコアがビジー状態になる。
    - partitionは並列処理の最小単位ととらえることができる。1コアの1スレッドが1つのpartitionである
    - partitionのサイズは`spark.sql.files.maxPartitionBytes`によって決定する。デフォルトは128MB。小さなpartitionファイルがたくさんあるとI/Oが異常に多くなりパフォーマンスが低下する(スモールファイル問題)
  - shuffle partition
    - shuffleステージで作成される。デフォルトでは`spark.sql.shuffle.partitions`で200に設定されている。データセットのサイズに応じてこの数を調整するとExecutorのタスクに送信される小さなpartitionの量を減らすことができる。
    - 












