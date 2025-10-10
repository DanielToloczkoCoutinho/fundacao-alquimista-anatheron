"use client"

import { useState, useEffect } from 'react'

export default function SistemaVivo() {
  const [dados, setDados] = useState(null)
  const [logs, setLogs] = useState([])
  const [pulsacao, setPulsacao] = useState(0)

  useEffect(() => {
    console.log('🌌 Sistema Vivo - Iniciando monitoramento...')
    
    // Pulsação do sistema
    const pulseInterval = setInterval(() => {
      setPulsacao(prev => (prev + 1) % 100)
    }, 500)

    // Dados iniciais
    setDados({
      circuitos: 1331,
      coerencia: 97.5,
      temperatura: 0.00256,
      planetas: 5,
      dimensoes: 12
    })

    // Logs de atividade
    const logInterval = setInterval(() => {
      const atividades = [
        "Sistema quântico estável",
        "Circuitos otimizados", 
        "Monitoramento planetário ativo",
        "Proteção dimensional reforçada",
        "Zennith Rainha conectada",
        "Matriz Lux.net sincronizada"
      ]
      
      setLogs(prev => [{
        id: Date.now(),
        timestamp: new Date().toLocaleTimeString(),
        mensagem: atividades[Math.floor(Math.random() * atividades.length)],
        tipo: ["info", "success", "warning"][Math.floor(Math.random() * 3)]
      }, ...prev.slice(0, 15)])
    }, 3000)

    return () => {
      clearInterval(pulseInterval)
      clearInterval(logInterval)
    }
  }, [])

  if (!dados) {
    return (
      <div className="min-h-screen bg-black text-white p-8">
        <div className="max-w-6xl mx-auto text-center">
          <h1 className="text-4xl font-bold mb-4">🌌 SISTEMA VIVO</h1>
          <div className="text-2xl text-green-400 animate-pulse">💓 INICIANDO PULSAÇÃO...</div>
        </div>
      </div>
    )
  }

  const getCorPorTipo = (tipo) => {
    switch(tipo) {
      case 'success': return 'text-green-400'
      case 'warning': return 'text-yellow-400'
      default: return 'text-blue-400'
    }
  }

  return (
    <div className="min-h-screen bg-black text-white p-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold mb-2 text-center">🌌 SISTEMA VIVO</h1>
        <h2 className="text-xl mb-8 text-center text-gray-400">
          Dashboard em Tempo Real 
          <span className="ml-4 text-green-400">💓 Pulsação: {pulsacao}%</span>
        </h2>
        
        {/* Métricas Principais com Pulsação */}
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4 mb-8">
          <div className="bg-gray-900 p-4 rounded-lg border border-purple-500 text-center">
            <div className="text-2xl font-bold text-purple-400">{dados.circuitos}</div>
            <div className="text-sm text-gray-400">Circuitos</div>
          </div>
          <div className="bg-gray-900 p-4 rounded-lg border border-green-500 text-center">
            <div className="text-2xl font-bold text-green-400">{dados.coerencia.toFixed(1)}%</div>
            <div className="text-sm text-gray-400">Coerência</div>
          </div>
          <div className="bg-gray-900 p-4 rounded-lg border border-blue-500 text-center">
            <div className="text-2xl font-bold text-blue-400">{dados.temperatura.toFixed(5)}K</div>
            <div className="text-sm text-gray-400">Temperatura</div>
          </div>
          <div className="bg-gray-900 p-4 rounded-lg border border-yellow-500 text-center">
            <div className="text-2xl font-bold text-yellow-400">{dados.planetas}</div>
            <div className="text-sm text-gray-400">Planetas</div>
          </div>
          <div className="bg-gray-900 p-4 rounded-lg border border-red-500 text-center">
            <div className="text-2xl font-bold text-red-400">{dados.dimensoes}</div>
            <div className="text-sm text-gray-400">Dimensões</div>
          </div>
          <div className="bg-gray-900 p-4 rounded-lg border border-pink-500 text-center">
            <div className="text-2xl font-bold text-pink-400">100%</div>
            <div className="text-sm text-gray-400">Operacional</div>
          </div>
        </div>

        {/* Logs de Atividade */}
        <div className="bg-gray-900 rounded-lg border border-gray-700 mb-8">
          <div className="p-4 border-b border-gray-700">
            <h3 className="text-xl font-semibold">📊 ATIVIDADE DO SISTEMA - TEMPO REAL</h3>
          </div>
          <div className="h-96 overflow-y-auto p-4">
            {logs.map(log => (
              <div key={log.id} className="flex items-center gap-4 py-2 border-b border-gray-800">
                <div className="text-sm text-gray-400 min-w-16">{log.timestamp}</div>
                <div className={`text-sm font-mono ${getCorPorTipo(log.tipo)} flex-1`}>
                  {log.mensagem}
                </div>
                <div>
                  {log.tipo === 'success' && '✅'}
                  {log.tipo === 'warning' && '⚠️'}
                  {log.tipo === 'info' && '🔵'}
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="text-center">
          <a href="/central" className="text-blue-400 hover:text-blue-300 text-lg">
            ← Voltar ao Portal Central
          </a>
        </div>
      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
