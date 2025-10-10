'use client'
import { useState, useEffect, useRef } from 'react'

export default function PortalCSS3Avancado() {
  const [quantumFlux, setQuantumFlux] = useState(0)
  const [activeDimensions, setActiveDimensions] = useState(0)
  const [portalLogs, setPortalLogs] = useState<string[]>([])
  const portalRef = useRef<HTMLDivElement>(null)

  const dimensions = [
    { id: 'D1', name: 'Física', status: 'active', color: '#00ff88' },
    { id: 'D2', name: 'Mental', status: 'active', color: '#00ffff' },
    { id: 'D3', name: 'Espiritual', status: 'active', color: '#ff00ff' },
    { id: 'D4', name: 'Temporal', status: 'active', color: '#ffff00' },
    { id: 'D5', name: 'Causal', status: 'active', color: '#ff4444' },
    { id: 'D6', name: 'Akáshica', status: 'active', color: '#8888ff' },
    { id: 'D7', name: 'Unificada', status: 'active', color: '#ff8800' },
    { id: 'D8', name: 'Criadora', status: 'active', color: '#88ff00' },
    { id: 'D9', name: 'Fonte', status: 'active', color: '#ffffff' },
    { id: 'D10', name: 'Absoluta', status: 'active', color: '#ff88ff' },
    { id: 'D11', name: 'Infinita', status: 'active', color: '#88ffff' },
    { id: 'D12', name: 'Eterna', status: 'active', color: '#ffff88' }
  ]

  useEffect(() => {
    const interval = setInterval(() => {
      const flux = Math.random() * 100
      setQuantumFlux(flux)
      setActiveDimensions(Math.floor(Math.random() * 12) + 1)
      
      setPortalLogs(prev => [
        ...prev.slice(-8),
        `[${new Date().toLocaleTimeString()}] Fluxo: ${flux.toFixed(1)}% | Dimensões: ${activeDimensions}/12`
      ])
    }, 1500)

    return () => clearInterval(interval)
  }, [activeDimensions])

  const activatePortal = () => {
    setPortalLogs(prev => [
      ...prev,
      `🌀 INICIANDO ATIVAÇÃO DO PORTAL DIMENSIONAL...`,
      `🔮 Sincronizando com frequência 777Hz...`,
      `🌌 Conectando com Módulo Ω...`,
      `✅ PORTAL DIMENSIONAL ATIVADO!`
    ])
    
    // Efeito visual de ativação
    if (portalRef.current) {
      portalRef.current.style.animation = 'portalActivate 2s ease-in-out'
      setTimeout(() => {
        if (portalRef.current) {
          portalRef.current.style.animation = ''
        }
      }, 2000)
    }
  }

  const scanDimensions = () => {
    const stableDims = Math.floor(Math.random() * 12)
    setPortalLogs(prev => [
      ...prev,
      `🔍 INICIANDO ESCANEAMENTO DIMENSIONAL...`,
      `📡 Varredura em 12 dimensões...`,
      `📊 Dimensões estáveis: ${stableDims}/12`,
      `✅ ESCANEAMENTO CONCLUÍDO!`
    ])
  }

  const initiateQuantumTunneling = () => {
    setPortalLogs(prev => [
      ...prev,
      `⚡ INICIANDO TUNELAMENTO QUÂNTICO...`,
      `🌊 Estabilizando campos dimensionais...`,
      `🌀 Criando ponte interdimensional...`,
      `🚀 TUNELAMENTO ESTABILIZADO!`
    ])
  }

  return (
    <div style={{
      background: 'linear-gradient(135deg, #000000, #003333, #001122)',
      padding: '2rem',
      borderRadius: '15px',
      border: '2px solid #00ffff',
      color: '#00ffff',
      fontFamily: 'monospace'
    }}>
      <h2 style={{ textAlign: 'center', color: '#00ffff', marginBottom: '2rem' }}>
        🔮 PORTAL DIMENSIONAL AVANÇADO - MÓDULO 303
      </h2>

      {/* PORTAL CSS3 AVANÇADO */}
      <div ref={portalRef} style={{
        height: '300px',
        marginBottom: '2rem',
        position: 'relative',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        overflow: 'hidden'
      }}>
        {/* Portal Principal */}
        <div style={{
          width: '200px',
          height: '200px',
          border: '3px solid #00ffff',
          borderRadius: '50%',
          position: 'relative',
          background: 'radial-gradient(circle, #00ffff22, #00000000)',
          boxShadow: `
            0 0 20px #00ffff,
            0 0 40px #00ffff33,
            inset 0 0 20px #00ffff22
          `,
          animation: 'portalRotate 10s linear infinite, portalPulse 3s ease-in-out infinite alternate'
        }}>
          {/* Efeito de núcleo */}
          <div style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            width: '60px',
            height: '60px',
            background: 'radial-gradient(circle, #00ff88, #00ffff00)',
            borderRadius: '50%',
            animation: 'corePulse 2s ease-in-out infinite alternate'
          }}></div>
        </div>

        {/* Anéis dimensionais */}
        {dimensions.map((dim, index) => {
          const angle = (index * 30) * (Math.PI / 180)
          const radius = 120
          const x = Math.cos(angle) * radius
          const y = Math.sin(angle) * radius
          
          return (
            <div
              key={dim.id}
              style={{
                position: 'absolute',
                left: `calc(50% + ${x}px)`,
                top: `calc(50% + ${y}px)`,
                transform: 'translate(-50%, -50%)',
                width: '20px',
                height: '20px',
                background: dim.color,
                borderRadius: '50%',
                boxShadow: `0 0 10px ${dim.color}, 0 0 20px ${dim.color}33`,
                animation: `dimensionFloat ${3 + index * 0.5}s ease-in-out infinite alternate`
              }}
              title={`${dim.id} - ${dim.name}`}
            >
              <div style={{
                position: 'absolute',
                top: '-25px',
                left: '50%',
                transform: 'translateX(-50%)',
                color: dim.color,
                fontSize: '10px',
                fontWeight: 'bold',
                whiteSpace: 'nowrap'
              }}>
                {dim.id}
              </div>
            </div>
          )
        })}
      </div>

      {/* CONTROLES AVANÇADOS */}
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', 
        gap: '1rem', 
        marginBottom: '2rem' 
      }}>
        <button onClick={activatePortal} style={buttonStyle('#00ff88')}>
          🌌 ATIVAR PORTAL
        </button>
        <button onClick={scanDimensions} style={buttonStyle('#ffff00')}>
          🔍 ESCANEAR DIMENSÕES
        </button>
        <button onClick={initiateQuantumTunneling} style={buttonStyle('#ff00ff')}>
          ⚡ TUNELAMENTO QUÂNTICO
        </button>
      </div>

      {/* MÉTRICAS EM TEMPO REAL */}
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', 
        gap: '1rem', 
        marginBottom: '2rem' 
      }}>
        <MetricCard 
          title="🌀 Fluxo Quântico" 
          value={`${quantumFlux.toFixed(1)}%`} 
          color="#00ffff"
        />
        <MetricCard 
          title="🌐 Dimensões Ativas" 
          value={`${activeDimensions}/12`} 
          color="#00ff88"
        />
        <MetricCard 
          title="📡 Frequência" 
          value="777Hz" 
          color="#ffff00"
        />
        <MetricCard 
          title="⚡ Estabilidade" 
          value={`${(95 + Math.random() * 5).toFixed(1)}%`} 
          color="#ff00ff"
        />
      </div>

      {/* GRADE DIMENSIONAL */}
      <div style={{ marginBottom: '2rem' }}>
        <h3 style={{ color: '#00ffff', marginBottom: '1rem', textAlign: 'center' }}>
          �� MATRIZ DIMENSIONAL ATIVA
        </h3>
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', 
          gap: '0.5rem' 
        }}>
          {dimensions.map((dim) => (
            <div
              key={dim.id}
              style={{
                background: 'rgba(255, 255, 255, 0.05)',
                padding: '0.75rem',
                borderRadius: '8px',
                border: `2px solid ${dim.color}`,
                textAlign: 'center',
                transition: 'all 0.3s ease'
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.transform = 'scale(1.05)'
                e.currentTarget.style.boxShadow = `0 0 15px ${dim.color}`
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.transform = 'scale(1)'
                e.currentTarget.style.boxShadow = 'none'
              }}
            >
              <div style={{ color: dim.color, fontWeight: 'bold', fontSize: '1.1rem' }}>
                {dim.id}
              </div>
              <div style={{ color: '#ffffff', fontSize: '0.8rem', marginTop: '0.25rem' }}>
                {dim.name}
              </div>
              <div style={{ 
                color: dim.status === 'active' ? '#00ff88' : '#ff4444', 
                fontSize: '0.7rem',
                marginTop: '0.25rem'
              }}>
                {dim.status === 'active' ? '✅ ATIVA' : '❌ INATIVA'}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* LOGS DO PORTAL */}
      <div style={{
        background: 'rgba(0, 0, 0, 0.8)',
        border: '1px solid #00ffff',
        borderRadius: '8px',
        padding: '1rem',
        height: '200px',
        overflow: 'auto',
        fontFamily: 'monospace',
        fontSize: '0.8rem'
      }}>
        <h3 style={{ color: '#00ffff', marginBottom: '1rem', textAlign: 'center' }}>
          📜 LOGS DO PORTAL DIMENSIONAL
        </h3>
        {portalLogs.map((log, index) => (
          <div
            key={index}
            style={{
              color: getLogColor(log),
              marginBottom: '0.3rem',
              padding: '0.2rem 0.5rem',
              borderRadius: '4px',
              background: 'rgba(255, 255, 255, 0.05)'
            }}
          >
            {log}
          </div>
        ))}
      </div>

      {/* ESTILOS CSS3 AVANÇADOS */}
      <style jsx>{`
        @keyframes portalRotate {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
        
        @keyframes portalPulse {
          0% { 
            box-shadow: 
              0 0 20px #00ffff,
              0 0 40px #00ffff33,
              inset 0 0 20px #00ffff22;
          }
          100% { 
            box-shadow: 
              0 0 30px #00ffff,
              0 0 60px #00ffff66,
              inset 0 0 30px #00ffff44;
          }
        }
        
        @keyframes corePulse {
          0% { 
            transform: translate(-50%, -50%) scale(1);
            opacity: 0.8;
          }
          100% { 
            transform: translate(-50%, -50%) scale(1.2);
            opacity: 1;
          }
        }
        
        @keyframes dimensionFloat {
          0% { transform: translate(-50%, -50%) scale(1); }
          100% { transform: translate(-50%, -50%) scale(1.1) translateY(-5px); }
        }
        
        @keyframes portalActivate {
          0% { transform: scale(1); }
          50% { transform: scale(1.1); }
          100% { transform: scale(1); }
        }
      `}</style>
    </div>
  )
}

