#!/bin/bash

echo "🚀 RECRIANDO MÓDULO 303 COM CÓDIGO GARANTIDO"
echo "============================================"

# Criar diretório se não existir
mkdir -p app/modulo-303

# Recriar o arquivo com código 100% funcional
cat > app/modulo-303/page.js << 'MOD303_CORRETO'
"use client"

import { useState, useEffect } from 'react'

export default function Modulo303() {
  const [dados, setDados] = useState({
    status: "OPERACIONAL",
    frequencia: "777.0 Hz",
    coerencia: "95.5%",
    dimensoes: "12/12 Ativas",
    circuitos: 1331,
    temperatura: "0.00256K"
  })

  const [logs, setLogs] = useState([])
  const [contador, setContador] = useState(0)

  // Efeito PRINCIPAL para atualizações em tempo real
  useEffect(() => {
    console.log('🔮 Módulo 303 - Iniciando sistema dinâmico...')
    
    const interval = setInterval(() => {
      setContador(prev => prev + 1)
      
      // Atualizar dados dinamicamente
      setDados(prev => ({
        ...prev,
        frequencia: `${(777 + Math.random() * 10).toFixed(1)} Hz`,
        coerencia: `${(95 + Math.random() * 3).toFixed(1)}%`,
        circuitos: 1331 + Math.floor(Math.random() * 10),
        temperatura: `${(0.00256 + Math.random() * 0.0001).toFixed(5)}K`
      }))

      // Adicionar log dinâmico
      const tiposLog = ["info", "success", "warning"]
      const mensagens = [
        "Sistema quântico estável",
        "Circuitos otimizados", 
        "Coerência mantida",
        "Frequência ajustada",
        "Dimensões sincronizadas",
        "Temperatura controlada"
      ]
      
      const novoLog = {
        timestamp: new Date().toLocaleTimeString(),
        mensagem: `${mensagens[Math.floor(Math.random() * mensagens.length)]} - Ciclo ${contador + 1}`,
        tipo: tiposLog[Math.floor(Math.random() * tiposLog.length)]
      }
      
      setLogs(prev => [novoLog, ...prev.slice(0, 8)])
      
      console.log('🔄 Módulo 303 - Dados atualizados:', novoLog)
      
    }, 3000) // Atualiza a cada 3 segundos

    // Cleanup
    return () => {
      console.log('🧹 Módulo 303 - Limpando intervalos')
      clearInterval(interval)
    }
  }, [contador])

  return (
    <div className="min-h-screen bg-black text-white p-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold mb-8 text-center">🔮 MÓDULO 303</h1>
        <h2 className="text-2xl mb-8 text-center text-purple-400">
          🌌 REALIDADE QUÂNTICA - SISTEMA DINÂMICO
          <br />
          <span className="text-sm text-green-400">Atualizações a cada 3 segundos | Ciclo: {contador}</span>
        </h2>
        
        {/* Status em Tempo Real */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          <div className="bg-gray-900 p-6 rounded-lg border border-purple-500">
            <h3 className="text-lg font-semibold mb-2">🌀 Status</h3>
            <p className="text-2xl text-green-400">{dados.status}</p>
          </div>
          <div className="bg-gray-900 p-6 rounded-lg border border-blue-500">
            <h3 className="text-lg font-semibold mb-2">📡 Frequência</h3>
            <p className="text-2xl text-blue-400">{dados.frequencia}</p>
          </div>
          <div className="bg-gray-900 p-6 rounded-lg border border-green-500">
            <h3 className="text-lg font-semibold mb-2">⚡ Coerência</h3>
            <p className="text-2xl text-green-400">{dados.coerencia}</p>
          </div>
          <div className="bg-gray-900 p-6 rounded-lg border border-yellow-500">
            <h3 className="text-lg font-semibold mb-2">🌐 Dimensões</h3>
            <p className="text-2xl text-yellow-400">{dados.dimensoes}</p>
          </div>
          <div className="bg-gray-900 p-6 rounded-lg border border-red-500">
            <h3 className="text-lg font-semibold mb-2">⚡ Circuitos</h3>
            <p className="text-2xl text-red-400">{dados.circuitos.toLocaleString()}</p>
          </div>
          <div className="bg-gray-900 p-6 rounded-lg border border-pink-500">
            <h3 className="text-lg font-semibold mb-2">🌡️ Temperatura</h3>
            <p className="text-2xl text-pink-400">{dados.temperatura}</p>
          </div>
        </div>

        {/* Logs em Tempo Real */}
        <div className="bg-gray-900 p-6 rounded-lg border border-gray-700 mb-8">
          <h3 className="text-xl font-semibold mb-4">📊 LOGS EM TEMPO REAL</h3>
          <div className="h-64 overflow-y-auto bg-black p-4 rounded">
            {logs.map((log, index) => (
              <div key={index} className="text-sm font-mono mb-2 flex items-center">
                <span className="text-gray-400 min-w-20">[{log.timestamp}]</span>
                <span className={
                  log.tipo === 'success' ? 'text-green-400 ml-2' : 
                  log.tipo === 'warning' ? 'text-yellow-400 ml-2' : 'text-blue-400 ml-2'
                }>
                  {log.mensagem}
                </span>
                <span className="ml-2">
                  {log.tipo === 'success' && '✅'}
                  {log.tipo === 'warning' && '⚠️'}
                  {log.tipo === 'info' && '🔵'}
                </span>
              </div>
            ))}
            {logs.length === 0 && (
              <div className="text-gray-500 text-center py-8">
                Inicializando sistema quântico...
                <br />
                <span className="text-sm">Os logs começarão em 3 segundos</span>
              </div>
            )}
          </div>
        </div>

        {/* Controles do Sistema */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
          <button 
            onClick={() => {
              setContador(0)
              setLogs([])
              console.log('🔄 Módulo 303 - Reiniciado manualmente')
            }}
            className="bg-purple-600 hover:bg-purple-700 p-4 rounded-lg text-white font-semibold"
          >
            🔄 Reiniciar Sistema
          </button>
          <button 
            onClick={() => {
              const novoLog = {
                timestamp: new Date().toLocaleTimeString(),
                mensagem: "Ação manual executada",
                tipo: "success"
              }
              setLogs(prev => [novoLog, ...prev])
            }}
            className="bg-blue-600 hover:bg-blue-700 p-4 rounded-lg text-white font-semibold"
          >
            📝 Adicionar Log Manual
          </button>
          <button 
            onClick={() => {
              console.log('🔮 Estado atual:', { dados, logs, contador })
              alert('Verifique o console do navegador para debug')
            }}
            className="bg-green-600 hover:bg-green-700 p-4 rounded-lg text-white font-semibold"
          >
            🐛 Debug no Console
          </button>
        </div>

        <div className="mt-8 text-center">
          <a href="/central" className="text-blue-400 hover:text-blue-300 text-lg">
            ← Voltar ao Portal Central
          </a>
        </div>
      </div>
    </div>
  )
}
MOD303_CORRETO

echo "✅ Módulo 303 recriado com código garantido"
echo ""
echo "🔨 Recompilando..."
npm run build

echo ""
echo "🚀 Deploy da correção..."
npx vercel --prod --force

