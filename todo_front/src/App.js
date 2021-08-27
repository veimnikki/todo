import React from 'react';
import Block from './components/Block';
import './styles/style.css';

function App() {

  return(
      <div className="background">
        <h1>Todo List</h1>
        <h2>16.08-22.08</h2>
        <Block block={{title:'Monday', id: 1}}/>
        <Block block={{title:'Tuesday', id: 2}}/>
        <Block block={{title:'Wednesday', id: 3}}/>
        <Block block={{title:'Thursday', id: 4}}/>
        <Block block={{title:'Friday', id: 5}}/>
        <Block block={{title:'Saturday', id: 6}}/>
        <Block block={{title:'Sunday', id: 7}}/>
      </div>
  )
}

export default App;