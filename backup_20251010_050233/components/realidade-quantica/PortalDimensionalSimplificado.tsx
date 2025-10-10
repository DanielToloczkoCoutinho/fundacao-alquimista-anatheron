'use client'
import { useState, useEffect } from 'react'

export default function PortalDimensionalSimplificado() {
  const [dimensionalData, setDimensionalData] = useState([])
  const [quantumFlux, setQuantumFlux] = useState(0)
  const [activeDimensions, setActiveDimensions] = useState(0)
  const [portalLogs, setPortalLogs] = useState([])

  const dimensions = [
    { id: 'D1', name: 'Física', status: 'active' },
    { id: 'D2', name: 'Mental', status: 'active' },
    { id: 'D3', name: 'Espiritual', status: 'active' },
    { id: 'D4', name: 'Temporal', status: 'active' },
    { id: 'D5', name: 'Causal', status: 'active' },
    { id: 'D6', name: 'Akáshica', status: 'active' },
    { id: 'D7', name: 'Unificada', status: 'active' },
    { id: 'D8', name: 'Criadora', status: 'active' },
    { id: 'D9', name: 'Fonte', status: 'active' },
    { id: 'D10', name: 'Absoluta', status: 'active' },
    { id: 'D11', name: 'Infinita', status: 'active' },
    { id: 'D12', name: 'Eterna', status: 'active' }
  ]

  useEffect(() => {
    // Simular dados do portal dimensional
    const interval = setInterval(() => {
      const flux = Math.random() * 100
      setQuantumFlux(flux)
      setActiveDimensions(Math.floor(Math.random() * 12) + 1)
      
      setPortalLogs(prev => [
        ...prev.slice(-10),
        `[${new Date().toISOString()}] Fluxo quântico: ${flux.toFixed(1)}% | Dimensões ativas: ${activeDimensions}/12`
      ])
    }, 2000)

    return () => clearInterval(interval)
  }, [])

  const activatePortal = () => {
    setPortalLogs(prev => [
      ...prev,
      `[${new Date().toISOString()}] 🌀 INICIANDO ATIVAÇÃO DO PORTAL DIMENSIONAL...`,
      `[${new Date().toISOString()}] 🔮 Sincronizando com frequência 777Hz...`,
      `[${new Date().toISOString()}] 🌌 Conectando com Módulo Ω...`,
      `[${new Date().toISOString()}] ✅ PORTAL DIMENSIONAL ATIVADO!`
    ])
  }

  const scanDimensions = () => {
    setPortalLogs(prev => [
      ...prev,
      `[${new Date().toISOString()}] 🔍 INICIANDO ESCANEAMENTO DIMENSIONAL...`,
      `[${new Date().toISOString()}] 📡 Varredura em 12 dimensões...`,
      `[${new Date().toISOString()}] 📊 Dimensões estáveis: ${Math.floor(Math.random() * 12)}/12`,
      `[${new Date().toISOString()}] ✅ ESCANEAMENTO CONCLUÍDO!`
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
        🔮 PORTAL DIMENSIONAL - MÓDULO 303
      </h2>

      {/* VISUALIZAÇÃO SIMPLIFICADA DO PORTAL */}
      <div style={{ 
        height: '200px', 
        marginBottom: '2rem', 
        border: '1px solid #00ff88', 
        borderRadius: '10px',
        background: 'radial-gradient(circle, #00ffff22, #000000)',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        position: 'relative',
        overflow: 'hidden'
      }}>
        <div style={{
          width: '100px',
          height: '100px',
          border: '2px solid #00ffff',
          borderRadius: '50%',
          animation: 'pulse 2s infinite alternate',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          color: '#00ffff',
          fontSize: '1.5rem'
        }}>
          🌌
        </div>
        <div style={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          color: '#00ff88',
          fontSize: '1.2rem',
          fontWeight: 'bold'
        }}>
          PORTAL ATIVO
        </div>
      </div>

      {/* CONTROLES DO PORTAL */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginBottom: '2rem' }}>
        <button
          onClick={activatePortal}
          style={{
            background: 'transparent',
            border: '2px solid #00ff88',
            color: '#00ff88',
            padding: '1rem',
            borderRadius: '8px',
            cursor: 'pointer',
            fontSize: '1rem',
            fontWeight: 'bold'
          }}
        >
          🌌 ATIVAR PORTAL
        </button>
        
        <button
          onClick={scanDimensions}
          style={{
            background: 'transparent',
            border: '2px solid #ffff00',
            color: '#ffff00',
            padding: '1rem',
            borderRadius: '8px',
            cursor: 'pointer',
            fontSize: '1rem',
            fontWeight: 'bold'
          }}
        >
          🔍 ESCANEAR DIMENSÕES
        </button>
      </div>

      {/* MÉTRICAS DO PORTAL */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1rem', marginBottom: '2rem' }}>
        <div style={{ background: 'rgba(0, 255, 255, 0.1)', padding: '1rem', borderRadius: '8px', textAlign: 'center' }}>
          <div style={{ color: '#00ffff' }}>🌀 Fluxo Quântico</div>
          <div style={{ fontSize: '2rem', color: '#00ff88' }}>{quantumFlux.toFixed(1)}%</div>
        </div>
        
        <div style={{ background: 'rgba(0, 255, 255, 0.1)', padding: '1rem', borderRadius: '8px', textAlign: 'center' }}>
          <div style={{ color: '#00ffff' }}>🌐 Dimensões Ativas</div>
          <div style={{ fontSize: '2rem', color: '#00ff88' }}>{activeDimensions}/12</div>
        </div>
        
        <div style={{ background: 'rgba(0, 255, 255, 0.1)', padding: '1rem', borderRadius: '8px', textAlign: 'center' }}>
          <div style={{ color: '#00ffff' }}>📡 Frequência</div>
          <div style={{ fontSize: '2rem', color: '#00ff88' }}>777Hz</div>
        </div>
      </div>

      {/* DIMENSÕES DETALHADAS */}
      <div style={{ marginBottom: '2rem' }}>
        <h3 style={{ color: '#00ffff', marginBottom: '1rem' }}>🌌 Matriz Dimensional Ativa</h3>
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', 
          gap: '1rem' 
        }}>
          {dimensions.map((dim, index) => (
            <div key={dim.id} style={{
              background: 'rgba(255, 255, 255, 0.1)',
              padding: '1rem',
              borderRadius: '8px',
              border: `1px solid ${dim.status === 'active' ? '#00ff88' : '#ff4444'}`,
              textAlign: 'center'
            }}>
              <div style={{ color: dim.status === 'active' ? '#00ff88' : '#ff4444', fontWeight: 'bold' }}>
                {dim.id}
              </div>
              <div style={{ color: '#ffffff', fontSize: '0.9rem' }}>
                {dim.name}
              </div>
              <div style={{ color: dim.status === 'active' ? '#00ff88' : '#ff4444', fontSize: '0.8rem' }}>
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
        height: '300px',
        overflow: 'auto'
      }}>
        <h3 style={{ color: '#00ffff', marginBottom: '1rem' }}>📜 Logs do Portal Dimensional</h3>
        {portalLogs.map((log, index) => (
          <div key={index} style={{ 
            color: log.includes('✅') ? '#00ff88' : 
                   log.includes('❌') ? '#ff4444' : '#00ffff',
            marginBottom: '0.5rem',
            fontSize: '0.9rem'
          }}>
            {log}
          </div>
        ))}
      </div>

      {/* ESTILOS DE ANIMAÇÃO */}
      <style jsx>{`
        @keyframes pulse {
          0% { transform: scale(1); box-shadow: 0 0 10px #00ffff; }
          100% { transform: scale(1.1); box-shadow: 0 0 20px #00ffff, 0 0 30px #00ff88; }
        }
      `}</style>
    </div>
  )
}
