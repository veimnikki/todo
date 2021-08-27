import React from 'react';
import Context from '../context';
import '../styles/style.css';
import AddTodos from './AddTodos';
import Tasks from './Tasks';

const Block = (props) => {
    const [todos, setTodos] = React.useState ([]);

    function toggleTodo(id) {
        setTodos(todos.map(todo => {
            if (todo.id === id) {
                todo.completed = !todo.completed
            }
            return todo
        })
        )
    }

    function removeTodo(id) {
        setTodos(todos.filter(todo => todo.id !== id))
    }

    function addTodo(title) {
        setTodos(todos.concat([{
            title:title,
            id: Date.now(), 
            completed: false
        }]))
    }
    

    return (
        <Context.Provider value={{ removeTodo }}>
            {(props.block.id !== 5) ? 
                <div className="day"> 
                    {props.block.title}
                    <hr align="center" width="180px" color="#D0C0C0" size="2"/>
                    {todos.length ? <Tasks todos={todos} onToggle={toggleTodo}/> : <p className = 'none'>Задач нет<p className='addn'>Нажмите "добавить", чтобы добавить новые задачи</p></p>}
                    <AddTodos onCreate={addTodo} />    
                </div> : 
                <div className="day5"> 
                    {props.block.title}
                    <hr align="center" width="180px" color="#D0C0C0" size="2"/>
                    {todos.length ? <Tasks todos={todos} onToggle={toggleTodo}/> : <p className = 'none'>Задач нет<p className='addn'>Нажмите "добавить", чтобы добавить новые задачи</p></p>}
                    <AddTodos onCreate={addTodo} />    
                </div>
            }
        </Context.Provider>
    );
};

export default Block;