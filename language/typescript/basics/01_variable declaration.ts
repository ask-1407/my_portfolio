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

// 宣言時に型を指定することもできる。
const num: number = 123;

// 使い分け：基本的にはconstによって再代入を禁止し，意図しない書き換えを防ぐのがよい。

/*
varは以下の理由から使用しない。
- 同じ変数名を宣言すると後から宣言された変数が有効となる。
- グローバル変数として定義されたとき，windowオブジェクトのプロパティとして定義されるため既存のプロパティを上書きする危険性がある。
- 変数巻き上げによる予期せぬ動作
*/

// varならエラーはでない。xは宣言されているが値は代入されていない。
console.log(x); // undefined
var x = 10;
console.log(x); // 10

// letやconstなら参照エラー
console.log(y); // ReferenceError: Cannot access 'y' before initialization
let y = 20;
console.log(y);

console.log(z); // ReferenceError: Cannot access 'z' before initialization
const z = 30;
console.log(z);

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

/*
配列も読み取り専用として型注釈できる。以下2通りの方法がある。
1: readonlyキーワードを使う方法
2: ReadonlyArray<T>を使う方法
両者に違いはないので書き手の好みで選択する。
*/

//1: readonly number[]と書くと変数の型がnumberの読み取り専用になる。
const nums: readonly number[] = [1,2,3];

//2: ReadonlyArray<T> のような書き方でも読み取り専用の配列型になる。
const nums: ReadonlyArray<number> = [1, 2, 3];
 
/*
[特徴]
読み取り型配列では，pushやpopのような破壊的操作がコンパイル時にない扱いとなるため
呼び出そうとするとＴypeScriptコンパイラーに警告される。
*/
const nums: readonly number[] = [1, 2, 3];
nums.push(4); //Property 'push' does not exist on type 'readonly number[]'.


// 代入はコンパイルエラー
const readonlyNumbers: readonly number[] = [1, 2, 3];
const writableNumbers: number[] = readonlyNumbers;// The type 'readonly number[]' is 'readonly' and cannot be assigned to the mutable type 'number[]

// どうしても読み取り専用配列を普通の配列に代入したいときは、型アサーション(type assertion)を使う
const readonlyNumbers: readonly number[] = [1, 2, 3];
const writableNumbers: number[] = readonlyNumbers as number[];

//constアサーション：as const

// 変数宣言時にas constをつけるとreadonlyにしたうえでリテラル型にする。
const arrasyAsConst = [1, 2, 3] as const;

const pokemon = {
    name: "pikachu",
    no: 25,
    genre: "mouse pokemon",
    height: 0.4,
    weight: 6.0,
} as const;

/*
[違い] 
- readonlyはプロパティごとにつけることができる，
‐ const assertionは再帰的にreadonlyにできる。
*/
type Country = {
    name: string;
    capitalCity: string;
};
   
type Continent = {
    readonly name: string;
    readonly canada: Country;
    readonly us: Country;
    readonly mexico: Country;
};
   
const america: Continent = {
    name: "North American Continent",
    canada: {
      name: "Republic of Canada",
      capitalCity: "Ottawa",
    },
    us: {
      name: "United States of America",
      capitalCity: "Washington, D.C.",
    },
    mexico: {
      name: "United Mexican States",
      capitalCity: "Mexico City",
    },
  };

/*
型推論：Type inference
- コンパイラが型を自動で推論する機能。

[利点]
‐ 型注釈を省略できるので、コードの記述量を減らせる利点がある

[ユースケース]
‐ 初期値による推論: 変数の宣言時に明らかな初期値が代入されている場合、その初期値の型から変数の型を推論できる。
‐ 関数の戻り値：関数内で return される値の型から、関数の戻り値の型を推論できる。
― 構造的な型推論： TypeScriptはオブジェクトの構造に基づいて型を推論する能力を持っているためインターフェースや型エイリアスを明示的に宣言しなくても、オブジェクトの形状から型を推論できる
*/
let x = 1; // let x: number = 1;と同じ意味になる
x = "hello"; // Type 'string' is not assignable to type 'number'.