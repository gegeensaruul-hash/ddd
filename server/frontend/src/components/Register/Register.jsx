import React, { useState } from 'react';

function Register() {
  const [formData, setFormData] = useState({
    username: '',
    firstName: '',
    lastName: '',
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Registered:', formData);
  };

  return (
    <div style={{ maxWidth: '400px', margin: '50px auto', padding: '30px', border: '1px solid #ddd', borderRadius: '8px' }}>
      <h2>Sign Up</h2>
      <div style={{ marginBottom: '15px' }}>
        <label>Username</label>
        <input type="text" name="username" value={formData.username} onChange={handleChange}
          style={{ width: '100%', padding: '8px', marginTop: '5px', border: '1px solid #ccc', borderRadius: '4px' }} />
      </div>
      <div style={{ marginBottom: '15px' }}>
        <label>First Name</label>
        <input type="text" name="firstName" value={formData.firstName} onChange={handleChange}
          style={{ width: '100%', padding: '8px', marginTop: '5px', border: '1px solid #ccc', borderRadius: '4px' }} />
      </div>
      <div style={{ marginBottom: '15px' }}>
        <label>Last Name</label>
        <input type="text" name="lastName" value={formData.lastName} onChange={handleChange}
          style={{ width: '100%', padding: '8px', marginTop: '5px', border: '1px solid #ccc', borderRadius: '4px' }} />
      </div>
      <div style={{ marginBottom: '15px' }}>
        <label>Email</label>
        <input type="email" name="email" value={formData.email} onChange={handleChange}
          style={{ width: '100%', padding: '8px', marginTop: '5px', border: '1px solid #ccc', borderRadius: '4px' }} />
      </div>
      <div style={{ marginBottom: '15px' }}>
        <label>Password</label>
        <input type="password" name="password" value={formData.password} onChange={handleChange}
          style={{ width: '100%', padding: '8px', marginTop: '5px', border: '1px solid #ccc', borderRadius: '4px' }} />
      </div>
      <button onClick={handleSubmit}
        style={{ width: '100%', padding: '10px', background: '#6c63ff', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', fontSize: '16px' }}>
        Register
      </button>
    </div>
  );
}

export default Register;