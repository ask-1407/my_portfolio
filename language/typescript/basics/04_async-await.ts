
// Promise<T>: 非同期処理の結果を表すことができる。

/*
以下の例を考える。
API1: リクエストを送り、結果を受け取る
API2: API1の結果を使ってリクエストを送り、結果を受け取る
API3: API2の結果を使ってリクエストを送り、結果を受け取る
*/

//　Promiseがないときは以下のように実現する
// API1. 非同期でAPIにリクエストを送って値を取得する処理
function request1(callback) {
    setTimeout(() => {
        callback(1); // 1は適当な値
    }, 1000);
}

// API2. 受け取った値を別のAPIにリクエストを送って値を取得する処理
function request2(result1, callback) {
    setTimeout(() => {
        callback(result1 + 1);
    }, 1000);
}

// API3. 受け取った値を別のAPIにリクエストを送って値を取得する処理
function request3(result2, callback){
    setTimeout(() => {
        callback(result2 + 1);
    }, 1000);
}

// API1~3を組み合わせる
request1((result1) => {
    request2(result1, (result2) => {
        request3(result2, (result3) => {
            console.log(result3); // 3
        });
    });
});

// Promiseを使った場合
function request_1() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(1);
        }, 1000);
    });
}

function request_2(result_1){
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(result_1 + 1);
        }, 1000)
    })
}

function request_3(result_2){
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(result_2 + 2);
        }, 1000)
    })
}

// Promiseを使うことで非常にすっきりする。
request_1()
    .then((result_1) => {
        return request_2(result_1);
    })
    .then((result_2) => {
        return request_3(result_2);
    })
    .then((result_3) => {
        console.log(result_3);
    })