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