import React from 'react';
import logo from './logo.svg';
import './App.css'
import { useState } from 'react';

function App() {
  const [inputValue, setInputValue] = useState("");
  const [todos, setTodos] =useState<Todo[]>([]);

  type Todo = { // Todoは以下3つの要素をもつ。
    inputValue: string;
    id: number;
    checked: boolean;
  }

  // handleChangedは引数eを受け取る。なお型を指定しないとErrorをはく。※TypeScript特有
  const handleChanged = (e: React.ChangeEvent<HTMLInputElement>) => {
    //console.log(e.target.value);
    setInputValue(e.target.value)
  }

  return (
    <div className="App">
      <div>
        <h2> Todoリスト with TypeScript</h2>
        <form onSubmit = {() => {}}>
         <input type = "text" onChange={(e) => {handleChanged(e)}} className="inputText"/>
         <input type = "submit" value="作成" className='submitButton'/>
        </form>
      </div>
    </div>
  );
}

export default App;
