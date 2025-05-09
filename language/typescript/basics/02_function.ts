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