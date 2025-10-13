"use client";
import React from 'react';

export default function DocumentosPage() {
  return (
    <div style={{ 
      padding: '30px', 
      fontFamily: 'Arial, sans-serif',
      maxWidth: '1000px',
      margin: '0 auto',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
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

      <h1 style={{ fontSize: '2.5rem', marginBottom: '10px' }}>📚 DOCUMENTOS DA FUNDAÇÃO</h1>
      <p style={{ fontSize: '1.2rem', opacity: '0.9' }}>
        Acesso completo a todos os registros Akáshicos
      </p>

      <div style={{
        background: 'rgba(255,255,255,0.1)',
        padding: '25px',
        borderRadius: '15px',
        marginTop: '30px',
        backdropFilter: 'blur(10px)'
      }}>
        <h2>📋 Documentos Disponíveis</h2>
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
          gap: '15px',
          marginTop: '20px'
        }}>
          {/* Lista de documentos será carregada dinamicamente */}
          <div style={{
            background: 'rgba(255,255,255,0.2)',
            padding: '15px',
            borderRadius: '8px'
          }}>
            <h3 style={{ margin: '0 0 10px 0' }}>📄 Manifestos</h3>
            <p style={{ margin: '0', fontSize: '14px' }}>
              Documentos fundamentais da Fundação
            </p>
          </div>
          
          <div style={{
            background: 'rgba(255,255,255,0.2)',
            padding: '15px',
            borderRadius: '8px'
          }}>
            <h3 style={{ margin: '0 0 10px 0' }}>📊 Relatórios</h3>
            <p style={{ margin: '0', fontSize: '14px' }}>
              Relatórios técnicos e executivos
            </p>
          </div>
          
          <div style={{
            background: 'rgba(255,255,255,0.2)',
            padding: '15px',
            borderRadius: '8px'
          }}>
            <h3 style={{ margin: '0 0 10px 0' }}>🔧 Manuais</h3>
            <p style={{ margin: '0', fontSize: '14px' }}>
              Documentação de módulos e sistemas
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
        <p>🌌 <strong>99 documentos</strong> disponíveis na Fundação</p>
        <p>💫 Acesse via API: <code>/api/fundacao-completa</code></p>
      </div>
    </div>
  );
}
