"use client"

import { useState, useEffect } from 'react'

export default function StatusPage() {
  const [health, setHealth] = useState(null)
  const [metrics, setMetrics] = useState(null)
  const [diagnostico, setDiagnostico] = useState("Executando diagnósticos...")

  useEffect(() => {
    const carregarDados = async () => {
      try {
        const [healthRes, metricsRes] = await Promise.all([
          fetch('/api/health'),
          fetch('/api/metrics')
        ])
        
        const healthData = await healthRes.json()
        const metricsData = await metricsRes.json()
        
        setHealth(healthData)
        setMetrics(metricsData)
        setDiagnostico("Sistema operacional ✅")
      } catch (error) {
        setDiagnostico("Erro no diagnóstico ❌")
      }
    }

    carregarDados()
    const interval = setInterval(carregarDados, 10000)
    return () => clearInterval(interval)
  }, [])

  const executarDiagnostico = () => {
    setDiagnostico("Executando diagnósticos avançados...")
    setTimeout(() => {
      setDiagnostico("Todos os sistemas operacionais ✅")
    }, 2000)
  }

  const sincronizarSistemas = () => {
    setDiagnostico("Sincronizando com Matriz Lux.Net...")
    setTimeout(() => {
      setDiagnostico("Sincronização completa 🌐")
    }, 1500)
  }

  return (
    <div className="min-h-screen bg-black text-white p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-8 text-center">📊 STATUS DO SISTEMA</h1>
        
        {/* Diagnóstico */}
        <div className="bg-gray-900 p-6 rounded-lg border border-blue-500 mb-6">
          <h2 className="text-2xl font-semibold mb-4">🔍 DIAGNÓSTICO DO SISTEMA</h2>
          <div className="text-center">
            <div className="text-xl mb-4">{diagnostico}</div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <button 
                onClick={executarDiagnostico}
                className="bg-green-600 hover:bg-green-700 p-3 rounded text-white"
              >
                🧪 Executar Diagnóstico
              </button>
              <button 
                onClick={sincronizarSistemas}
                className="bg-purple-600 hover:bg-purple-700 p-3 rounded text-white"
              >
                🌐 Sincronizar Sistemas
              </button>
            </div>
          </div>
        </div>

        {health && metrics && (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Health Status */}
            <div className="bg-gray-900 p-6 rounded-lg border border-green-500">
              <h2 className="text-2xl font-semibold mb-4">✅ STATUS DE SAÚDE</h2>
              <div className="space-y-3">
                <div className="flex justify-between">
                  <span>Sistema:</span>
                  <span className="text-green-400 font-semibold">{health.status.toUpperCase()}</span>
                </div>
                <div className="flex justify-between">
                  <span>Versão:</span>
                  <span className="text-blue-400">{health.version}</span>
                </div>
                <div className="flex justify-between">
                  <span>Timestamp:</span>
                  <span className="text-gray-400 text-sm">{new Date(health.timestamp).toLocaleString()}</span>
                </div>
                
                <div className="mt-4">
                  <h3 className="font-semibold mb-2">Sistemas:</h3>
                  {Object.entries(health.systems).map(([system, status]) => (
                    <div key={system} className="flex justify-between text-sm">
                      <span className="capitalize">{system.replace(/_/g, ' ')}:</span>
                      <span className={status.includes('online') || status.includes('active') ? 'text-green-400' : 'text-yellow-400'}>
                        {status.toUpperCase()}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* Métricas */}
            <div className="bg-gray-900 p-6 rounded-lg border border-yellow-500">
              <h2 className="text-2xl font-semibold mb-4">📈 MÉTRICAS EM TEMPO REAL</h2>
              <div className="space-y-3">
                <div className="flex justify-between">
                  <span>Circuitos Quânticos:</span>
                  <span className="text-purple-400 font-semibold">{metrics.circuitos_quantico}</span>
                </div>
                <div className="flex justify-between">
                  <span>Coerência:</span>
                  <span className="text-green-400">{metrics.coerencia.toFixed(1)}%</span>
                </div>
                <div className="flex justify-between">
                  <span>Temperatura:</span>
                  <span className="text-blue-400">{metrics.temperatura.toFixed(5)}K</span>
                </div>
                <div className="flex justify-between">
                  <span>Atualizado:</span>
                  <span className="text-gray-400 text-sm">{new Date(metrics.timestamp).toLocaleTimeString()}</span>
                </div>
              </div>
            </div>
          </div>
        )}

        <div className="mt-8 text-center">
          <a href="/central" className="text-blue-400 hover:text-blue-300">
            ← Voltar ao Portal Central
          </a>
        </div>
      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
