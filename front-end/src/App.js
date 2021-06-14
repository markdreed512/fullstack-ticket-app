import './App.css';
import React from 'react'
import NavBar from './components/NavBar'
import SignUpForm from './components/SignUpForm'
import 'semantic-ui-css/semantic.min.css'
function App() {
  return (
    <div >
      <NavBar />
     <SignUpForm />
    </div>
  );
}

export default App;
