fn main() {
    println!("Hello, world!")
}

// スラッシュ2つでコメントとみなせる
/*
複数行はこんな感じで書く
*/


// let 変数名＝値; にて変数を宣言する
let char_a = 'a'; //char型
let str_a = "a"; //&str型
let string_b = "b.to_string()"; //String型

// dbg!(変数名);を実行すると変数の値が出力される
let one =1;
dbg!(one);

// 以下のように書くと変数oneのスコープは関数内のみとなる。
fn main() {
    let one =1;
    dbg!(one);
}
