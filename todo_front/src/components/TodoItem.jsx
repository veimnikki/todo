import React, { useContext } from 'react';
import PropTypes from 'prop-types';
import '../styles/style.css';
import Context from '../context';


function TodoItem({ todo, onChange }) {
    const { removeTodo } = useContext(Context)
    const classes = []
    
    if (todo.completed) {
        classes.push ('Done')
    }

    return (
        <li className="Li">
            <span className={classes.join(' ')}>
            <label class="custom-checkbox">
                <input 
                    type='checkbox'
                    checked={todo.completed} 
                    id='happy' 
                    value="value-1"
                    class="custom-checkbox" 
                    name="happy"
                    onChange={ () => onChange(todo.id) 
                }/>
                <span></span>
            </label>
                {todo.title}
            </span>
            <button id="close" onClick={() => removeTodo(todo.id)}>&times;</button>
        </li>
    );  
};

TodoItem.propTypes = {
    todo: PropTypes.object.isRequired,
    onChange: PropTypes.func.isRequired
}

export default TodoItem;