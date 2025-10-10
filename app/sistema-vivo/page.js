"use client"

import { useState, useEffect } from 'react'

export default function SistemaVivo() {
  const [dados, setDados] = useState({
    pulsacao: 77,
    frequencia: "432Hz",
    estabilidade: "98.5%",
    conexoes: 1331
  })
  const [logs, setLogs] = useState([])
  const [contador, setContador] = useState(0)

  useEffect(() => {
    const interval = setInterval(() => {
      setContador(prev => prev + 1)
      
      // Atualizar dados em tempo real
      setDados(prev => ({
        pulsacao: 75 + Math.floor(Math.random() * 6),
        frequencia: `${428 + Math.floor(Math.random() * 8)}Hz`,
        estabilidade: `${(97 + Math.random() * 3).toFixed(1)}%`,
        conexoes: 1331 + Math.floor(Math.random() * 10)
      }))

      // Adicionar logs
      if (contador % 3 === 0) {
        const mensagens = [
          "Sistema vital estável",
          "Pulsação cósmica normal",
          "Conexões dimensionais ativas",
          "Fluxo de energia constante",
          "Harmonia universal mantida"
        ]
        setLogs(prev => [{
          id: Date.now(),
          timestamp: new Date().toLocaleTimeString(),
          mensagem: mensagens[Math.floor(Math.random() * mensagens.length)],
          tipo: 'info'
        }, ...prev.slice(0, 6)])
      }
    }, 2000)

    return () => clearInterval(interval)
  }, [contador])

  return (
    <div className="min-h-screen bg-black text-white p-6">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-5xl font-bold mb-2 bg-gradient-to-r from-green-400 to-blue-400 bg-clip-text text-transparent">
            🌿 SISTEMA VIVO
          </h1>
          <p className="text-xl text-gray-400 mb-4">Dashboard de Monitoramento em Tempo Real</p>
          <div className="flex justify-center space-x-4 text-sm">
            <span className="text-green-400">● SISTEMA ATIVO</span>
            <span className="text-gray-400">|</span>
            <span className="text-blue-400">Ciclo: {contador}</span>
          </div>
        </div>

        {/* Métricas Principais */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          <div className="bg-gray-900 p-6 rounded-xl border border-green-500 text-center">
            <div className="text-3xl font-bold text-green-400 animate-pulse">{dados.pulsacao}</div>
            <div className="text-sm text-gray-400 mt-2">Pulsação Cósmica</div>
          </div>
          <div className="bg-gray-900 p-6 rounded-xl border border-blue-500 text-center">
            <div className="text-3xl font-bold text-blue-400">{dados.frequencia}</div>
            <div className="text-sm text-gray-400 mt-2">Frequência Base</div>
          </div>
          <div className="bg-gray-900 p-6 rounded-xl border border-purple-500 text-center">
            <div className="text-3xl font-bold text-purple-400">{dados.estabilidade}</div>
            <div className="text-sm text-gray-400 mt-2">Estabilidade</div>
          </div>
          <div className="bg-gray-900 p-6 rounded-xl border border-yellow-500 text-center">
            <div className="text-3xl font-bold text-yellow-400">{dados.conexoes}</div>
            <div className="text-sm text-gray-400 mt-2">Conexões Ativas</div>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Gráfico de Pulsação */}
          <div className="bg-gray-900 p-6 rounded-xl border border-green-500">
            <h3 className="text-xl font-bold mb-4 text-green-400">📈 PULSAÇÃO CÓSMICA</h3>
            <div className="h-64 bg-black rounded-lg p-4 flex items-end space-x-1">
              {Array.from({ length: 20 }).map((_, i) => (
                <div 
                  key={i}
                  className="flex-1 bg-green-500 rounded-t transition-all duration-500"
                  style={{ 
                    height: `${40 + Math.sin(i + contador * 0.5) * 30}%`,
                    opacity: 0.7 + Math.sin(i + contador * 0.3) * 0.3
                  }}
                ></div>
              ))}
            </div>
          </div>

          {/* Logs do Sistema */}
          <div className="bg-gray-900 p-6 rounded-xl border border-blue-500">
            <h3 className="text-xl font-bold mb-4 text-blue-400">📝 ATIVIDADE VITAL</h3>
            <div className="h-64 overflow-y-auto bg-black rounded-lg p-4">
              {logs.map(log => (
                <div key={log.id} className="text-sm mb-2 flex items-start">
                  <span className="text-gray-400 text-xs min-w-16">[{log.timestamp}]</span>
                  <span className="text-green-400 ml-2">{log.mensagem}</span>
                </div>
              ))}
              {logs.length === 0 && (
                <div className="text-gray-500 text-center py-12">
                  <div className="text-4xl mb-2">🌿</div>
                  <div>Monitorando atividade vital...</div>
                </div>
              )}
            </div>
          </div>
        </div>

        <div className="mt-8 text-center">
          <a href="/central" className="inline-block bg-gray-700 hover:bg-gray-600 px-6 py-3 rounded-lg text-white font-semibold transition-colors">
            ← Voltar ao Portal Central
          </a>
        </div>
      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
