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

// 式と文
/* 
文：変数の宣言・束縛を行う。結果を返さない
式：評価されると結果を返す。
Rustの制御構文の多くは評価されると最終的に値を返すので式指向言語とよばれる。
*/

// 以下のように書くことで変数sixに計算結果が格納される。
let three = 1+2;
let six = three * 2;
dbg!(three); // => 3
dbg!(six); // => 6

// 不変性と可変性

//不変性”：一つの変数に再代入できない
let one = 1;
one = one*2; // cannot mutate immutable variable 'one' analyzer

/*
シャドーイング：同名の変数を改めて定義すること。
シャドーイング前とは全く関係のない別の変数となる。
*/ 
let one = "1": // これはOK. 

// Rustでは基本的に不変変数として定義されるがmut修飾子をつけると可変にできる
let mut one = 1:
one = one * 2:
dbg!(one); // 2が出力される