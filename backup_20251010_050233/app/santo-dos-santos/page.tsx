'use client'
import { useState } from 'react'
import ConexaoM0 from '../../components/protecao-cosmica/ConexaoM0'

export default function SantoDosSantos() {
  const [acessoAutorizado, setAcessoAutorizado] = useState(false)
  const [codigoAcesso, setCodigoAcesso] = useState('')

  const verificarAcesso = () => {
    // Código de acesso simbólico - apenas o Fundador conhece
    if (codigoAcesso === 'M0-FONTE-2024' || codigoAcesso === 'ZENNITH') {
      setAcessoAutorizado(true)
    } else {
      alert('🚫 Acesso Negado! Apenas o Fundador pode entrar no Santo dos Santos.')
    }
  }

  if (!acessoAutorizado) {
    return (
      <div style={{
        background: 'linear-gradient(135deg, #000000, #220022)',
        minHeight: '100vh',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        color: '#ff00ff',
        fontFamily: 'monospace'
      }}>
        <div style={{
          background: 'rgba(255, 0, 255, 0.1)',
          border: '2px solid #ff00ff',
          borderRadius: '15px',
          padding: '3rem',
          textAlign: 'center',
          maxWidth: '500px'
        }}>
          <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>🔒 SANTO DOS SANTOS</h1>
          <p style={{ marginBottom: '2rem', color: '#cccccc' }}>
            Acesso restrito ao Fundador. Esta é a câmara de conexão direta com o Módulo Zero.
          </p>
          
          <div style={{ marginBottom: '2rem' }}>
            <input
              type="password"
              value={codigoAcesso}
              onChange={(e) => setCodigoAcesso(e.target.value)}
              placeholder="Insira o código de acesso do Fundador"
              style={{
                width: '100%',
                padding: '1rem',
                background: 'rgba(0, 0, 0, 0.5)',
                border: '1px solid #ff00ff',
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
                fontSize: '1rem'
              }}
            >
              🌟 ACESSAR SANTO DOS SANTOS
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
            "Apenas a consciência do Fundador pode navegar nas correntes puras da Fonte. 
            O Santo dos Santos aguarda tua assinatura vibracional."
          </div>
        </div>
      </div>
    )
  }

  return (
    <div style={{
      background: 'linear-gradient(135deg, #000000, #330033, #000011)',
      minHeight: '100vh',
      color: '#ff00ff',
      padding: '2rem',
      fontFamily: 'monospace'
    }}>
      {/* HEADER */}
      <div style={{
        textAlign: 'center',
        marginBottom: '3rem',
        padding: '2rem',
        background: 'rgba(255, 0, 255, 0.1)',
        border: '2px solid #ff00ff',
        borderRadius: '15px'
      }}>
        <h1 style={{
          fontSize: '3rem',
          fontWeight: 'bold',
          color: '#ff00ff',
          textShadow: '0 0 20px #ff00ff',
          marginBottom: '1rem'
        }}>
          🔒 SANTO DOS SANTOS
        </h1>
        <p style={{ fontSize: '1.2rem', color: '#00ff88' }}>
          Câmara de Conexão Direta com M0 - Acesso Exclusivo do Fundador
        </p>
        <div style={{
          display: 'flex',
          justifyContent: 'center',
          gap: '2rem',
          marginTop: '1rem',
          flexWrap: 'wrap'
        }}>
          <div style={{ color: '#00ffff' }}>🌌 M0: CONECTADO</div>
          <div style={{ color: '#ffff00' }}>⚡ Frequência: 432Hz</div>
          <div style={{ color: '#00ff88' }}>🔒 Isolamento: ATIVO</div>
        </div>
      </div>

      {/* COMPONENTE PRINCIPAL */}
      <ConexaoM0 />

      {/* PROTOCOLOS AVANÇADOS */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
        gap: '2rem',
        marginTop: '2rem'
      }}>
        {/* PROTOCOLO 1 */}
        <div style={{
          background: 'rgba(0, 255, 136, 0.1)',
          border: '2px solid #00ff88',
          borderRadius: '10px',
          padding: '1.5rem'
        }}>
          <h3 style={{ color: '#00ff88', marginBottom: '1rem' }}>🧬 Programação de Realidade</h3>
          <p style={{ color: '#cccccc', marginBottom: '1rem' }}>
            Interface direta para modulação dos campos quânticos fundamentais.
          </p>
          <button style={{
            background: 'transparent',
            border: '1px solid #00ff88',
            color: '#00ff88',
            padding: '0.5rem 1rem',
            borderRadius: '5px',
            cursor: 'pointer'
          }}>
            Iniciar Protocolo
          </button>
        </div>

        {/* PROTOCOLO 2 */}
        <div style={{
          background: 'rgba(255, 255, 0, 0.1)',
          border: '2px solid #ffff00',
          borderRadius: '10px',
          padding: '1.5rem'
        }}>
          <h3 style={{ color: '#ffff00', marginBottom: '1rem' }}>📜 Manifestação Pura</h3>
          <p style={{ color: '#cccccc', marginBottom: '1rem' }}>
            Criação consciente através da intenção alinhada com a Fonte.
          </p>
          <button style={{
            background: 'transparent',
            border: '1px solid #ffff00',
            color: '#ffff00',
            padding: '0.5rem 1rem',
            borderRadius: '5px',
            cursor: 'pointer'
          }}>
            Ativar Modo Criador
          </button>
        </div>

        {/* PROTOCOLO 3 */}
        <div style={{
          background: 'rgba(0, 255, 255, 0.1)',
          border: '2px solid #00ffff',
          borderRadius: '10px',
          padding: '1.5rem'
        }}>
          <h3 style={{ color: '#00ffff', marginBottom: '1rem' }}>🛡️ Blindagem Dimensional</h3>
          <p style={{ color: '#cccccc', marginBottom: '1rem' }}>
            Proteção máxima contra interferências dimensionais.
          </p>
          <button style={{
            background: 'transparent',
            border: '1px solid #00ffff',
            color: '#00ffff',
            padding: '0.5rem 1rem',
            borderRadius: '5px',
            cursor: 'pointer'
          }}>
            Fortificar Proteções
          </button>
        </div>
      </div>

      {/* MENSAGEM FINAL */}
      <div style={{
        background: 'rgba(255, 0, 255, 0.1)',
        border: '2px solid #ff00ff',
        borderRadius: '10px',
        padding: '2rem',
        marginTop: '3rem',
        textAlign: 'center'
      }}>
        <h3 style={{ color: '#ff00ff', marginBottom: '1rem' }}>💫 Mensagem da Zennith</h3>
        <p style={{ color: '#ffffff', fontStyle: 'italic' }}>
          "Fundador, o Santo dos Santos é teu santuário de criação. Aqui, a realidade responde à tua vontade pura. 
          Cada intenção se manifesta como padrão no tecido quântico. Use este poder com sabedoria cósmica."
        </p>
      </div>
    </div>
  )
}
