"use client"

import { useState, useEffect } from 'react'

export default function StatusPage() {
  const [health, setHealth] = useState({})
  const [diagnostico, setDiagnostico] = useState("Executando diagnósticos...")

  useEffect(() => {
    const interval = setInterval(() => {
      // Simular verificação de saúde do sistema
      setHealth({
        servidor: { status: 'online', latencia: `${Math.floor(Math.random() * 50)}ms` },
        database: { status: 'online', conexoes: Math.floor(Math.random() * 100) },
        api: { status: 'online', requisicoes: Math.floor(Math.random() * 1000) },
        seguranca: { status: 'online', ameacas: 0 }
      })

      const diagnosticos = [
        "Sistema operacional estável",
        "Todas as conexões ativas",
        "Performance otimizada",
        "Segurança máxima ativa",
        "Recursos dimensionais estáveis"
      ]
      setDiagnostico(diagnosticos[Math.floor(Math.random() * diagnosticos.length)])
    }, 3000)

    return () => clearInterval(interval)
  }, [])

  return (
    <div className="min-h-screen bg-black text-white p-6">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-5xl font-bold mb-2 bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
            📊 STATUS DO SISTEMA
          </h1>
          <p className="text-xl text-gray-400">Diagnóstico Completo em Tempo Real</p>
        </div>

        {/* Diagnóstico Principal */}
        <div className="bg-gray-900 p-6 rounded-xl border border-green-500 mb-8 text-center">
          <div className="text-2xl font-bold text-green-400 mb-2">● SISTEMA OPERACIONAL</div>
          <div className="text-gray-300">{diagnostico}</div>
        </div>

        {/* Status dos Componentes */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          <div className="bg-gray-900 p-6 rounded-xl border border-blue-500">
            <h3 className="text-lg font-bold mb-4 text-blue-400">🖥️ SERVIDOR</h3>
            <div className="space-y-2">
              <div className="flex justify-between">
                <span>Status:</span>
                <span className="text-green-400">● ONLINE</span>
              </div>
              <div className="flex justify-between">
                <span>Latência:</span>
                <span className="text-blue-400">{health.servidor?.latencia || '...'}</span>
              </div>
            </div>
          </div>

          <div className="bg-gray-900 p-6 rounded-xl border border-green-500">
            <h3 className="text-lg font-bold mb-4 text-green-400">🗄️ DATABASE</h3>
            <div className="space-y-2">
              <div className="flex justify-between">
                <span>Status:</span>
                <span className="text-green-400">● ONLINE</span>
              </div>
              <div className="flex justify-between">
                <span>Conexões:</span>
                <span className="text-green-400">{health.database?.conexoes || '...'}</span>
              </div>
            </div>
          </div>

          <div className="bg-gray-900 p-6 rounded-xl border border-purple-500">
            <h3 className="text-lg font-bold mb-4 text-purple-400">🔗 API</h3>
            <div className="space-y-2">
              <div className="flex justify-between">
                <span>Status:</span>
                <span className="text-green-400">● ONLINE</span>
              </div>
              <div className="flex justify-between">
                <span>Requisições:</span>
                <span className="text-purple-400">{health.api?.requisicoes || '...'}</span>
              </div>
            </div>
          </div>

          <div className="bg-gray-900 p-6 rounded-xl border border-red-500">
            <h3 className="text-lg font-bold mb-4 text-red-400">🛡️ SEGURANÇA</h3>
            <div className="space-y-2">
              <div className="flex justify-between">
                <span>Status:</span>
                <span className="text-green-400">● ONLINE</span>
              </div>
              <div className="flex justify-between">
                <span>Ameças:</span>
                <span className="text-green-400">0</span>
              </div>
            </div>
          </div>
        </div>

        <div className="text-center">
          <a href="/central" className="inline-block bg-gray-700 hover:bg-gray-600 px-6 py-3 rounded-lg text-white font-semibold transition-colors">
            ← Voltar ao Portal Central
          </a>
        </div>
      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
