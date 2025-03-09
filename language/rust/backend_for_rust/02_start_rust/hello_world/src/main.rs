fn main() {
    println!("Hello, world!");
    print!("\n");
    println!("Hello, Cargo!");
}

/*
- cargoコマンドでプロジェクトを作ることができ、tomlにcargoの設定ファイルができる。
- このファイルには追加でパッケージの情報を付与したり、依存関係を記述できる。
- Rustは実行前にコンパイルする必要がある。
- 該当のディレクトリで「cargo build」を実行するとコンパイルが実行される。
- 成功するとプロジェクト全体がビルドされ、実行可能ファイルがtarget/debugに生成される
- rustc ./your_script.rs にて指定したスクリプトをコンパイルする。
- ./your_script.rs　を実行すると、記載の内容が実行される。
*/