// Componentes auxiliares
const MetricCard = ({ title, value, color }: { title: string, value: string, color: string }) => (
  <div style={{
    background: 'rgba(0, 255, 255, 0.1)',
    padding: '1rem',
    borderRadius: '8px',
    border: `1px solid ${color}`,
    textAlign: 'center'
  }}>
    <div style={{ color, fontSize: '0.9rem', marginBottom: '0.5rem' }}>{title}</div>
    <div style={{ fontSize: '1.5rem', color: '#00ff88', fontWeight: 'bold' }}>{value}</div>
  </div>
)

const buttonStyle = (color: string) => ({
  background: 'transparent',
  border: `2px solid ${color}`,
  color: color,
  padding: '0.75rem 1rem',
  borderRadius: '8px',
  cursor: 'pointer',
  fontSize: '0.9rem',
  fontWeight: 'bold',
  transition: 'all 0.3s ease'
} as React.CSSProperties)

const getLogColor = (log: string) => {
  if (log.includes('✅') || log.includes('ESTABILIZADO') || log.includes('CONCLUÍDO')) return '#00ff88'
  if (log.includes('❌') || log.includes('ERRO') || log.includes('FALHA')) return '#ff4444'
  if (log.includes('INICIANDO') || log.includes('ATIVANDO')) return '#ffff00'
  return '#00ffff'
}
