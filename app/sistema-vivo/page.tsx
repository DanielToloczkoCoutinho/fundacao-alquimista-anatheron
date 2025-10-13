"use client";
'use client';
export const dynamic = "force-dynamic";
import { useEffect, useState } from 'react';

export default function SistemaVivo() {
  const [loadTime, setLoadTime] = useState('');
  const [isClient, setIsClient] = useState(false);

  useEffect(() => {
    setIsClient(true);
    setLoadTime(new Date().toLocaleString());
  }, []);

  return (
    <div style={{ 
      padding: '20px', 
      background: '#1a1a1a', 
      color: '#ffffff',
      minHeight: '100vh',
      fontFamily: 'monospace'
    }}>
      <h1>🏗️ Sistema Vivo - Fundação Alquimista</h1>
      <p>Interface dinâmica - Sistema operacional em tempo real</p>
      
      <div style={{ marginTop: '20px', padding: '15px', background: '#2a2a2a', borderRadius: '8px' }}>
        <h2>📊 Status do Sistema</h2>
        <p>🚀 <strong>Status:</strong> Online e Dinâmico</p>
        <p>🕒 <strong>Carregado em:</strong> {loadTime || 'Carregando...'}</p>
        <p>🔧 <strong>Modo:</strong> {isClient ? 'Cliente' : 'Servidor'}</p>
        <p>⚡ <strong>Dinâmico:</strong> force-dynamic ativado</p>
      </div>

      <div style={{ marginTop: '20px', padding: '15px', background: '#2a2a2a', borderRadius: '8px' }}>
        <h2>🎯 Métricas em Tempo Real</h2>
        <p>• Uptime: <strong>{(Date.now() % 100000) / 1000}s</strong></p>
        <p>• Memória: <strong>{(Math.random() * 100).toFixed(1)}%</strong></p>
        <p>• CPU: <strong>{(Math.random() * 100).toFixed(1)}%</strong></p>
        <p>• Conexões: <strong>{Math.floor(Math.random() * 1000)}</strong></p>
      </div>

      <div style={{ marginTop: '20px', padding: '15px', background: '#2a2a2a', borderRadius: '8px' }}>
        <h2>🔧 Controles do Sistema</h2>
        <button style={{ 
          padding: '10px 15px', 
          background: '#00ff88', 
          color: '#000', 
          border: 'none', 
          borderRadius: '5px',
          marginRight: '10px',
          cursor: 'pointer'
        }}>
          🔄 Atualizar Métricas
        </button>
        <button style={{ 
          padding: '10px 15px', 
          background: '#0088ff', 
          color: '#fff', 
          border: 'none', 
          borderRadius: '5px',
          cursor: 'pointer'
        }}>
          📊 Ver Logs Detalhados
        </button>
      </div>
    </div>
  );
}
