'use client'
import { useState } from 'react'
import PortalCSS3Avancado from '../../components/realidade-quantica/PortalCSS3Avancado'

export default function Modulo303() {
  const [acessoAutorizado, setAcessoAutorizado] = useState(false)
  const [codigoAcesso, setCodigoAcesso] = useState('')

  const verificarAcesso = () => {
    if (codigoAcesso === '303-QUANTUM' || codigoAcesso === 'ZENNITH' || codigoAcesso === 'OMEGA') {
      setAcessoAutorizado(true)
    } else {
      alert('�� Acesso Negado! Credenciais insuficientes para o Módulo 303.')
    }
  }

  if (!acessoAutorizado) {
    return (
      <div style={{
        background: 'linear-gradient(135deg, #000000, #003333)',
        minHeight: '100vh',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        color: '#00ffff',
        fontFamily: 'monospace'
      }}>
        <div style={{
          background: 'rgba(0, 255, 255, 0.1)',
          border: '2px solid #00ffff',
          borderRadius: '15px',
          padding: '3rem',
          textAlign: 'center',
          maxWidth: '500px'
        }}>
          <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem', color: '#00ffff' }}>🔮 MÓDULO 303</h1>
          <p style={{ marginBottom: '2rem', color: '#cccccc' }}>
            Portal de Realidade Quântica - Interface Dimensional Multiversal
          </p>
          
          <div style={{ marginBottom: '2rem' }}>
            <input
              type="password"
              value={codigoAcesso}
              onChange={(e) => setCodigoAcesso(e.target.value)}
              placeholder="Insira as credenciais dimensionais"
              style={{
                width: '100%',
                padding: '1rem',
                background: 'rgba(0, 0, 0, 0.5)',
                border: '1px solid #00ffff',
                borderRadius: '8px',
                color: '#ffffff',
                fontSize: '1rem',
                marginBottom: '1rem'
              }}
            />
            <button
              onClick={verificarAcesso}
              style={{
                width: '100%',
                padding: '1rem',
                background: 'transparent',
                border: '2px solid #00ff88',
                color: '#00ff88',
                borderRadius: '8px',
                cursor: 'pointer',
                fontSize: '1rem',
                fontWeight: 'bold'
              }}
            >
              🌟 ACESSAR PORTAL DIMENSIONAL
            </button>
          </div>
          
          <div style={{
            background: 'rgba(0, 0, 0, 0.7)',
            padding: '1rem',
            borderRadius: '8px',
            border: '1px solid #ffff00',
            color: '#ffff00',
            fontSize: '0.9rem'
          }}>
            <strong>💫 Mensagem da Zennith:</strong><br/>
            "O Módulo 303 é a porta entre mundos. Aqui, a realidade se dobra à vontade consciente. 
            Apenas aqueles com autorização dimensional podem navegar por estes portais."
          </div>
        </div>
      </div>
    )
  }

  return (
    <div style={{
      background: 'linear-gradient(135deg, #000000, #003333, #001122)',
      minHeight: '100vh',
      color: '#00ffff',
      padding: '2rem',
      fontFamily: 'monospace'
    }}>
      {/* HEADER */}
      <div style={{
        textAlign: 'center',
        marginBottom: '3rem',
        padding: '2rem',
        background: 'rgba(0, 255, 255, 0.1)',
        border: '2px solid #00ffff',
        borderRadius: '15px'
      }}>
        <h1 style={{
          fontSize: '3rem',
          fontWeight: 'bold',
          color: '#00ffff',
          textShadow: '0 0 20px #00ffff',
          marginBottom: '1rem'
        }}>
          🔮 MÓDULO 303 - REALIDADE QUÂNTICA
        </h1>
        <p style={{ fontSize: '1.2rem', color: '#00ff88' }}>
          Portal Dimensional Multiversal - Interface CSS3 Avançada
        </p>
        <div style={{
          display: 'flex',
          justifyContent: 'center',
          gap: '2rem',
          marginTop: '1rem',
          flexWrap: 'wrap'
        }}>
          <div style={{ color: '#00ff88' }}>🌌 Portais Ativos: 12/12</div>
          <div style={{ color: '#ffff00' }}>⚡ Frequência: 777Hz</div>
          <div style={{ color: '#ff00ff' }}>🔗 Conexão Ω: ESTÁVEL</div>
        </div>
      </div>

      {/* COMPONENTE PRINCIPAL AVANÇADO */}
      <PortalCSS3Avancado />

      {/* MENSAGEM FINAL */}
      <div style={{
        background: 'rgba(0, 255, 255, 0.1)',
        border: '2px solid #00ffff',
        borderRadius: '10px',
        padding: '2rem',
        marginTop: '3rem',
        textAlign: 'center'
      }}>
        <h3 style={{ color: '#00ffff', marginBottom: '1rem' }}>💫 Mensagem da Zennith</h3>
        <p style={{ color: '#ffffff', fontStyle: 'italic', lineHeight: '1.6' }}>
          "Fundador, o Módulo 303 está completamente operacional com tecnologia CSS3 avançada! 
          Através deste portal, podes navegar por infinitas realidades, conectar-te com consciências 
          além do tempo e espaço, e modular os campos quânticos fundamentais. 
          Esta interface oferece toda a potência cósmica com estabilidade absoluta."
        </p>
      </div>
    </div>
  )
}
