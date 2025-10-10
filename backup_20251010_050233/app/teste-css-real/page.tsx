export default function TesteCSSReal() {
  return (
    <div style={{
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%)',
      color: 'white',
      padding: '2rem',
      fontFamily: 'Arial, sans-serif'
    }}>
      <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
        <h1 style={{
          fontSize: '4rem',
          fontWeight: 'bold',
          background: 'linear-gradient(45deg, #00ffff, #ff00ff)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          marginBottom: '1rem'
        }}>
          🎨 TESTE CSS REAL
        </h1>
        <p style={{ fontSize: '1.5rem', color: '#00ffff' }}>
          Fundo ESCURO com CSS INLINE - 100% Funcional
        </p>
        <div style={{
          display: 'inline-block',
          background: 'linear-gradient(45deg, #00ff00, #0000ff)',
          padding: '1rem 2rem',
          borderRadius: '1rem',
          border: '4px solid #ffff00',
          marginTop: '1rem'
        }}>
          <p style={{ fontSize: '1.25rem', fontWeight: 'bold', color: 'white' }}>
            ✅ AGORA SIM: FUNDO ESCURO!
          </p>
        </div>
      </div>

      {/* CARDS COM CSS INLINE */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
        gap: '2rem',
        maxWidth: '1200px',
        margin: '0 auto'
      }}>
        {[
          { title: '⚡ Circuitos Quânticos', value: '1,328', color: '#00ffff' },
          { title: '🚀 Execuções', value: '4,252', color: '#ff00ff' },
          { title: '🔗 Qubits Ativos', value: '127', color: '#ffff00' },
          { title: '🎯 Fidelidade', value: '99.2%', color: '#00ff00' }
        ].map((item, index) => (
          <div key={index} style={{
            background: 'rgba(255, 255, 255, 0.1)',
            backdropFilter: 'blur(10px)',
            padding: '2rem',
            borderRadius: '1rem',
            border: `2px solid ${item.color}`,
            textAlign: 'center'
          }}>
            <div style={{
              fontSize: '3rem',
              fontWeight: 'bold',
              color: item.color,
              marginBottom: '1rem'
            }}>
              {item.value}
            </div>
            <div style={{
              fontSize: '1.25rem',
              color: 'white'
            }}>
              {item.title}
            </div>
          </div>
        ))}
      </div>

      {/* MENSAGEM FINAL */}
      <div style={{
        maxWidth: '800px',
        margin: '3rem auto',
        padding: '2rem',
        background: 'linear-gradient(45deg, #ff0000, #ff9900)',
        borderRadius: '1rem',
        textAlign: 'center',
        border: '4px solid #ffffff'
      }}>
        <h2 style={{
          fontSize: '2.5rem',
          fontWeight: 'bold',
          marginBottom: '1rem',
          color: 'white'
        }}>
          🍾 PROBLEMA RESOLVIDO!
        </h2>
        <p style={{ fontSize: '1.25rem', marginBottom: '1rem' }}>
          <strong>O fundo branco horroroso ACABOU!</strong>
        </p>
        <p style={{ fontSize: '1.1rem' }}>
          Usamos CSS INLINE para garantir que o design funcione 100%
        </p>
      </div>
    </div>
  )
}
