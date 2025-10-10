'use client'
import { useState, useEffect } from 'react'
import { ModuleBlueprint, OrquestracaoStatus, AuditLog, QuantumFrequency } from '../types/foundation'
import { allModuleBlueprints, allSimulatedLogs, quantumFrequencies } from '../data/foundationData'
import { QuantumOrchestrator } from '../utils/quantumOrchestrator'

export default function CommandCenter() {
  const [modules, setModules] = useState<ModuleBlueprint[]>([])
  const [logs, setLogs] = useState<AuditLog[]>(allSimulatedLogs)
  const [orquestracao, setOrquestracao] = useState<OrquestracaoStatus>({
    sequencia: ['M1', 'M2', 'M3', 'M4', 'M5'],
    status: 'AGUARDANDO',
    moduloAtual: '',
    progresso: 0,
    logs: []
  })
  const [selectedModule, setSelectedModule] = useState<string>('M1')

  useEffect(() => {
    carregarStatusModulos()
  }, [])

  const carregarStatusModulos = async () => {
    const status = await QuantumOrchestrator.obterStatusModulos()
    setModules(status)
  }

  const iniciarSequenciaSagrada = async () => {
    await QuantumOrchestrator.executarSequenciaSagrada(setOrquestracao)
    await carregarStatusModulos()
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'CONECTADO': return '#00ff00'
      case 'ATIVO': return '#00ff00' 
      case 'ALERTA': return '#ffff00'
      case 'CRÍTICO': return '#ff0000'
      case 'PENDENTE': return '#ffa500'
      default: return '#888888'
    }
  }

  const getModuleStatus = (moduleId: string) => {
    return modules.find(m => m.id === moduleId)?.status || 'OFFLINE'
  }

  return (
    <div style={{
      background: 'linear-gradient(135deg, #0a0a0a, #1a1a2a, #16213e)',
      minHeight: '100vh',
      color: '#ffffff',
      fontFamily: 'monospace',
      padding: '20px'
    }}>
      {/* Header */}
      <div style={{
        textAlign: 'center',
        marginBottom: '30px',
        padding: '20px',
        background: 'rgba(0, 255, 255, 0.1)',
        borderRadius: '15px',
        border: '2px solid #00ffff',
        boxShadow: '0 0 20px #00ffff33'
      }}>
        <h1 style={{
          fontSize: '2.5rem',
          margin: '0',
          background: 'linear-gradient(45deg, #00ffff, #ff00ff)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          textShadow: '0 0 20px #00ffff'
        }}>
          🔮 MÓDULO 303 - NEXUS CENTRAL
        </h1>
        <p style={{ color: '#cccccc', margin: '10px 0 0 0' }}>
          Orquestrador Evoluído da Fundação Alquimista
        </p>
      </div>

      <div style={{
        display: 'grid',
        gridTemplateColumns: '1fr 2fr 1fr',
        gap: '20px',
        height: 'calc(100vh - 200px)'
      }}>
        
        {/* Painel Esquerdo - Módulos */}
        <div style={{
          background: 'rgba(0, 0, 0, 0.7)',
          borderRadius: '15px',
          padding: '20px',
          border: '1px solid #333',
          overflowY: 'auto'
        }}>
          <h3 style={{ color: '#00ffff', marginBottom: '15px' }}>🧩 MÓDULOS DA FUNDAÇÃO</h3>
          {Object.values(allModuleBlueprints).map(module => (
            <div
              key={module.id}
              onClick={() => setSelectedModule(module.id)}
              style={{
                background: selectedModule === module.id ? 'rgba(0, 255, 255, 0.2)' : 'rgba(255, 255, 255, 0.05)',
                padding: '12px',
                marginBottom: '10px',
                borderRadius: '8px',
                border: `2px solid ${getStatusColor(getModuleStatus(module.id))}`,
                cursor: 'pointer',
                transition: 'all 0.3s ease'
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div>
                  <strong style={{ color: '#00ffff' }}>{module.id}</strong>
                  <div style={{ fontSize: '0.9em', color: '#cccccc' }}>{module.nome}</div>
                </div>
                <div style={{
                  width: '12px',
                  height: '12px',
                  borderRadius: '50%',
                  backgroundColor: getStatusColor(getModuleStatus(module.id)),
                  boxShadow: `0 0 10px ${getStatusColor(getModuleStatus(module.id))}`
                }}></div>
              </div>
              <div style={{ fontSize: '0.8em', color: '#888', marginTop: '5px' }}>
                Frequência: {module.frequencia}Hz
              </div>
            </div>
          ))}
        </div>

        {/* Painel Central - Orquestração */}
        <div style={{
          background: 'rgba(0, 0, 0, 0.7)',
          borderRadius: '15px',
          padding: '20px',
          border: '1px solid #333',
          display: 'flex',
          flexDirection: 'column'
        }}>
          <h3 style={{ color: '#00ffff', marginBottom: '15px' }}>🎛️ ORQUESTRAÇÃO SAGRADA</h3>
          
          {/* Status da Sequência */}
          <div style={{
            background: 'rgba(0, 0, 0, 0.5)',
            padding: '15px',
            borderRadius: '10px',
            marginBottom: '20px',
            border: '1px solid #00ffff'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
              <span>Status: <strong style={{ color: getStatusColor(orquestracao.status) }}>{orquestracao.status}</strong></span>
              <span>Progresso: <strong>{orquestracao.progresso.toFixed(1)}%</strong></span>
            </div>
            <div style={{
              width: '100%',
              height: '10px',
              background: '#333',
              borderRadius: '5px',
              overflow: 'hidden'
            }}>
              <div style={{
                width: `${orquestracao.progresso}%`,
                height: '100%',
                background: 'linear-gradient(90deg, #00ffff, #ff00ff)',
                transition: 'width 0.3s ease'
              }}></div>
            </div>
            {orquestracao.moduloAtual && (
              <div style={{ marginTop: '10px', color: '#ffff00' }}>
                Módulo Atual: <strong>{orquestracao.moduloAtual}</strong>
              </div>
            )}
          </div>

          {/* Botão de Início */}
          <button
            onClick={iniciarSequenciaSagrada}
            disabled={orquestracao.status === 'EM_EXECUCAO'}
            style={{
              background: orquestracao.status === 'EM_EXECUCAO' 
                ? 'linear-gradient(45deg, #666, #888)'
                : 'linear-gradient(45deg, #00ffff, #ff00ff)',
              color: '#000',
              border: 'none',
              padding: '12px 24px',
              borderRadius: '8px',
              fontSize: '1.1em',
              fontWeight: 'bold',
              cursor: orquestracao.status === 'EM_EXECUCAO' ? 'not-allowed' : 'pointer',
              marginBottom: '20px',
              textShadow: '0 0 10px #ffffff'
            }}
          >
            {orquestracao.status === 'EM_EXECUCAO' ? '🔄 EXECUTANDO...' : '🚀 INICIAR SEQUÊNCIA SAGRADA'}
          </button>

          {/* Logs em Tempo Real */}
          <div style={{
            flex: 1,
            background: 'rgba(0, 0, 0, 0.5)',
            borderRadius: '10px',
            padding: '15px',
            overflowY: 'auto',
            border: '1px solid #333'
          }}>
            <h4 style={{ color: '#00ffff', marginBottom: '10px' }}>📜 LOGS DA ORQUESTRAÇÃO</h4>
            {orquestracao.logs.map((log, index) => (
              <div key={index} style={{
                padding: '8px',
                marginBottom: '5px',
                background: 'rgba(255, 255, 255, 0.05)',
                borderRadius: '5px',
                fontSize: '0.9em',
                borderLeft: '3px solid #00ffff'
              }}>
                {log}
              </div>
            ))}
          </div>
        </div>

        {/* Painel Direito - Frequências e Status */}
        <div style={{
          background: 'rgba(0, 0, 0, 0.7)',
          borderRadius: '15px',
          padding: '20px',
          border: '1px solid #333',
          overflowY: 'auto'
        }}>
          <h3 style={{ color: '#00ffff', marginBottom: '15px' }}>📊 FREQUÊNCIAS QUÂNTICAS</h3>
          
          {quantumFrequencies.map(freq => (
            <div key={freq.nome} style={{
              background: 'rgba(255, 255, 255, 0.05)',
              padding: '10px',
              marginBottom: '10px',
              borderRadius: '8px',
              borderLeft: `4px solid ${freq.cor}`
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                <strong style={{ color: freq.cor }}>{freq.nome}</strong>
                <span>{freq.valor}Hz</span>
              </div>
              <div style={{ fontSize: '0.8em', color: '#cccccc' }}>{freq.descricao}</div>
            </div>
          ))}

          <div style={{ marginTop: '20px', paddingTop: '20px', borderTop: '1px solid #333' }}>
            <h4 style={{ color: '#00ffff', marginBottom: '10px' }}>🌐 STATUS GLOBAL</h4>
            <div style={{ fontSize: '0.9em' }}>
              <div>Módulos Conectados: <strong style={{ color: '#00ff00' }}>{modules.filter(m => m.status === 'CONECTADO').length}</strong></div>
              <div>Em Alerta: <strong style={{ color: '#ffff00' }}>{modules.filter(m => m.status === 'ALERTA').length}</strong></div>
              <div>Críticos: <strong style={{ color: '#ff0000' }}>{modules.filter(m => m.status === 'CRÍTICO').length}</strong></div>
            </div>
          </div>
        </div>

      </div>

      {/* Efeitos Visuais */}
      <style jsx>{`
        @keyframes pulse {
          0% { opacity: 0.3; }
          100% { opacity: 0.7; }
        }
      `}</style>
    </div>
  )
}
