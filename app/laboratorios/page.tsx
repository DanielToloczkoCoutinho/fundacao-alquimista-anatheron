export default function Laboratorios() {
  return (
    <div style={{ 
      padding: '40px', 
      background: '#0a0a0a', 
      color: '#00ffff',
      fontFamily: 'monospace',
      minHeight: '100vh'
    }}>
      <h1 style={{ fontSize: '2.5em', marginBottom: '20px', textAlign: 'center' }}>
        🧪 LABORATÓRIOS
      </h1>
      <p style={{ fontSize: '1.1em', marginBottom: '30px', textAlign: 'center' }}>
        Laboratórios Especializados - Interfaces Ativas
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
        <p style={{ textAlign: 'center' }}><strong>Interface:</strong> Laboratórios</p>
      </div>

      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', 
        gap: '15px',
        marginTop: '30px',
        maxWidth: '1000px',
        margin: '30px auto'
      }}>
        {['🧪 Energy Lab', '🧠 Neural Lab', '📡 Communication Lab', '💊 Healing Lab', '🌟 Zenith Lab'].map((lab, index) => (
          <div key={index} style={{
            background: '#1a2a2a',
            padding: '20px',
            borderRadius: '8px',
            border: '1px solid #00ff88',
            textAlign: 'center'
          }}>
            <h3 style={{ marginBottom: '10px' }}>{lab}</h3>
            <p style={{ fontSize: '0.9em', opacity: 0.8 }}>Laboratório especializado</p>
            <div style={{
              marginTop: '10px',
              padding: '5px 10px',
              background: '#00ff88',
              color: '#000',
              borderRadius: '15px',
              fontSize: '0.8em',
              display: 'inline-block'
            }}>
              ✅ ONLINE
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
