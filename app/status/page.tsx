"use client";
"use client";
export const dynamic = "force-dynamic";

export default function Status() {
  return (
    <div style={{ 
      padding: '20px', 
      background: '#1a1a1a', 
      color: '#ffffff',
      minHeight: '100vh',
      fontFamily: 'monospace'
    }}>
      <h1>🏗️ Status - Fundação Alquimista</h1>
      <p>Interface dinâmica - Em desenvolvimento</p>
      <div style={{ marginTop: '20px', padding: '10px', background: '#2a2a2a', borderRadius: '5px' }}>
        <p>🚀 <strong>Status:</strong> Online</p>
        <p>📊 <strong>Carregado em:</strong> {new Date().toLocaleString()}</p>
        <p>🔧 <strong>Modo:</strong> Dinâmico (force-dynamic)</p>
      </div>
    </div>
  );
}
