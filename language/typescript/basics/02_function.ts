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

