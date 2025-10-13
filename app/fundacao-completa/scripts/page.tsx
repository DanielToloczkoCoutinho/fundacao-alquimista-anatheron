"use client";
import React from 'react';

export default function ScriptsPage() {
  return (
    <div style={{ 
      padding: '30px', 
      fontFamily: 'Arial, sans-serif',
      maxWidth: '1000px',
      margin: '0 auto',
      background: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
      minHeight: '100vh',
      color: 'white'
    }}>
      <div style={{ marginBottom: '30px' }}>
        <a 
          href="/fundacao-completa"
          style={{
            color: 'white',
            textDecoration: 'none',
            padding: '10px 20px',
            background: 'rgba(255,255,255,0.2)',
            borderRadius: '5px'
          }}
        >
          ← Voltar para Fundação Completa
        </a>
      </div>

      <h1 style={{ fontSize: '2.5rem', marginBottom: '10px' }}>⚡ SCRIPTS ALQUÍMICOS</h1>
      <p style={{ fontSize: '1.2rem', opacity: '0.9' }}>
        Scripts Python e Shell da Fundação Alquimista
      </p>

      <div style={{
        background: 'rgba(255,255,255,0.1)',
        padding: '25px',
        borderRadius: '15px',
        marginTop: '30px',
        backdropFilter: 'blur(10px)'
      }}>
        <h2>🛠️ Categorias de Scripts</h2>
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))',
          gap: '15px',
          marginTop: '20px'
        }}>
          <div style={{
            background: 'rgba(255,255,255,0.2)',
            padding: '15px',
            borderRadius: '8px',
            textAlign: 'center'
          }}>
            <div style={{ fontSize: '2rem', marginBottom: '10px' }}>🔄</div>
            <h3 style={{ margin: '0' }}>Sincronização</h3>
          </div>
          
          <div style={{
            background: 'rgba(255,255,255,0.2)',
            padding: '15px',
            borderRadius: '8px',
            textAlign: 'center'
          }}>
            <div style={{ fontSize: '2rem', marginBottom: '10px' }}>🔒</div>
            <h3 style={{ margin: '0' }}>Segurança</h3>
          </div>
          
          <div style={{
            background: 'rgba(255,255,255,0.2)',
            padding: '15px',
            borderRadius: '8px',
            textAlign: 'center'
          }}>
            <div style={{ fontSize: '2rem', marginBottom: '10px' }}>📊</div>
            <h3 style={{ margin: '0' }}>Análise</h3>
          </div>
          
          <div style={{
            background: 'rgba(255,255,255,0.2)',
            padding: '15px',
            borderRadius: '8px',
            textAlign: 'center'
          }}>
            <div style={{ fontSize: '2rem', marginBottom: '10px' }}>🚀</div>
            <h3 style={{ margin: '0' }}>Deploy</h3>
          </div>
        </div>
      </div>

      <div style={{
        marginTop: '30px',
        padding: '20px',
        background: 'rgba(255,255,255,0.1)',
        borderRadius: '10px',
        textAlign: 'center'
      }}>
        <p>⚡ <strong>75 scripts</strong> disponíveis na Fundação</p>
        <p>🐍 Python + Shell scripts operacionais</p>
      </div>
    </div>
  );
}
