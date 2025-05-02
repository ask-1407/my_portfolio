import React from 'react';
import './App.css'
import { useState } from 'react';

function App() {
  const [inputValue, setInputValue] = useState("");
  const [todos, setTodos] =useState<Todo[]>([]);

  type Todo = { // Todoは以下3つの要素をもつ。
    inputValue: string;
    id: number;
    checked: boolean;
  };

  // handleChangedは引数eを受け取る。なお型を指定しないとErrorをはく。※TypeScript特有
  const handleChanged = (e: React.ChangeEvent<HTMLInputElement>) => {
    //console.log(e.target.value);
    setInputValue(e.target.value)
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault(); // ページのリロードを防ぐ

    // 新しいTodoを作成
    const newTodo: Todo = {
      inputValue: inputValue,
      id: todos.length, //　本来ならUnique IDを指定する
      checked: false
    };

    setTodos([newTodo, ...todos]); //スプレッド構文で展開しnewTodoを追加。
    setInputValue("");

  };

  return (
    <div className="App">
      <div>
        <h2> Todoリスト with TypeScript</h2>
        {/* フォーム入力欄 */}
        <form onSubmit = {(e) => {handleSubmit(e)}}>
         <input type = "text" onChange={(e) => {handleChanged(e)}} className="inputText"/>
         <input type = "submit" value="作成" className='submitButton'/>
        </form>
        {/* ToDoリストの表示 */}
         <ul>
           {todos.map( (todo) => (
            <li>  {todo.inputValue} </li>
           ))}
         </ul>
      </div>
    </div>
  );
}

export default App;
