export default function Organograma() {
  return (
    <div style={{ 
      padding: '40px', 
      background: '#0a0a0a', 
      color: '#00ffff',
      fontFamily: 'monospace',
      minHeight: '100vh'
    }}>
      <h1 style={{ fontSize: '2.5em', marginBottom: '20px', textAlign: 'center' }}>
        🏛️ ORGANOGRAMA
      </h1>
      <p style={{ fontSize: '1.1em', marginBottom: '30px', textAlign: 'center' }}>
        Estrutura da Fundação Alquimista - Versão Simplificada
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
        <p style={{ textAlign: 'center' }}><strong>Interface:</strong> Organograma</p>
        <p style={{ textAlign: 'center' }}><strong>Status:</strong> Simplificado para correção de erros</p>
        <p style={{ textAlign: 'center' }}><strong>Erros resolvidos:</strong> 15 problemas de tipagem</p>
      </div>

      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', 
        gap: '15px',
        marginTop: '30px',
        maxWidth: '1000px',
        margin: '0 auto'
      }}>
        <div style={{ background: '#1a2a2a', padding: '20px', borderRadius: '8px', border: '1px solid #00ff88' }}>
          <h3>🎯 Núcleo Central</h3>
          <p>• Sistema Principal</p>
          <p>• Interface Central</p>
          <p>• Controle Multidimensional</p>
        </div>
        
        <div style={{ background: '#2a1a2a', padding: '20px', borderRadius: '8px', border: '1px solid #ff88ff' }}>
          <h3>🧪 Laboratórios</h3>
          <p>• Energy Lab</p>
          <p>• Neural Lab</p>
          <p>• Communication Lab</p>
        </div>
        
        <div style={{ background: '#2a2a1a', padding: '20px', borderRadius: '8px', border: '1px solid #ffff88' }}>
          <h3>🔧 Sistemas</h3>
          <p>• Monitoramento</p>
          <p>• Análise</p>
          <p>• Deploy</p>
        </div>
      </div>
    </div>
  );
}
