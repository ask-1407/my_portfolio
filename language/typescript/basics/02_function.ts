// 関数宣言

// 関数宣言の引数と戻り値に型注釈を書くことができる。
function increment(num: number): number {//引数の型注釈を省くとany型とみなされる。
    return num + 1;
}

// 戻り値の型注釈を省略した場合、コンパイラーがコードから型推論します。
function increment(num: number) {
    return num+1;
}

// returnが複数あり違う型を返している場合推論される型はユニオン型になります。
function getFirst(items: number[]){
    if (typeof items[0] === "number") {
        return items[0];
    }

    return null;
}

getFirst([1, 2, 3]); //function getFirst(items: number[]): number | null

// 関数式の構文: 変数に関数を代入する
const increment = function (n: number) {
    //                         ^^^^^^^^引数の型注釈. 省略するとany型になる
    return n + 1;
  };


// 戻り値の注釈も書ける。
const getZero = function (): number {
    //                         ^^^^^^戻り値の型注釈
    return 0;
  };
  
// 関数式をオブジェクトのプロパティに代入することもできる。
const オブジェクト = {
    メソッド名: function () {},
  };


/*
アロー関数: JavaScriptの関数を作る方法
- 関数式・関数宣言がもともとあったのに後発として加えられた。
- 機能上の違いはほぼないが，構文の簡潔するために実装された。
*/

// 書き方は以下の通り。
(引数) => {
    // 処理内容
  };

// 関数式
const increment = function (n) {
    return n + 1;
};

// アロー関数
const increment = (n) => {
    return n + 1;
  };


// 引数が一つなら引数のカッコが省略できる。
const increment = n => {/**/};
// 

//型注釈をつけた場合は以下。
const increment = (num: number) => num + 1;
//                    ^^^^^^^^引数の型注釈

const increment = (num: number): number => num + 1; // 返り値に着けた場合。

// 従来の関数(関数式)
[1, 2, 3].map(function (n) {
    return n + 1;
  });
// アロー関数
[1, 2, 3].map((n) => n + 1);

/*
オプション引数：渡す引数を省略する。TypeScript固有の機能。
- オプション引数の型は型とundefinedのユニオン型となる。
- T | undefined型の引数は引数が省略できないが，オプション引数であれば省略が可能。
- オプション引数の後に普通の引数はかけない。
*/

//書き方
function 関数名(引数名?: 型) {}
//                  ^オプション引数の標示

// プション引数を使用する際には、undefined である可能性を考慮した処理を書く必要がある。
function hello(person?: string) {
    if (typeof person === "undefined") { // if文でデフォルト値を入れ込む。※こういうパターンならデフォルト引数を使ったほうが早い。
      person = "anonymous";
    }
    return "Hello " + person.toUpperCase();
  }

/*
デフォルト引数: 引数の値がundefinedのとき、代わりの値を指定できる
・JavaScriptのデフォルト引数は引数がundefinedのとき使われる値
・構文: function 関数名(引数: 型 = デフォルト値) {}
・nullのときはデフォルト値にならない
・引数の途中に書ける
・簡単な初期化処理も書ける
・TypeScriptでは型推論が効く
*/ 

// 構文
function 関数名(引数: 型 = デフォルト値) {}
// アロー関数
(引数: 型 = デフォルト値) => {};

// 次の例では引数xがundefinedで，デフォルト値は1が入る。
function foo(x = 1) {
    console.log(x);
  }
foo(); // => 1

// 引数にundefinedを渡す場合もデフォルト値が代入される。
foo(undefined); // => 1

// 引数がnullのときはデフォルト引数は適用されない。
foo(null); // => null

// TypeScriptではデフォルト引数があると引数の型推論が効く。
function foo(x = 1) {}
//           ^ (parameter) x: number

/*
残余引数：引数の個数が決まっていない引数のこと。いわゆる可変長引数。
*/

// 構文
function func(...params: number[]) {
    // ...
}

/*
配列を残余引数に渡す。
- 残余引数、引数受取時には配列になりますが、関数呼び出しのときにひとつの配列にまとめて渡すことはできません。
- 配列を余剰引数に渡す場合は、スプレッド構文(spread syntax)を用います。
*/ 
const scores: number[] = [1, 2, 3, 4, 5];
const highest = Math.max(...scores) // => 5

