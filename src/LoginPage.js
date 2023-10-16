import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Form, FormGroup, Label, Input, Button } from 'reactstrap'; // Import Reactstrap components
import './Login.css'; // Import the CSS file

function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = () => {
    // Perform authentication logic here
    // For simplicity, let's assume a successful login for any username and password
    navigate('/foodlisting'); // Redirect to /foodlisting on successful login
  };

  return (
    <div className="container">
      <h2>Login</h2>
      <Form>
        <FormGroup>
          <Label for="username">Username:</Label>
          <Input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="password">Password:</Label>
          <Input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </FormGroup>
        <Button color="primary" onClick={handleLogin}>
          Login
        </Button>
      </Form>
    </div>
  );
}

export default LoginPage;