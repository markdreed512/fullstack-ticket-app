import React from 'react'
import { Form } from "semantic-ui-react"
const handleSubmit = (e) => {
    e.preventDefault()
    console.log(e.target)
}
const SignUpForm = () => {
    return (
        <Form onSubmit={handleSubmit} style={{width: "50%"}}>
            <input placeholder="username"/>
            <input placeholder="password"/>
            <input placeholder="password"/>
            <button>Sign Up</button>
        </Form>
    )
}

export default SignUpForm