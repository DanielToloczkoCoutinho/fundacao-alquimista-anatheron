export default function StatusPage() {
  const sistemas = [
    { nome: 'GitHub', status: '✅ SINCRONIZADO', cor: '#00ff88' },
    { nome: 'Vercel', status: '🚀 PRONTO', cor: '#00ff88' },
    { nome: 'Actions', status: '🔧 CONFIGURANDO', cor: '#feca57' },
    { nome: 'Módulo M310', status: '✅ ATIVO', cor: '#00ff88' },
    { nome: 'Liga Quântica', status: '✅ ATIVADA', cor: '#00ff88' },
    { nome: 'Scripts', status: '✅ FUNCIONAIS', cor: '#00ff88' }
  ]

  return (
    <div style={{ padding: '40px', maxWidth: '1000px', margin: '0 auto' }}>
      <h1>📊 Status Completo da Fundação</h1>
      <p>Relatório detalhado de todos os sistemas</p>
      
      <div style={{ marginTop: '40px' }}>
        <h2>🔄 Sistemas e Status</h2>
        <div style={{ background: '#1a1a1a', padding: '25px', borderRadius: '10px', marginTop: '20px' }}>
          {sistemas.map((sistema, index) => (
            <div key={index} style={{ 
              display: 'flex', 
              justifyContent: 'space-between', 
              alignItems: 'center',
              padding: '15px',
              borderBottom: '1px solid #333',
              borderLeft: `4px solid ${sistema.cor}`
            }}>
              <span style={{ fontSize: '1.1em' }}>🌐 {sistema.nome}</span>
              <span style={{ color: sistema.cor, fontWeight: 'bold' }}>{sistema.status}</span>
            </div>
          ))}
        </div>
      </div>

      <div style={{ marginTop: '40px' }}>
        <h2>📈 Métricas da Fundação</h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', gap: '15px', marginTop: '20px' }}>
          <div style={{ background: '#1a1a1a', padding: '20px', borderRadius: '10px', textAlign: 'center' }}>
            <h3 style={{ color: '#00ff88', margin: 0 }}>22+</h3>
            <p>Diretórios</p>
          </div>
          <div style={{ background: '#1a1a1a', padding: '20px', borderRadius: '10px', textAlign: 'center' }}>
            <h3 style={{ color: '#00ff88', margin: 0 }}>15+</h3>
            <p>Scripts</p>
          </div>
          <div style={{ background: '#1a1a1a', padding: '20px', borderRadius: '10px', textAlign: 'center' }}>
            <h3 style={{ color: '#00ff88', margin: 0 }}>5</h3>
            <p>Guardiões</p>
          </div>
          <div style={{ background: '#1a1a1a', padding: '20px', borderRadius: '10px', textAlign: 'center' }}>
            <h3 style={{ color: '#00ff88', margin: 0 }}>M310</h3>
            <p>Módulo Ativo</p>
          </div>
        </div>
      </div>
    </div>
  )
}