/*
this引数
- アロー関数以外の関数とクラスのメソッドの第一引数は特殊な引数"this"を受けることができる。
- Python の self に近い概念
*/ 

class Male{
    private name: string;

    public constructor(name: string) {
        this.name = name;
    }

    public toString(); string {
        return `Monsieur ${this.name}`;
    }
};

class Female {
    private name: string;

    public constructor(name: string) {
        this.name = name;
    }
    public toString(this: Female): string{
        return `Madame &{this.name}`
    }
};

// どちらも普通の用途は同じように使える。
const male: Male = new Male("Taro");
const female: Female = new Female("Hanako");

male.toString(); // Monsieur Taro
female.toString(); // Madame Hanako

// インスタンスのtoString()を変数に代入すると意味が変わる。
const maleToStr: () => string = male.toString;
const femaleToStr: (this: Female) => string = female.toString;
 
maleToStr();
femaleToStr(); // The 'this' context of type 'void' is not assignable to method's 'this' of type 'Female'.

/*
[型ガード関数]
- ある変数が特定の型であることをコンパイラに明示的に伝えることができ、型に関するエラーを未然に防ぐことができます。
- これにより、より安全で信頼性の高いコードを書くことができるようになります。
- typeof や instanceof がTypeScriptが提供する型ガードだが、ユーザーで定義することもできる。
*/ 

// ユーザー定義の型ガード関数では型述語(型の性質や関係性を表明したり、検査したりするための仕組み)を使用する。
function isDuck(animal: Animal): animal is Duck { // animal is Duckが型述語。戻り値がboolean型の関数に対して適用できる。
    return animal instanceof Duck;
}

animal.quacks(); // ここではquacks()は存在しない。Property 'quacks' does not exist on type 'Animal'.

if (isDuck(animal)) {
  animal.quacks(); // OK
}

/*
[コールバック関数]
- 関数の引数として渡される関数のこと。設計パターンの一つ。
- 関数の中で引数で指定した関数を呼び出す（コールバックする）ことで関数の振る舞いを制御したり、非同期な結果を受け取ることができます。
*/ 

// 例：greetNewUserはhello関数とgoodMorning関数をいそれぞれコールバック関数として渡すことで挨拶の内容を変える。
function greetNewUser(func: (name: string) => string) {
  console.log(func("ご新規"));
}

function hello(name: string){
  return "こんにちは! ${name}さん";
}

function goodMorning(name: string){
  return "おはようございます！${name}さん";
}

greetNewUser(hello);
greetNewUser(goodMorning);

// 非同期処理でもコールバック関数は利用される。
// 例：Node.jsのfsモジュールのファイル読み込みのサンプルコード
import fs from "fs";
 
fs.readFile("./user.txt", "utf-8", (err, data) => {
  if (err) {
    console.error(err);
  }
  console.log(data);
});

// コールバック関数地獄：ネストが深くなり可読性が低下する問題のこと. 
// 非同期的にファイルを3回連続で読み込む処理
import fs from "fs";
 
fs.readFile("./a.txt", "utf-8", (err, data) => {
  fs.readFile(data, "utf-8", (err, data) => {
    fs.readFile(data, (err, data) => {
      console.log(data);
    });
  });
});

// Promiseを利用することで解消可能。
import { promises as fs} from "fs";
fs.readFile("a.txt", "utf-8")
  .then( (data) => fs.readFile(data, "utf-8"))
  .then( (data) => fs.readFile(data, "utf-8"))
  .then( (data) => console.log(data));

/*
コールバック関数には同期型と非同期型が存在します。
- 同期型：親の関数が処理を完了するまでの間に、その場で順番に実行される
- 非同期型：親の関数が処理を開始した後、すぐに完了するとは限らない処理の結果を受け取るために使われる
*/ 

// 同期型の例
const numbers = [1,2,3];
const doubles = numbers.map((n: number)=>{
  return n*2;
});
console.log(doubles); // [2, 4, 6]


// 非同期型の例
setTimeout(() => {
  console.log("This is a callback function!");
} , 1000);

console.log("hello");
// hello 
// This is a callback function!

