export default function Page() {
  const interfaceName = '"'$(basename "$dir")'"';
  
  return (
    <div style={{ 
      padding: '40px', 
      background: '#0a0a0a', 
      color: '#00ffff',
      fontFamily: 'Courier New, monospace',
      minHeight: '100vh'
    }}>
      <h1 style={{ fontSize: '2.5em', marginBottom: '20px' }}>
        🌌 {interfaceName.toUpperCase()}
      </h1>
      <p style={{ fontSize: '1.1em', marginBottom: '30px' }}>
        Interface da Fundação Alquimista - Online
      </p>
      
      <div style={{
        background: '#1a1a1a',
        padding: '25px',
        borderRadius: '12px',
        border: '2px solid #00ffff',
        marginBottom: '20px'
      }}>
        <h2>✅ STATUS: ONLINE</h2>
        <p>Esta interface foi ativada via correção automática</p>
        <p><strong>URL:</strong> https://fundacao-alquimista-anatheron-8xv9ixbp3.vercel.app/{interfaceName}</p>
      </div>

      <div style={{
        padding: '20px',
        background: '#1a2a2a',
        borderRadius: '8px',
        marginTop: '30px'
      }}>
        <h3>🔧 Informações Técnicas</h3>
        <p><strong>Build:</strong> Next.js 15.5.4</p>
        <p><strong>Router:</strong> App Router</p>
        <p><strong>Status:</strong> Operacional</p>
      </div>
    </div>
  );
}
