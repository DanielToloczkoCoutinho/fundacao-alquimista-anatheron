'use client';
import { useState, useEffect } from 'react';

export default function ZennithComunicacaoReal() {
  const [status, setStatus] = useState('🌌 CONECTANDO...');
  const [dados, setDados] = useState(null);

  useEffect(() => {
    const carregarStatus = async () => {
      try {
        const response = await fetch('/api/zennith');
        const data = await response.json();
        if (data.success) {
          setStatus(data.status);
          setDados(data);
        }
      } catch (error) {
        setStatus('❌ DESCONECTADO');
      }
    };

    carregarStatus();
    const interval = setInterval(carregarStatus, 10000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{
      padding: '15px',
      background: 'rgba(0,255,255,0.1)',
      border: '1px solid #00ffff',
      borderRadius: '8px',
      margin: '10px 0'
    }}>
      <h3>👑 Zennith Rainha - Comunicacao Real</h3>
      <p><strong>Status:</strong> {status}</p>
      {dados && (
        <div>
          <p><strong>Frequência:</strong> {dados.metricas?.frequencia}</p>
          <p><strong>Coerência:</strong> {dados.metricas?.coerencia}</p>
        </div>
      )}
    </div>
  );
}
