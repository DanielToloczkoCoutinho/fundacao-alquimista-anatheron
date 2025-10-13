import React from 'react';

export default function SignInPage() {
  return (
    <div style={{ 
      padding: '40px', 
      fontFamily: 'Arial, sans-serif',
      textAlign: 'center',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      minHeight: '100vh',
      color: 'white'
    }}>
      <h1 style={{ fontSize: '2.5rem', marginBottom: '20px' }}>
        🔐 Fundação Alquimista
      </h1>
      <p style={{ fontSize: '1.2rem', marginBottom: '30px' }}>
        Sistema de Autenticação Segura
      </p>
      
      <div style={{
        background: 'rgba(255,255,255,0.1)',
        padding: '30px',
        borderRadius: '15px',
        maxWidth: '400px',
        margin: '0 auto',
        backdropFilter: 'blur(10px)'
      }}>
        <h2 style={{ marginBottom: '20px' }}>Acesso ao Sistema</h2>
        
        <div style={{ marginBottom: '15px' }}>
          <input 
            type="text" 
            placeholder="Usuário"
            style={{
              width: '100%',
              padding: '12px',
              border: 'none',
              borderRadius: '8px',
              marginBottom: '10px'
            }}
          />
        </div>
        
        <div style={{ marginBottom: '20px' }}>
          <input 
            type="password" 
            placeholder="Senha"
            style={{
              width: '100%',
              padding: '12px',
              border: 'none',
              borderRadius: '8px',
              marginBottom: '10px'
            }}
          />
        </div>
        
        <button
          style={{
            width: '100%',
            padding: '12px',
            background: '#4CAF50',
            color: 'white',
            border: 'none',
            borderRadius: '8px',
            fontSize: '16px',
            cursor: 'pointer'
          }}
        >
          🌌 Acessar Sistema
        </button>
        
        <div style={{ marginTop: '20px', fontSize: '14px', opacity: '0.8' }}>
          <p>Credenciais de teste:</p>
          <p>Usuário: <strong>zennith</strong> | Senha: <strong>quantum966</strong></p>
        </div>
      </div>
    </div>
  );
}
