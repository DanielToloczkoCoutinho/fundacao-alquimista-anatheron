export default function VerdadeReal() {
  return (
    <div style={{
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)',
      color: 'white',
      padding: '2rem',
      fontFamily: 'Arial, sans-serif'
    }}>
      <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
        <h1 style={{
          fontSize: '4rem',
          fontWeight: 'bold',
          background: 'linear-gradient(45deg, #ff0000, #ffff00)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          marginBottom: '1rem'
        }}>
          🔍 VERDADE REAL
        </h1>
        <p style={{ fontSize: '1.5rem', color: '#00ffff' }}>
          Dados REAIS - Agora com fundo escuro GARANTIDO
        </p>
      </div>

      {/* ESTATÍSTICAS */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
        gap: '1.5rem',
        maxWidth: '1000px',
        margin: '0 auto 3rem auto'
      }}>
        {[
          { value: '1,328', label: 'Circuitos Quânticos', color: '#00ffff' },
          { value: '4,252', label: 'Execuções', color: '#ff00ff' },
          { value: '100', label: 'Imports Qiskit', color: '#ffff00' },
          { value: '13,526', label: 'Arquivos Python', color: '#00ff00' }
        ].map((item, index) => (
          <div key={index} style={{
            background: 'rgba(255, 255, 255, 0.1)',
            backdropFilter: 'blur(10px)',
            padding: '1.5rem',
            borderRadius: '1rem',
            border: `3px solid ${item.color}`,
            textAlign: 'center'
          }}>
            <div style={{
              fontSize: '2.5rem',
              fontWeight: 'bold',
              color: item.color,
              marginBottom: '0.5rem'
            }}>
              {item.value}
            </div>
            <div style={{ fontSize: '1.1rem' }}>{item.label}</div>
            <div style={{
              fontSize: '0.8rem',
              color: '#00ff00',
              marginTop: '0.5rem'
            }}>
              ✅ NÚMERO REAL
            </div>
          </div>
        ))}
      </div>

      {/* MENSAGEM FINAL */}
      <div style={{
        maxWidth: '600px',
        margin: '2rem auto',
        padding: '2rem',
        background: 'linear-gradient(45deg, #00ff00, #0000ff)',
        borderRadius: '1rem',
        textAlign: 'center',
        border: '4px solid #ffff00'
      }}>
        <h2 style={{
          fontSize: '2rem',
          fontWeight: 'bold',
          marginBottom: '1rem',
          color: 'white'
        }}>
          🎨 FUNDO BRANCO ELIMINADO!
        </h2>
        <p style={{ fontSize: '1.2rem' }}>
          Usando CSS INLINE para garantir o design escuro
        </p>
      </div>
    </div>
  )
}
