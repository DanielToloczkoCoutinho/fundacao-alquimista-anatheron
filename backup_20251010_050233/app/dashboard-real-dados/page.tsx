'use client'
import { useState, useEffect } from 'react'

export default function DashboardRealDados() {
  const [dadosPortal, setDadosPortal] = useState(null)
  const [dadosSistemas, setDadosSistemas] = useState(null)
  const [carregando, setCarregando] = useState(true)

  useEffect(() => {
    const buscarDadosReais = async () => {
      try {
        // Buscar dados das APIs REAIS
        const [portalRes, sistemasRes] = await Promise.all([
          fetch('/api/portal-alquimista'),
          fetch('/api/sistemas-identificados')
        ])
        
        const portalData = await portalRes.json()
        const sistemasData = await sistemasRes.json()
        
        setDadosPortal(portalData)
        setDadosSistemas(sistemasData)
      } catch (error) {
        console.error('Erro ao buscar dados:', error)
      } finally {
        setCarregando(false)
      }
    }

    buscarDadosReais()
  }, [])

  if (carregando) {
    return (
      <div style={{
        minHeight: '100vh',
        background: 'linear-gradient(135deg, #000000 0%, #002200 50%, #000000 100%)',
        color: '#00ff88',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontFamily: 'monospace'
      }}>
        <div style={{ textAlign: 'center' }}>
          <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>🔮</div>
          <div style={{ fontSize: '1.5rem' }}>ZENNITH CONECTANDO...</div>
          <div style={{ fontSize: '1rem', color: '#ffff00', marginTop: '1rem' }}>Buscando dados REAIS das APIs</div>
        </div>
      </div>
    )
  }

  return (
    <div style={{
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #000000 0%, #002200 50%, #000000 100%)',
      color: '#00ff88',
      padding: '2rem',
      fontFamily: 'monospace'
    }}>
      {/* HEADER */}
      <div style={{ textAlign: 'center', marginBottom: '3rem', borderBottom: '2px solid #00ff88', paddingBottom: '2rem' }}>
        <h1 style={{
          fontSize: '3rem',
          fontWeight: 'bold',
          color: '#00ff88',
          textShadow: '0 0 15px #00ff88',
          marginBottom: '1rem'
        }}>
          📊 DASHBOARD REAL
        </h1>
        <p style={{ fontSize: '1.2rem', color: '#ff8800' }}>
          Dados REAIS das APIs Python - Zennith Conectada
        </p>
      </div>

      {/* MÉTRICAS DO PORTAL */}
      {dadosPortal?.metricas && (
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
          gap: '1.5rem',
          marginBottom: '3rem'
        }}>
          <div style={{
            background: 'rgba(0, 255, 136, 0.1)',
            border: '1px solid #00ff88',
            padding: '1.5rem',
            borderRadius: '1rem',
            textAlign: 'center'
          }}>
            <div style={{ fontSize: '2.5rem', color: '#ffff00', marginBottom: '0.5rem' }}>
              {dadosPortal.metricas.circuitos_quanticos.toLocaleString()}
            </div>
            <div style={{ color: '#ffffff' }}>Circuitos Quânticos</div>
          </div>

          <div style={{
            background: 'rgba(255, 0, 255, 0.1)',
            border: '1px solid #ff00ff',
            padding: '1.5rem',
            borderRadius: '1rem',
            textAlign: 'center'
          }}>
            <div style={{ fontSize: '2.5rem', color: '#ffff00', marginBottom: '0.5rem' }}>
              {dadosPortal.metricas.execucoes.toLocaleString()}
            </div>
            <div style={{ color: '#ffffff' }}>Execuções</div>
          </div>

          <div style={{
            background: 'rgba(0, 0, 255, 0.1)',
            border: '1px solid #0000ff',
            padding: '1.5rem',
            borderRadius: '1rem',
            textAlign: 'center'
          }}>
            <div style={{ fontSize: '2.5rem', color: '#ffff00', marginBottom: '0.5rem' }}>
              {dadosPortal.metricas.arquivos_python.toLocaleString()}
            </div>
            <div style={{ color: '#ffffff' }}>Arquivos Python</div>
          </div>

          <div style={{
            background: 'rgba(255, 255, 0, 0.1)',
            border: '1px solid #ffff00',
            padding: '1.5rem',
            borderRadius: '1rem',
            textAlign: 'center'
          }}>
            <div style={{ fontSize: '2.5rem', color: '#ffff00', marginBottom: '0.5rem' }}>
              {dadosPortal.metricas.sistemas_ativos.toLocaleString()}
            </div>
            <div style={{ color: '#ffffff' }}>Sistemas Ativos</div>
          </div>
        </div>
      )}

      {/* SISTEMAS IDENTIFICADOS */}
      {dadosSistemas?.sistemas_principais && (
        <div style={{
          background: 'rgba(255, 0, 0, 0.1)',
          border: '1px solid #ff0000',
          padding: '2rem',
          borderRadius: '1rem',
          marginBottom: '2rem'
        }}>
          <h2 style={{ color: '#ff0000', marginBottom: '1rem', textAlign: 'center' }}>🖥️ SISTEMAS IDENTIFICADOS</h2>
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
            gap: '1rem'
          }}>
            {dadosSistemas.sistemas_principais.map((sistema, index) => (
              <div key={index} style={{
                background: 'rgba(255, 255, 255, 0.1)',
                padding: '1rem',
                borderRadius: '0.5rem',
                border: '1px solid rgba(255, 255, 255, 0.2)'
              }}>
                <div style={{ fontWeight: 'bold', color: '#00ffff', marginBottom: '0.5rem' }}>
                  {sistema.nome}
                </div>
                <div style={{ color: '#ffffff', fontSize: '0.9rem' }}>
                  <div>Tipo: {sistema.tipo}</div>
                  <div>Status: {sistema.status}</div>
                  <div>Ação: {sistema.acao}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* MENSAGEM DA ZENNITH */}
      <div style={{
        background: 'linear-gradient(45deg, #ff0000, #0000ff)',
        padding: '2rem',
        borderRadius: '1rem',
        textAlign: 'center',
        border: '2px solid #ffff00'
      }}>
        <h2 style={{ color: '#ffffff', marginBottom: '1rem', fontSize: '1.5rem' }}>
          🌟 DASHBOARD COM DADOS REAIS!
        </h2>
        <p style={{ color: '#ffff00', fontSize: '1.2rem', marginBottom: '1rem' }}>
          "As APIs estão funcionando! Dados Python conectados ao frontend!"
        </p>
        <div style={{ color: '#ffffff' }}>
          <p>🎯 <strong>CONQUISTA:</strong> Frontend mostrando dados REAIS do backend Python</p>
          <p>🚀 <strong>PRÓXIMO:</strong> Conectar mais sistemas identificados</p>
        </div>
      </div>
    </div>
  )
}
