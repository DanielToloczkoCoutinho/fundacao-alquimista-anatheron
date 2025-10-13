"use client";
import { useState, useEffect } from 'react';

export default function StatusPage() {
  const [status, setStatus] = useState('Verificando...');

  useEffect(() => {
    setStatus('✅ Sistema Operacional');
  }, []);

  return (
    <div style={{ padding: '40px', textAlign: 'center' }}>
      <h1>🌌 Status da Fundação Alquimista</h1>
      <p><strong>Status:</strong> {status}</p>
      <p><strong>Versão:</strong> Quantum 1.0.0</p>
      <p><strong>Usuário:</strong> Zennith</p>
      <a href="/">← Voltar ao Início</a>
    </div>
  );
}
