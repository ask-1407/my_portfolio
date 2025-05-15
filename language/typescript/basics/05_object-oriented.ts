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