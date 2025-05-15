/*
各種スコープは以下の通り
- グローバルスコープ
- ローカルスコープ
 - 関数スコープ
 - レキシカルスコープ
 - ブロックスコープ

グローバルスコープはどこからでも参照できる。
windowオブジェクトがグローバルオブジェクトとなっている。windowオブジェクトのプロパティへのアクセスはwindowを省略できる。
varを使って変数宣言するとグローバルになるが非推奨。
*/ 
　
Date === window.Date;
console === window.console;

// 関数スコープ
function func() {
    const variable = 123;
    return variable; // 参照可
}
console.log(variable); // 参照不可

// レキシカルスコープ：関数を定義した地点から参照できる関数外の変数のこと。
const x = 100;
function a() {
    console.log(x); // 関数外の変数が見える。
}
a(); // => 100

// ブロックスコープ：ブレース{ }で囲まれた範囲だけ有効なスコープ。ブロックの外から参照できません。
{if (navigator.userAgent.includes("Firefox")) {
    const browser = "Firefox";
  } else {
    const browser = "Firefox以外";
  }
  console.log(browser); // 参照できずエラー
    const x = 100;
    console.log(x); // => 100
}
console.log(x); // 参照できない。ReferenceError: x is not defined

// if-else

let result;
if (value === 0) {
  result = "OK";
} else {
  result = "NG";
}

// 式で条件分岐を使いたいときは三項演算子を使う
const result = value === 0 ? "OK" : "NG"; // valueが0ならOK、そうでなければNG

// こういう書き方はできない
const result = if (value === 0) "OK" : "NG";

/*
for-of, 拡張for: 構文はPythonのfor inに似ている
*/ 
const numbers = [1, 2, 3];
for (const n of numbers) {
  console.log(n);
}

// for-ofでインデックスを取得するにはentriesメソッドを使う。
const words = ["apple", "banana", "orange"];
for (const [index, word] of words.entries()) {
  console.log(index, word)
}

// breakで中断、continueで次のループにスキップする
const arr = ["1","2","3"];
for (let i = 0; i < arr.length; i++) {
  if (arr[i] === "a") {
    continue;
  
  if (arr[i] === "b") {}
   break;
  }
  console.log(arr[i])
}



// for-inは順番通りなる保証がないため利用しない。