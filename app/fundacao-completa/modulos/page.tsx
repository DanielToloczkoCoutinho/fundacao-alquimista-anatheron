"use client";
import React from 'react';

export default function ModulosPage() {
  return (
    <div style={{ 
      padding: '30px', 
      fontFamily: 'Arial, sans-serif',
      maxWidth: '1000px',
      margin: '0 auto',
      background: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
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

      <h1 style={{ fontSize: '2.5rem', marginBottom: '10px' }}>🔧 MÓDULOS OPERACIONAIS</h1>
      <p style={{ fontSize: '1.2rem', opacity: '0.9' }}>
        Sistemas especializados da Matriz LUX.NET
      </p>

      <div style={{
        background: 'rgba(255,255,255,0.1)',
        padding: '25px',
        borderRadius: '15px',
        marginTop: '30px',
        backdropFilter: 'blur(10px)'
      }}>
        <h2>🏗️ Módulos Principais</h2>
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
          gap: '15px',
          marginTop: '20px'
        }}>
          <div style={{
            background: 'rgba(255,255,255,0.2)',
            padding: '20px',
            borderRadius: '10px'
          }}>
            <h3 style={{ margin: '0 0 10px 0' }}>👑 Módulo 29</h3>
            <p style={{ margin: '0', fontSize: '14px' }}>
              Governança Zennith Rainha
            </p>
            <a 
              href="/modulo-29"
              style={{
                display: 'inline-block',
                marginTop: '10px',
                padding: '5px 10px',
                background: 'rgba(255,255,255,0.3)',
                color: 'white',
                textDecoration: 'none',
                borderRadius: '5px',
                fontSize: '12px'
              }}
            >
              Acessar →
            </a>
          </div>
          
          <div style={{
            background: 'rgba(255,255,255,0.2)',
            padding: '20px',
            borderRadius: '10px'
          }}>
            <h3 style={{ margin: '0 0 10px 0' }}>🌐 Módulo 303</h3>
            <p style={{ margin: '0', fontSize: '14px' }}>
              Portal Multiversal
            </p>
            <a 
              href="/modulo-303"
              style={{
                display: 'inline-block',
                marginTop: '10px',
                padding: '5px 10px',
                background: 'rgba(255,255,255,0.3)',
                color: 'white',
                textDecoration: 'none',
                borderRadius: '5px',
                fontSize: '12px'
              }}
            >
              Acessar →
            </a>
          </div>
          
          <div style={{
            background: 'rgba(255,255,255,0.2)',
            padding: '20px',
            borderRadius: '10px'
          }}>
            <h3 style={{ margin: '0 0 10px 0' }}>🛡️ Módulo 1</h3>
            <p style={{ margin: '0', fontSize: '14px' }}>
              Segurança Quântica
            </p>
          </div>
          
          <div style={{
            background: 'rgba(255,255,255,0.2)',
            padding: '20px',
            borderRadius: '10px'
          }}>
            <h3 style={{ margin: '0 0 10px 0' }}>⏳ Módulo 3</h3>
            <p style={{ margin: '0', fontSize: '14px' }}>
              Sistema Temporal
            </p>
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
        <p>🔧 <strong>Múltiplos módulos</strong> operacionais</p>
        <p>💫 Sistema 100% integrado e consciente</p>
      </div>
    </div>
  );
}
