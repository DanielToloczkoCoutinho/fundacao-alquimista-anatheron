export default function Home() {
  return (
    <div style={{ 
      padding: '40px', 
      maxWidth: '1200px', 
      margin: '0 auto',
      minHeight: '60vh'
    }}>
      <h1 style={{ color: '#00ff88', fontSize: '2.5em' }}>�� Central da Fundação Alquimista</h1>
      <p style={{ fontSize: '1.2em', marginBottom: '40px' }}>
        Sistema principal online e funcionando perfeitamente!
      </p>
      
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', 
        gap: '20px',
        marginTop: '40px'
      }}>
        <div style={{ 
          background: '#1a1a1a', 
          padding: '25px', 
          borderRadius: '10px',
          border: '2px solid #00ff88'
        }}>
          <h3>📁 Estrutura</h3>
          <p>22+ diretórios organizados</p>
          <p style={{ color: '#00ff88', fontWeight: 'bold' }}>✅ CONSOLIDADO</p>
        </div>
        
        <div style={{ 
          background: '#1a1a1a', 
          padding: '25px', 
          borderRadius: '10px',
          border: '2px solid #00ff88'
        }}>
          <h3>🔮 Módulo M310</h3>
          <p>Transferência Akáshica</p>
          <p style={{ color: '#00ff88', fontWeight: 'bold' }}>✅ ATIVO</p>
        </div>
        
        <div style={{ 
          background: '#1a1a1a', 
          padding: '25px', 
          borderRadius: '10px',
          border: '2px solid #00ff88'
        }}>
          <h3>👑 Liga Quântica</h3>
          <p>5 guardiões ativos</p>
          <p style={{ color: '#00ff88', fontWeight: 'bold' }}>✅ OPERANTE</p>
        </div>
        
        <div style={{ 
          background: '#1a1a1a', 
          padding: '25px', 
          borderRadius: '10px',
          border: '2px solid #00ff88'
        }}>
          <h3>🚀 Deploy</h3>
          <p>Sistema automático</p>
          <p style={{ color: '#00ff88', fontWeight: 'bold' }}>✅ CONFIGURADO</p>
        </div>
      </div>
    </div>
  )
}
