"use client"

import { useState, useEffect } from 'react'

export default function PortalCentral() {
  const [tempoAtivo, setTempoAtivo] = useState(0)
  const [metricas, setMetricas] = useState(null)
  const [logs, setLogs] = useState([])
  const [coerenciaQuantica, setCoerenciaQuantica] = useState(95.5)
  const [modulosAtivos, setModulosAtivos] = useState([])

  // Efeito principal - núcleo dinâmico
  useEffect(() => {
    console.log('🌌 Portal Central - Sistema interdimensional online...')
    
    // Timer principal
    const timer = setInterval(() => {
      setTempoAtivo(prev => prev + 1)
    }, 1000)

    // Atualização de coerência quântica
    const coerenciaInterval = setInterval(() => {
      setCoerenciaQuantica(prev => Math.max(85, Math.min(99.9, prev + (Math.random() - 0.5))))
    }, 2000)

    // Buscar métricas da API
    const fetchMetrics = async () => {
      try {
        const response = await fetch('/api/metrics')
        const data = await response.json()
        setMetricas(data)
        adicionarLog(`Métricas sincronizadas - Circuitos: ${data.circuitos}`, 'success')
      } catch (error) {
        adicionarLog('Erro na sincronização métricas', 'error')
      }
    }

    // Logs automáticos do sistema
    const logInterval = setInterval(() => {
      const mensagens = [
        { msg: "Sistema quântico estável", tipo: "info" },
        { msg: "Monitoramento 12D ativo", tipo: "success" },
        { msg: "Conexões Zennith operacionais", tipo: "info" },
        { msg: "Proteção Lux.Net ativa", tipo: "success" },
        { msg: "Frequência 777Hz mantida", tipo: "info" },
        { msg: "Escaneamento dimensional em progresso", tipo: "warning" }
      ]
      const mensagem = mensagens[Math.floor(Math.random() * mensagens.length)]
      adicionarLog(mensagem.msg, mensagem.tipo)
    }, 4000)

    fetchMetrics()
    const metricsInterval = setInterval(fetchMetrics, 8000)

    return () => {
      clearInterval(timer)
      clearInterval(coerenciaInterval)
      clearInterval(logInterval)
      clearInterval(metricsInterval)
    }
  }, [])

  const adicionarLog = (mensagem, tipo = 'info') => {
    setLogs(prev => [{
      id: Date.now(),
      timestamp: new Date().toLocaleTimeString(),
      mensagem,
      tipo
    }, ...prev.slice(0, 8)])
  }

  const ativarModulo = (moduloNome) => {
    if (!modulosAtivos.includes(moduloNome)) {
      setModulosAtivos(prev => [...prev, moduloNome])
      adicionarLog(`Módulo ${moduloNome} ativado`, 'success')
    }
  }

  const modulos = [
    { 
      nome: "M15", 
      path: "#", 
      cor: "purple", 
      desc: "Proteção Planetária",
      frequencia: "333Hz"
    },
    { 
      nome: "M303", 
      path: "/modulo-303", 
      cor: "green", 
      desc: "Realidade Quântica",
      frequencia: "777Hz"
    },
    { 
      nome: "M29", 
      path: "#", 
      cor: "blue", 
      desc: "Governança Zennith", 
      frequencia: "555Hz"
    },
    { 
      nome: "Sistema Vivo", 
      path: "/sistema-vivo", 
      cor: "yellow", 
      desc: "Dashboard Tempo Real",
      frequencia: "888Hz"
    },
    { 
      nome: "Status", 
      path: "/status", 
      cor: "pink", 
      desc: "Diagnóstico Completo",
      frequencia: "222Hz"
    },
    { 
      nome: "Lux.Net", 
      path: "#", 
      cor: "red", 
      desc: "Matriz Central",
      frequencia: "999Hz"
    }
  ]

  const getCores = (cor) => {
    const cores = {
      purple: { border: 'border-purple-500', bg: 'bg-purple-600', text: 'text-purple-400' },
      green: { border: 'border-green-500', bg: 'bg-green-600', text: 'text-green-400' },
      blue: { border: 'border-blue-500', bg: 'bg-blue-600', text: 'text-blue-400' },
      yellow: { border: 'border-yellow-500', bg: 'bg-yellow-600', text: 'text-yellow-400' },
      pink: { border: 'border-pink-500', bg: 'bg-pink-600', text: 'text-pink-400' },
      red: { border: 'border-red-500', bg: 'bg-red-600', text: 'text-red-400' }
    }
    return cores[cor] || cores.purple
  }

  return (
    <div className="min-h-screen bg-black text-white p-6">
      <div className="max-w-7xl mx-auto">
        {/* Cabeçalho com Status em Tempo Real */}
        <div className="text-center mb-8">
          <h1 className="text-5xl font-bold mb-2 bg-gradient-to-r from-purple-400 to-blue-400 bg-clip-text text-transparent">
            🌌 PORTAL CENTRAL
          </h1>
          <p className="text-xl text-gray-400 mb-4">Nexus de Comando Interdimensional</p>
          
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
            <div className="bg-gray-900 p-4 rounded-lg border border-green-500 text-center">
              <div className="text-2xl font-bold text-green-400 animate-pulse">{tempoAtivo}s</div>
              <div className="text-sm text-gray-400">Tempo Ativo</div>
            </div>
            <div className="bg-gray-900 p-4 rounded-lg border border-blue-500 text-center">
              <div className="text-2xl font-bold text-blue-400">
                {metricas ? metricas.circuitos : '1331'}
              </div>
              <div className="text-sm text-gray-400">Circuitos</div>
            </div>
            <div className="bg-gray-900 p-4 rounded-lg border border-purple-500 text-center">
              <div className="text-2xl font-bold text-purple-400">{coerenciaQuantica.toFixed(1)}%</div>
              <div className="text-sm text-gray-400">Coerência Quântica</div>
            </div>
            <div className="bg-gray-900 p-4 rounded-lg border border-yellow-500 text-center">
              <div className="text-2xl font-bold text-yellow-400">{modulosAtivos.length}/6</div>
              <div className="text-sm text-gray-400">Módulos Ativos</div>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Painel de Módulos */}
          <div className="lg:col-span-2">
            <h2 className="text-2xl font-bold mb-4 text-center">🎛️ PAINEL DE CONTROLE</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {modulos.map((modulo, index) => {
                const cores = getCores(modulo.cor)
                const estaAtivo = modulosAtivos.includes(modulo.nome)
                
                return (
                  <div 
                    key={index}
                    className={`bg-gray-900 p-5 rounded-xl border-2 ${cores.border} hover:scale-105 transition-all duration-300 cursor-pointer ${
                      estaAtivo ? 'ring-2 ring-white ring-opacity-50' : ''
                    }`}
                    onClick={() => ativarModulo(modulo.nome)}
                  >
                    <div className="flex justify-between items-start mb-3">
                      <div>
                        <h3 className="text-xl font-bold">{modulo.nome}</h3>
                        <p className="text-gray-400 text-sm">{modulo.desc}</p>
                      </div>
                      <span className={`text-sm px-2 py-1 rounded ${estaAtivo ? 'bg-green-500 text-white' : 'bg-gray-700 text-gray-300'}`}>
                        {estaAtivo ? '✅ ATIVO' : '⚡ ATIVAR'}
                      </span>
                    </div>
                    
                    <div className="flex justify-between items-center text-sm">
                      <span className="text-gray-400">Frequência:</span>
                      <span className={cores.text}>{modulo.frequencia}</span>
                    </div>
                    
                    {modulo.path !== '#' && (
                      <a 
                        href={modulo.path}
                        className={`mt-3 ${cores.bg} hover:opacity-90 px-4 py-2 rounded text-white block text-center text-sm font-semibold transition-opacity`}
                        onClick={(e) => e.stopPropagation()}
                      >
                        🌟 ACESSAR SISTEMA
                      </a>
                    )}
                  </div>
                )
              })}
            </div>
          </div>

          {/* Painel Lateral - Logs e Coerência */}
          <div className="space-y-6">
            {/* Indicador de Coerência Quântica */}
            <div className="bg-gray-900 p-5 rounded-xl border border-purple-500">
              <h3 className="text-lg font-bold mb-3 text-purple-400">�� COERÊNCIA QUÂNTICA</h3>
              <div className="space-y-2">
                <div className="flex justify-between text-sm">
                  <span>Estado Atual:</span>
                  <span className={coerenciaQuantica > 95 ? 'text-green-400' : 'text-yellow-400'}>
                    {coerenciaQuantica > 95 ? 'ÓTIMO' : 'ESTÁVEL'}
                  </span>
                </div>
                <div className="w-full bg-gray-700 rounded-full h-2">
                  <div 
                    className="bg-gradient-to-r from-green-400 to-purple-400 h-2 rounded-full transition-all duration-1000"
                    style={{ width: `${coerenciaQuantica}%` }}
                  ></div>
                </div>
                <div className="text-xs text-gray-400 text-center">
                  {coerenciaQuantica.toFixed(1)}% de estabilidade
                </div>
              </div>
            </div>

            {/* Logs do Sistema */}
            <div className="bg-gray-900 p-5 rounded-xl border border-blue-500">
              <h3 className="text-lg font-bold mb-3 text-blue-400">📝 LOGS VIBRACIONAIS</h3>
              <div className="h-64 overflow-y-auto bg-black rounded-lg p-3">
                {logs.map(log => (
                  <div key={log.id} className="text-sm mb-2 flex items-start">
                    <span className="text-gray-400 text-xs min-w-14">[{log.timestamp}]</span>
                    <span className={
                      log.tipo === 'success' ? 'text-green-400 ml-2' :
                      log.tipo === 'error' ? 'text-red-400 ml-2' :
                      log.tipo === 'warning' ? 'text-yellow-400 ml-2' : 'text-blue-400 ml-2'
                    }>
                      {log.mensagem}
                    </span>
                  </div>
                ))}
                {logs.length === 0 && (
                  <div className="text-gray-500 text-center py-8">Sistema inicializando...</div>
                )}
              </div>
            </div>
          </div>
        </div>

        {/* Barra de Status Inferior */}
        <div className="mt-8 bg-gray-900 rounded-lg p-4 border border-gray-700">
          <div className="flex flex-wrap justify-between items-center text-sm">
            <div className="flex items-center space-x-4">
              <span className="text-green-400">● SISTEMA OPERACIONAL</span>
              <span className="text-gray-400">|</span>
              <span>Módulos: {modulos.length}</span>
              <span className="text-gray-400">|</span>
              <span>Tempo: {tempoAtivo}s</span>
            </div>
            <div className="text-gray-400">
              Fundação Alquimista © 2025 - Nexus Central
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
