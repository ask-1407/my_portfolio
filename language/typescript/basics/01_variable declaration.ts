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

[型推論と動的型づけの違い]
‐ 型推論：コンパイルのタイミングで型が決定される。その後変更されることはない。
‐ 動的型付け：実行時に型が決まる。ゆえに実行タイミングにより方が変化する。
*/
let x = 1; // let x: number = 1;と同じ意味になる
x = "hello"; // Type 'string' is not assignable to type 'number'.


// データ型：プリミティブ型とオブジェクトの二つに分類される。

/*
[プリミティブ型の特徴]
- Immutable
- プロパティをもたない
*/

null.toString(); // Error
"name".length; // 4. プリミティブ型をオブジェクトのように扱える(auto boxing)のはJavaScriptの特徴。

// boolean: trueかfalse ※大文字で始まるBoolean型があるがbooleanとは別の型。
const isOk = true; 
const isPandas = false;
const isOk: boolean = true; // 型推論

// number: 整数や少数などの数値。JavaScriptでは整数と少数を型レベルで区別しない。

100_000_000 // 一億。アンスコで数字を区切ることができる。

5.toString(); //小数点と区別できないので構文エラーとなる。以下２通りで実現可能。
5..toString(); 
(5).toString();

const count: number = 123; //型推論

//NanとInfinityはnumber型

/*
NanとInfinityはnumber型
- Nan：非数(not-a-number)を表す。JavaScriptでは、処理の結果、数値にならない場合にNaNを返すことがある
- Infinity：無限大。1を0で割るとこの値を返す。
*/
const price = parseInt("百円");
console.log(price); // NaN

// 値がNaNであるかどうかはNumber.isNaNを利用する。
if (Number.isNaN(price)) {
  console.log("数値化できません");
}

// string: クォートの如何に関わらず文字列となる。PHPと同様。
"Hello";
'Hello';
`Hello`;

// 文字列中に同じ引用符が含まれている場合はバックスラッシュでエスケープする。
'He said "madam, I\'m Adam."'
"He said \"madam, I'm Adam.\""

// バッククォートで囲ったものは式や変数を埋め込むことができる。
const count = 10;
console.log(`現在、${count}名が見ています。`);
`税込み${Math.floor(100 * 1.1)}円`

/*
[使い分け]
- 基本的に"を使用する
- 文字列の中に"が含まれる場合は'を使用する
- 文字列展開する必要があるときは`を使用する
*/

// 型推論
const message: string = "Hello"

/*
[型強制]
- 型が異なる2つの値に対し演算してもエラーにならない(別の型に暗黙的に変換される)ことがある。これを型強制という。
- どんな型に型強制されるかは演算子によっても異なる
*/ 
"1" - 1; //=> 0
"1" + 1; //=> "11"

/*
[ボックス化]
- プリミティブをオブジェクトへ変換しオブジェクトのように扱う操作のこと
- JavaScriptでは、プリミティブ型の値でもフィールドを参照できたり、メソッドが呼び出せます。
- 自動Box化で変換先となるオブジェクトのことを"ラッパーオブジェクト"とよぶ。
- TypeScriptではラッパーオブジェクト(例:String)よりもプリミティブ型(例:string)で型注釈すべし
*/ 
const str = "abc";
// オブジェクトのように扱う
str.length; // フィールドの参照
str.toUpperCase(); // メソッド呼び出し

// TypeScriptではラッパーオブジェクトの型をつかって型注釈をかける。プリミティブ型を代入することもできる。
const bool: Boolean = false;
const num: Number = 0;
const str: String = "";
const sym: Symbol = Symbol();
const big: BigInt = 10n;

// プリミティブ型にラッパーオブジェクトを代入することはできない。
const n1: Number = 0;
const n2: number = n1;

// ラッパーオブジェクト型は演算子が使えない
const num: Number = 1;
num * 2;

// ラッパーオブジェクト型を型注釈に使う利点はありません。型注釈にはプリミティブ型を使う。
const num1: Number = 0;// anti pattern
const num2: number = 0;// good

/*
any
・any型はどんな型でも代入を許す
・any型は型チェックされない
・型推論できない変数は暗黙的にany型になる
・anyは使いようによっては悪くない
・がんばらないTypeScriptという考え方もある
*/ 

// anyで宣言された変数はどんな型でも許容する。
let value: any;
value = 1; // OK
value = "string"; // OK
value = {name: "オブジェクト"}// OK

// anyはコンパイラが型チェックを行わないので実行時のエラーを指摘しない。
const str: any = 123;
str.toLowerCase(); // TypeError: str.toLowerCase is not a function

// tsconfig.json にて noImplicitAny: true を設定することで、TypeScriptが型をany型と推測した場合にエラーが発生するようになる。
function hello(name) {  //Parameter 'name' implicitly has an 'any' type.
  console.log(`Hello, ${name.toUpperCase()}`);
}

/*
any型を濫用すると型チェックが弱くなりバグの発見できなくなる恐れがある。
理由なくanyを使うのは問題ですが、どうしてもanyを使わないとならない場面や、型安全性を妥協した上で、まずは動くコードを形にすることを優先するといったこともありえます。
anyをどこまで許容するか、型チェックをどこまで厳格にするかは、チームの熟練度やプロジェクトの方針によるところが大きいです。
*/

//unknown型：型が何かわからないときに使う。APIレスポンスの型が不明だがとりあえず実装⇒わかったら適切な型に変えるのがまるそう。
//そのままだと使えないのでtypeofやinstanceofなどの条件式に含んだif文を使う。(型ガードと呼称)
const value: unknown = "";
if (typeof value === "string"){ // valueがstring型ならstring型のメソッドtoUpperCase()を使う
  console.log(value.toUpperCase());
}

// 型ガード関数を使う方法もある
function isObject(value: unknown): value is object {
  return typeof value === "object" && value !== null;
}
const value: unknown = { a: 1, b: 2 };
// 型ガード
if (isObject(value)) {
  // ここでは、valueをobject型として扱える
  console.log(Object.keys(value));
}