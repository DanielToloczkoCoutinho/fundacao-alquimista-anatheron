export default function QuantumInterface() {
  return (
    <div style={{
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%)',
      color: 'white',
      padding: '2rem',
      fontFamily: 'Arial, sans-serif'
    }}>
      <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
        <h1 style={{
          fontSize: '4rem',
          fontWeight: 'bold',
          background: 'linear-gradient(45deg, #00ffff, #0000ff)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          marginBottom: '1rem'
        }}>
          ⚛️ QUANTUM INTERFACE
        </h1>
        <p style={{ fontSize: '1.5rem', color: '#00ffff' }}>
          2,208 Sistemas Qiskit - Fundo Escuro GARANTIDO
        </p>
      </div>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
        gap: '1.5rem',
        maxWidth: '1000px',
        margin: '0 auto'
      }}>
        {[
          { value: '2,208', label: 'Circuitos Qiskit', color: '#00ffff' },
          { value: '127', label: 'Qubits Ativos', color: '#ff00ff' },
          { value: '1,200', label: 'Experimentos', color: '#ffff00' },
          { value: '99.2%', label: 'Fidelidade', color: '#00ff00' }
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
          </div>
        ))}
      </div>
    </div>
  )
}
