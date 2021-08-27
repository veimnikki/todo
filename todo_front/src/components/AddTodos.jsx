import React, { useState }  from 'react'
import PropTypes from 'prop-types'
import '../styles/style.css';

function AddTodos({onCreate}) {
    const [value, setValue] = useState('')

    function submitHandler(event) {
        event.preventDefault()
        
        if (value.trim()) {
            onCreate(value)
            setValue('')
        }
    }

    return (
        <div>
            <div id='form-wrap'>
                <form onSubmit={submitHandler} action="/requestFine" autocomplete="off" method="POST">
                    <label />
                    <input value={value} onChange={event => setValue(event.target.value)} placeholder="добавить задачу" className='forma' />
                    <button className='ok' type='submit'>ok</button>
                </form>
            </div>
        </div>
    )
}

AddTodos.propTypes = {
    onCreate: PropTypes.func.isRequired
}

export default AddTodos
