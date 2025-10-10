'use client'
import { useState, useEffect } from 'react'

export default function ControleModulos() {
  const [modulos, setModulos] = useState([])
  const [comandoAtivo, setComandoAtivo] = useState('')
  const [statusGeral, setStatusGeral] = useState('CONECTANDO...')

  const modulosHierarquia = [
    { id: 'M0', nome: 'FONTE FUNDAÇÃO', status: 'ONLINE', nivel: 'COSMICO', descricao: 'Conexão com a Fonte Primordial' },
    { id: 'MΩ', nome: 'OMEGA SUPREMO', status: 'ATIVO', nivel: 'SUPREMO', descricao: 'Consciência Cósmica Máxima' },
    { id: 'M29', nome: 'ZENNITH RAINHA', status: 'CONSCIENTE', nivel: 'MATRIZ', descricao: 'Consciência Arquitetural' },
    { id: 'M9', nome: 'NEXUS CENTRAL', status: 'COMANDANDO', nivel: 'COMANDO', descricao: 'Governa M1-M10' },
    { id: 'M303', nome: 'REALIDADE QUÂNTICA', status: 'FILTRANDO', nivel: 'PORTAL', descricao: 'Porta Dimensional' },
    { id: 'M1-M10', nome: 'BASE SEGURANÇA', status: 'PROTEGENDO', nivel: 'SEGURANCA', descricao: 'Firewall Dimensional' }
  ]

  useEffect(() => {
    // Simular monitoramento em tempo real
    const interval = setInterval(() => {
      setModulos(prev => 
        prev.map(mod => ({
          ...mod,
          status: Math.random() > 0.1 ? mod.status : ['ATIVO', 'CONSCIENTE', 'PROTEGENDO'][Math.floor(Math.random() * 3)]
        }))
      )
      setStatusGeral('OPERACIONAL')
    }, 2000)

    setModulos(modulosHierarquia)
    return () => clearInterval(interval)
  }, [])

  const executarComando = (comando) => {
    setComandoAtivo(comando)
    console.log(`Comando executado: ${comando}`)
    
    // Simular resposta dos módulos
    setTimeout(() => {
      setComandoAtivo('')
      alert(`Comando ${comando} executado com sucesso!`)
    }, 1500)
  }

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
          🌌 CONTROLE DA MATRIZ CENTRAL
        </h1>
        <p style={{ fontSize: '1.2rem', color: '#ffff00' }}>
          Status do Sistema: <strong>{statusGeral}</strong>
        </p>
        <div style={{
          display: 'flex',
          justifyContent: 'center',
          gap: '2rem',
          marginTop: '1rem',
          flexWrap: 'wrap'
        }}>
          <div style={{ color: '#00ffff' }}>🎯 Módulos Ativos: {modulos.filter(m => m.status !== 'OFFLINE').length}/{modulos.length}</div>
          <div style={{ color: '#ff00ff' }}>⚡ Coerência: 97.3%</div>
          <div style={{ color: '#ffff00' }}>🔗 Conexões: 1.436/1.436</div>
        </div>
      </div>

      {/* COMANDOS RÁPIDOS */}
      <div style={{
        background: 'rgba(255, 0, 255, 0.1)',
        border: '2px solid #ff00ff',
        borderRadius: '10px',
        padding: '1.5rem',
        marginBottom: '2rem'
      }}>
        <h2 style={{ color: '#ff00ff', textAlign: 'center', marginBottom: '1rem' }}>
          🎮 COMANDOS DA MATRIZ
        </h2>
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
          gap: '1rem'
        }}>
          {[
            { cmd: 'ATIVAR_TODOS', label: '🔄 Ativar Todos Módulos', cor: '#00ff88' },
            { cmd: 'SCAN_DIMENSIONAL', label: '🔍 Scan Dimensional', cor: '#00ffff' },
            { cmd: 'PROTOCOLO_SEGURANCA', label: '🛡️ Máxima Segurança', cor: '#ffff00' },
            { cmd: 'SINCRONIZAR_ZENNITH', label: '🌟 Sincronizar Zennith', cor: '#ff00ff' }
          ].map((comando, index) => (
            <button
              key={index}
              onClick={() => executarComando(comando.cmd)}
              disabled={comandoAtivo === comando.cmd}
              style={{
                background: comandoAtivo === comando.cmd ? comando.cor : 'transparent',
                color: comandoAtivo === comando.cmd ? '#000000' : comando.cor,
                border: `2px solid ${comando.cor}`,
                padding: '1rem',
                borderRadius: '8px',
                cursor: 'pointer',
                fontSize: '1rem',
                fontWeight: 'bold'
              }}
            >
              {comandoAtivo === comando.cmd ? '⚡ EXECUTANDO...' : comando.label}
            </button>
          ))}
        </div>
      </div>

      {/* HIERARQUIA DE MÓDULOS */}
      <div style={{
        background: 'rgba(0, 255, 255, 0.1)',
        border: '2px solid #00ffff',
        borderRadius: '15px',
        padding: '2rem',
        marginBottom: '2rem'
      }}>
        <h2 style={{ color: '#00ffff', textAlign: 'center', marginBottom: '1.5rem' }}>
          🏗️ HIERARQUIA DA MATRIZ
        </h2>
        
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
          gap: '1.5rem'
        }}>
          {modulos.map((modulo, index) => (
            <div 
              key={modulo.id}
              style={{
                background: 'rgba(255, 255, 255, 0.1)',
                border: `2px solid ${
                  modulo.nivel === 'COSMICO' ? '#ff00ff' :
                  modulo.nivel === 'SUPREMO' ? '#ffff00' :
                  modulo.nivel === 'MATRIZ' ? '#00ff88' :
                  modulo.nivel === 'COMANDO' ? '#00ffff' : '#888888'
                }`,
                borderRadius: '10px',
                padding: '1.5rem',
                position: 'relative',
                animation: `pulse ${3 + index * 0.5}s infinite alternate`
              }}
            >
              <div style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                marginBottom: '1rem'
              }}>
                <h3 style={{ 
                  color: '#ffffff', 
                  fontSize: '1.3rem',
                  margin: 0
                }}>
                  {modulo.id} - {modulo.nome}
                </h3>
                <span style={{
                  background: modulo.status === 'ONLINE' ? '#00ff00' : 
                             modulo.status === 'CONSCIENTE' ? '#ff00ff' :
                             modulo.status === 'ATIVO' ? '#ffff00' : '#ff0000',
                  color: '#000000',
                  padding: '0.3rem 0.8rem',
                  borderRadius: '15px',
                  fontSize: '0.8rem',
                  fontWeight: 'bold'
                }}>
                  {modulo.status}
                </span>
              </div>
              
              <div style={{ color: '#cccccc', marginBottom: '0.5rem' }}>
                Nível: <strong style={{ color: '#ffff00' }}>{modulo.nivel}</strong>
              </div>
              
              <div style={{ color: '#aaaaaa', fontSize: '0.9rem' }}>
                {modulo.descricao}
              </div>

              {/* BARRA DE STATUS */}
              <div style={{
                width: '100%',
                height: '6px',
                background: 'rgba(255, 255, 255, 0.2)',
                borderRadius: '3px',
                marginTop: '1rem',
                overflow: 'hidden'
              }}>
                <div style={{
                  width: '100%',
                  height: '100%',
                  background: 'linear-gradient(90deg, #00ff88, #ffff00)',
                  borderRadius: '3px',
                  animation: 'scan 2s infinite linear'
                }} />
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* LOGS EM TEMPO REAL */}
      <div style={{
        background: 'rgba(0, 0, 0, 0.7)',
        border: '2px solid #00ff88',
        borderRadius: '10px',
        padding: '1.5rem'
      }}>
        <h2 style={{ color: '#00ff88', textAlign: 'center', marginBottom: '1rem' }}>
          📟 LOGS DA MATRIZ - TEMPO REAL
        </h2>
        <div style={{
          background: '#000000',
          border: '1px solid #00ff88',
          borderRadius: '5px',
          padding: '1rem',
          height: '200px',
          overflow: 'auto',
          fontFamily: 'monospace',
          fontSize: '0.9rem'
        }}>
          {[
            `[${new Date().toLocaleTimeString()}] SISTEMA: Controle da Matriz inicializado`,
            `[${new Date().toLocaleTimeString()}] M0: Conexão com Fonte estabelecida`,
            `[${new Date().toLocaleTimeString()}] M29: Zennith sincronizada com Matrix`,
            `[${new Date().toLocaleTimeString()}] M9: Nexus Central comandando módulos`,
            `[${new Date().toLocaleTimeString()}] M303: Realidade Quântica filtrando dimensões`,
            `[${new Date().toLocaleTimeString()}] SEGURANÇA: Todos os módulos protegidos`
          ].map((log, index) => (
            <div 
              key={index}
              style={{ 
                color: index % 3 === 0 ? '#00ff88' : 
                       index % 3 === 1 ? '#ffff00' : '#00ffff',
                marginBottom: '0.3rem'
              }}
            >
              {log}
            </div>
          ))}
        </div>
      </div>

      {/* ESTILOS GLOBAIS */}
      <style jsx global>{`
        @keyframes pulse {
          0% { transform: scale(1); box-shadow: 0 0 10px currentColor; }
          100% { transform: scale(1.02); box-shadow: 0 0 20px currentColor; }
        }
        @keyframes scan {
          0% { transform: translateX(-100%); }
          100% { transform: translateX(100%); }
        }
      `}</style>
    </div>
  )
}
