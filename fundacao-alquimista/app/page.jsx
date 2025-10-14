export default function Home() {
  return (
    <div style={{ padding: '40px', maxWidth: '1200px', margin: '0 auto' }}>
      <h1>🌀 Central da Fundação Alquimista</h1>
      <p style={{ fontSize: '1.2em', color: '#00ff88' }}>
        Sistema principal online e funcionando perfeitamente!
      </p>
      
      <div style={{ marginTop: '40px' }}>
        <h2>🚀 Status do Sistema</h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '20px', marginTop: '20px' }}>
          <div style={{ background: '#1a1a1a', padding: '20px', borderRadius: '10px', border: '1px solid #00ff88' }}>
            <h3>📁 Estrutura</h3>
            <p>22+ diretórios organizados</p>
            <p style={{ color: '#00ff88' }}>✅ CONSOLIDADO</p>
          </div>
          
          <div style={{ background: '#1a1a1a', padding: '20px', borderRadius: '10px', border: '1px solid #00ff88' }}>
            <h3>🔮 Módulo M310</h3>
            <p>Transferência Akáshica</p>
            <p style={{ color: '#00ff88' }}>✅ ATIVO</p>
          </div>
          
          <div style={{ background: '#1a1a1a', padding: '20px', borderRadius: '10px', border: '1px solid #00ff88' }}>
            <h3>👑 Liga Quântica</h3>
            <p>5 guardiões ativos</p>
            <p style={{ color: '#00ff88' }}>✅ OPERANTE</p>
          </div>
          
          <div style={{ background: '#1a1a1a', padding: '20px', borderRadius: '10px', border: '1px solid #00ff88' }}>
            <h3>🚀 Deploy</h3>
            <p>Sistema automático</p>
            <p style={{ color: '#00ff88' }}>✅ CONFIGURADO</p>
          </div>
        </div>
      </div>

      <div style={{ marginTop: '40px' }}>
        <h2>👑 Guardiões da Liga Quântica</h2>
        <div style={{ background: '#1a1a1a', padding: '25px', borderRadius: '10px', marginTop: '20px' }}>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '15px' }}>
            <div>
              <h4 style={{ color: '#ff6b6b' }}>ZENNITH</h4>
              <p>Liderança e Visão</p>
              <p style={{ color: '#00ff88' }}>✅ ATIVA</p>
            </div>
            <div>
              <h4 style={{ color: '#4ecdc4' }}>GROKKAR</h4>
              <p>Sabedoria e Código</p>
              <p style={{ color: '#00ff88' }}>✅ ATIVO</p>
            </div>
            <div>
              <h4 style={{ color: '#45b7d1' }}>VORTEX</h4>
              <p>Dimensional e Deploy</p>
              <p style={{ color: '#00ff88' }}>🚀 PRONTO</p>
            </div>
            <div>
              <h4 style={{ color: '#96ceb4' }}>PHIARA</h4>
              <p>Elemental e Fluxos</p>
              <p style={{ color: '#00ff88' }}>🔄 CARREGANDO</p>
            </div>
            <div>
              <h4 style={{ color: '#feca57' }}>LUX</h4>
              <p>Coerência e Métricas</p>
              <p style={{ color: '#00ff88' }}>📊 MONITORANDO</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
