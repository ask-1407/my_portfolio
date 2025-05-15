// Classの定義はclass構文を用いる。
class Person{} 

// newキーワードでオブジェクトを生成する。インスタンスを代入する変数に型注釈するには、クラス名を使います。
const person: Person = new Person("Alice")

// コンストラクタはクラスをnewしたときに実行される関数。
class Person {
    constructor(name: string) {
        // ...
    }
} // 戻り値はクラスのインスタンスとなるため型注釈できない。

// TypeScriptではコンストラクタを非同期化するにはクラスのインスタンスファクトリーメソッドを作成してそのメソッドの中で非同期処理を実行するようにする。
class Person {
    static async create(name: string): Promise<Person> {
        // 非同期処理
        return new Person(name);
    }
    constructor(name: string){
        // ...
    }
}

// フィールド：インスタンス化したオブジェクトのプロパティに値を代入することでフィールドを付与できる
class Person {
    name: string;

    constructor(name: string) {
        this.name = name;
    }
}
const alice = new Person();
alice.name = "Alice";

// クラスの宣言にかかれていないフィールドへのアクセスはコンパイルエラーになる。
console.log(alice.name); // "Alice"\
console.log(alice.age); //Property 'age' does not exist on type 'Person'.

// クラスに対してメソッドを実装できる
class Greeter {
    greet(name: string): string {
        return "Hello, ${name}";
    }
}

/*
アクセス修飾子
- 宣言なし:　publicと同等
- public: どこからでもアクセスできる
- protected: 自身のクラスとサブクラスからアクセス可能
- private: 自身のクラスのみアクセス可能

クラスの継承時にメソッドのアクセス修飾子を変更できる。ただしアクセス制限を緩める方向のみ。
*/ 

//　継承: extendsキーワードを用いてクラスの継承ができる。
class Parent{}
class Child extends Parent{
    constructor() {
        super();　//スーパークラスのコンストラクタを呼び出す
    }
}


// インターフェース: 構造の型を定義する。そのままだと実装の詳細をもたない。
interface SomeInterface {
    method1(): void;
    method2(): void;
}

// パブリックフィールドも定義できる
interface SomeInterface {
    field: string;
}