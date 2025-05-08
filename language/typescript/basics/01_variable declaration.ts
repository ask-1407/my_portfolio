// 変数宣言：letを用いた方法

//書き方
let x = 1; 
x = 2; //letは再代入が可能。

let x; // 初期値なしで宣言し
x = 1;

// 変数宣言：constを用いた方法
const obj = { a: 1 };
obj = { a: 2 }; // 再代入は不可
obj.a = 2; // プロパティの変更はできる

// 使い分け：基本的にはconstによって再代入を禁止し，意図しない書き換えを防ぐのがよい。

// readonlyプロパティをつけると読み取り専用になる。
let obj: {
    readonly foo: number;
};
obj = { foo: 1 };
obj.foo = 2;

// 再帰的には適用されないので子や孫にもreadonlyをつける。
let obj: {
    readonly foo: {
      readonly bar: number;
    };
  };

// ユーティリティ型のRadonlyを使えば一括で変更できる。
let obj: Readonly<{
    a: number;
    b: number;
    c: number;
    d: number;
    e: number;
    f: number;
  }>;

/*
読み取り専用指定を受けたプロパティがチェックを受けるのはコンパイル時だけであり
コンパイルされた後のJavaScriptとしては、readonlyがついていたプロパティも代入可能になる。
*/

// 配列の場合：変数自体の再代入はできません。しかし、配列要素は変更できます
const arr = [1, 2];
arr = [3, 4]; // 再代入は不可
arr.push(3); // 要素の変更はできる