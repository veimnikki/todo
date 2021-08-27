import React from 'react';
import PropTypes from 'prop-types';
import '../styles/style.css';
import TodoItem from './TodoItem';

function Tasks(props) {

    return (
        <div className="tasks">
            <ul>
                {props.todos.map(todo => {
                    return <TodoItem todo={todo} key={todo.id} onChange={props.onToggle}/>
                })}
            </ul>
        </div>
    );  
};

Tasks.propTypes = {
    todos: PropTypes.arrayOf(PropTypes.object).isRequired,
    onToggle: PropTypes.func.isRequired
}

export default Tasks;