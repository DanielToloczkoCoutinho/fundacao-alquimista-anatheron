"use client";
export const dynamic = "force-dynamic";
export default function Dashboard() {
  const currentInterface = "dashboard";
  
  return (
    <div style={{ 
      padding: '40px', 
      background: '#0a0a0a', 
      color: '#00ffff',
      fontFamily: 'monospace',
      minHeight: '100vh'
    }}>
      <h1 style={{ fontSize: '2.5em', marginBottom: '20px', textAlign: 'center' }}>
        📊 DASHBOARD
      </h1>
      <p style={{ fontSize: '1.1em', marginBottom: '30px', textAlign: 'center' }}>
        Sistema de Monitoramento - Fundação Alquimista
      </p>
      
      <div style={{ 
        background: '#1a1a1a', 
        padding: '20px', 
        margin: '20px auto',
        borderRadius: '10px',
        border: '1px solid #00ffff',
        maxWidth: '800px'
      }}>
        <h2 style={{ textAlign: 'center', marginBottom: '15px' }}>✅ SISTEMA OPERACIONAL</h2>
        <p style={{ textAlign: 'center' }}><strong>Build:</strong> Next.js 15.5.4</p>
        <p style={{ textAlign: 'center' }}><strong>CSS:</strong> Inline</p>
        <p style={{ textAlign: 'center' }}><strong>Interface:</strong> Dashboard</p>
      </div>

      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', 
        gap: '15px',
        marginTop: '30px',
        maxWidth: '800px',
        margin: '30px auto'
      }}>
        {[
          { name: 'Sistemas', value: '284', color: '#ff4444' },
          { name: 'Interfaces', value: '47', color: '#4444ff' },
          { name: 'Scripts', value: '1.937', color: '#44ff44' },
          { name: 'Arquivos', value: '284K', color: '#ffff44' }
        ].map((metric, index) => (
          <div key={index} style={{
            background: '#1a1a1a',
            padding: '15px',
            borderRadius: '8px',
            border: '1px solid #ff4444',
            textAlign: 'center'
          }}>
            <div style={{ fontSize: '2em', color: '#ff4444', fontWeight: 'bold' }}>
              {metric.value}
            </div>
            <div style={{ fontSize: '0.9em', opacity: 0.8 }}>
              {metric.name}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
