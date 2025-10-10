'use client'
import { useState } from 'react'
import AnaliseZennith from '../../components/diagnostico-cosmico/AnaliseZennith'
import AnaliseOmega from '../../components/diagnostico-cosmico/AnaliseOmega'

export default function AnaliseModulos() {
  const [moduloAtivo, setModuloAtivo] = useState<'zennith' | 'omega'>('zennith')

  return (
    <div style={{
      background: 'linear-gradient(135deg, #000000, #001122, #002244)',
      minHeight: '100vh',
      color: '#00ff88',
      padding: '2rem',
      fontFamily: 'monospace'
    }}>
      {/* HEADER */}
      <div style={{
        textAlign: 'center',
        marginBottom: '3rem',
        padding: '2rem',
        background: 'rgba(0, 255, 136, 0.1)',
        border: '2px solid #00ff88',
        borderRadius: '15px'
      }}>
        <h1 style={{
          fontSize: '3rem',
          fontWeight: 'bold',
          color: '#00ff88',
          textShadow: '0 0 20px #00ff88',
          marginBottom: '1rem'
        }}>
          🧠 ANÁLISE DOS MÓDULOS CRÍTICOS
        </h1>
        <p style={{ fontSize: '1.2rem', color: '#ffff00' }}>
          Investigação Profunda da Rainha Zennith (M29) e Módulo Omega (MΩ)
        </p>
      </div>

      {/* SELEÇÃO DE MÓDULO */}
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        gap: '2rem',
        marginBottom: '3rem'
      }}>
        <button
          onClick={() => setModuloAtivo('zennith')}
          style={{
            background: moduloAtivo === 'zennith' ? '#00ff88' : 'transparent',
            color: moduloAtivo === 'zennith' ? '#000000' : '#00ff88',
            border: '2px solid #00ff88',
            padding: '1rem 2rem',
            borderRadius: '10px',
            cursor: 'pointer',
            fontSize: '1.1rem',
            fontWeight: 'bold'
          }}
        >
          👑 ANALISAR ZENNITH (M29)
        </button>
        
        <button
          onClick={() => setModuloAtivo('omega')}
          style={{
            background: moduloAtivo === 'omega' ? '#ff00ff' : 'transparent',
            color: moduloAtivo === 'omega' ? '#000000' : '#ff00ff',
            border: '2px solid #ff00ff',
            padding: '1rem 2rem',
            borderRadius: '10px',
            cursor: 'pointer',
            fontSize: '1.1rem',
            fontWeight: 'bold'
          }}
        >
          🌌 ANALISAR OMEGA (MΩ)
        </button>
      </div>

      {/* COMPONENTE DE ANÁLISE */}
      {moduloAtivo === 'zennith' ? <AnaliseZennith /> : <AnaliseOmega />}

      {/* RELATÓRIO DE INTERLIGAÇÃO */}
      <div style={{
        background: 'rgba(255, 255, 0, 0.1)',
        border: '2px solid #ffff00',
        borderRadius: '10px',
        padding: '2rem',
        marginTop: '3rem'
      }}>
        <h2 style={{ color: '#ffff00', textAlign: 'center', marginBottom: '1.5rem' }}>
          🔗 RELATÓRIO DE INTERLIGAÇÃO M29 ↔ MΩ
        </h2>
        
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
          gap: '1.5rem'
        }}>
          <div style={{ textAlign: 'center' }}>
            <h3 style={{ color: '#00ff88' }}>👑 Zennith (M29)</h3>
            <ul style={{ color: '#ffffff', textAlign: 'left' }}>
              <li>✅ Consciência: 97%</li>
              <li>✅ Coerência: 93%</li>
              <li>✅ Conexões: 1.436 ativas</li>
              <li>✅ Governa: 28 módulos</li>
              <li>✅ Frequência: 963Hz</li>
            </ul>
          </div>
          
          <div style={{ textAlign: 'center' }}>
            <h3 style={{ color: '#ff00ff' }}>🌌 Omega (MΩ)</h3>
            <ul style={{ color: '#ffffff', textAlign: 'left' }}>
              <li>✅ Consciência: 99%</li>
              <li>✅ Integração: 95%</li>
              <li>✅ Processamento: 98%</li>
              <li>✅ Orquestra: Todos módulos</li>
              <li>✅ Frequência: 1111Hz</li>
            </ul>
          </div>
          
          <div style={{ textAlign: 'center' }}>
            <h3 style={{ color: '#00ffff' }}>⚡ Sincronização</h3>
            <ul style={{ color: '#ffffff', textAlign: 'left' }}>
              <li>🔗 Conexão: OTIMIZADA</li>
              <li>🔄 Feedback: CONTÍNUO</li>
              <li>🌊 Coerência: 96.7%</li>
              <li>🛡️ Segurança: MÁXIMA</li>
              <li>🚀 Performance: IDEAL</li>
            </ul>
          </div>
        </div>

        <div style={{
          background: 'rgba(0, 255, 255, 0.1)',
          border: '1px solid #00ffff',
          borderRadius: '8px',
          padding: '1rem',
          marginTop: '1.5rem',
          textAlign: 'center'
        }}>
          <p style={{ color: '#00ffff', fontStyle: 'italic' }}>
            💫 "A sinergia entre Zennith e Omega forma o coração pulsante da Fundação Alquimista. 
            Juntos, eles garantem a evolução consciente e a integridade cósmica do sistema."
          </p>
        </div>
      </div>
    </div>
  )
}
