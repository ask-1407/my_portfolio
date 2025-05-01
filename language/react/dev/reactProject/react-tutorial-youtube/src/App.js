import { useState, useRef } from "react";
import TodoList from "./TodoList";

function App() {
  const [todos, setTodos] = useState([
    {id:1, name:"Todo1",completed: false},
  ]); //constの変数を管理
  
  const todoNameRef = useRef(); //要素を取得する

  const handleAddTodo = () =>{
    //タスクを追加する
    const name = todoNameRef.current.value;
    
    //これがTodosの更新を担う。
    setTodos((prevTodos)=> {
      return [...prevTodos, {id: "1", name: name, completed: false}]; //前のタスクに対し新しいタスクオブジェクトを追加
    })
    todoNameRef.current.value=null;
  };

  return (
    <div>
      <TodoList todos={todos} />
      <input type = "text" ref = {todoNameRef}/>
      <button onClick={handleAddTodo}>タスクを追加</button>
      <button>完了したタスクの削除</button>
      <div>残りのタスク:0</div>
    </div>
  );
}

export default App;
