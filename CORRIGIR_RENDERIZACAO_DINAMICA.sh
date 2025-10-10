#!/bin/bash

echo "🚨 CORRIGINDO RENDERIZAÇÃO ESTÁTICA PARA DINÂMICA"
echo "================================================"

# O problema é que Next.js está pré-renderizando como estático
# Precisamos forçar renderização dinâmica no lado do cliente

# 1. Corrigir Módulo 303 com export dinâmico
cat > app/modulo-303/page.js << 'MOD303_DYNAMIC'
"use client"

import { useState, useEffect } from 'react'

// Forçar componente totalmente dinâmico
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
  const [carregado, setCarregado] = useState(false)

  useEffect(() => {
    console.log('🎯 Módulo 303 - Cliente carregado, iniciando dinâmica...')
    setCarregado(true)
    
    const interval = setInterval(() => {
      setContador(prev => prev + 1)
      
      // Atualizações dinâmicas
      setDados(prev => ({
        ...prev,
        frequencia: `${(777 + Math.random() * 10).toFixed(1)} Hz`,
        coerencia: `${(95 + Math.random() * 3).toFixed(1)}%`,
        circuitos: 1331 + Math.floor(Math.random() * 10),
        temperatura: `${(0.00256 + Math.random() * 0.0001).toFixed(5)}K`
      }))

      // Logs dinâmicos
      const novoLog = {
        timestamp: new Date().toLocaleTimeString(),
        mensagem: `Sistema ativo - Ciclo ${contador + 1}`,
        tipo: ["info", "success", "warning"][Math.floor(Math.random() * 3)]
      }
      
      setLogs(prev => [novoLog, ...prev.slice(0, 8)])
      
    }, 3000)

    return () => {
      console.log('🧹 Limpando intervalos')
      clearInterval(interval)
    }
  }, [contador])

  // Se não carregou no cliente, mostrar loading
  if (!carregado) {
    return (
      <div className="min-h-screen bg-black text-white p-8">
        <div className="max-w-6xl mx-auto text-center">
          <h1 className="text-4xl font-bold mb-4">🔮 MÓDULO 303</h1>
          <div className="text-2xl text-yellow-400">🔄 Carregando sistema dinâmico...</div>
          <div className="text-sm text-gray-400 mt-4">Aguarde, o sistema começará em 3 segundos</div>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-black text-white p-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold mb-8 text-center">🔮 MÓDULO 303</h1>
        <h2 className="text-2xl mb-8 text-center text-purple-400">
          🌌 REALIDADE QUÂNTICA - SISTEMA 100% DINÂMICO
          <br />
          <span className="text-sm text-green-400">Atualizando... | Ciclo: {contador}</span>
        </h2>
        
        {/* Métricas em tempo real */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          <div className="bg-gray-900 p-6 rounded-lg border border-purple-500">
            <h3 className="text-lg font-semibold mb-2">🌀 Status</h3>
            <p className="text-2xl text-green-400">{dados.status}</p>
          </div>
          <div className="bg-gray-900 p-6 rounded-lg border border-blue-500">
            <h3 className="text-lg font-semibold mb-2">📡 Frequência</h3>
            <p className="text-2xl text-blue-400 animate-pulse">{dados.frequencia}</p>
          </div>
          <div className="bg-gray-900 p-6 rounded-lg border border-green-500">
            <h3 className="text-lg font-semibold mb-2">⚡ Coerência</h3>
            <p className="text-2xl text-green-400 animate-pulse">{dados.coerencia}</p>
          </div>
        </div>

        {/* Logs dinâmicos */}
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
              </div>
            ))}
          </div>
        </div>

        <div className="text-center">
          <a href="/central" className="text-blue-400 hover:text-blue-300">
            ← Voltar ao Portal Central
          </a>
        </div>
      </div>
    </div>
  )
}

// Forçar dynamic
export const dynamic = 'force-dynamic'
MOD303_DYNAMIC

echo "✅ Módulo 303 corrigido para dinâmico forçado"

# 2. Corrigir Sistema Vivo
cat > app/sistema-vivo/page.js << 'SISTEMAVIVO_DYNAMIC'
"use client"

import { useState, useEffect } from 'react'

export default function SistemaVivo() {
  const [metricas, setMetricas] = useState({
    circuitos: 1331,
    coerencia: 97.5,
    temperatura: 0.00256,
    atualizacao: new Date().toLocaleTimeString()
  })

  const [logs, setLogs] = useState([])
  const [carregado, setCarregado] = useState(false)

  useEffect(() => {
    console.log('🌌 Sistema Vivo - Iniciando dashboard dinâmico...')
    setCarregado(true)
    
    const interval = setInterval(() => {
      setMetricas(prev => ({
        circuitos: prev.circuitos + Math.floor(Math.random() * 3 - 1),
        coerencia: Math.max(95, Math.min(99, prev.coerencia + (Math.random() - 0.5))),
        temperatura: 0.00256 + (Math.random() * 0.0001 - 0.00005),
        atualizacao: new Date().toLocaleTimeString()
      }))

      const novoLog = {
        timestamp: new Date().toLocaleTimeString(),
        mensagem: ["Sistema ativo", "Dados atualizados", "Monitorando"][Math.floor(Math.random() * 3)],
        tipo: ["info", "success"][Math.floor(Math.random() * 2)]
      }
      
      setLogs(prev => [novoLog, ...prev.slice(0, 10)])
      
    }, 2000)

    return () => clearInterval(interval)
  }, [])

  if (!carregado) {
    return (
      <div className="min-h-screen bg-black text-white p-8">
        <div className="max-w-6xl mx-auto text-center">
          <h1 className="text-4xl font-bold mb-4">🌌 SISTEMA VIVO</h1>
          <div className="text-2xl text-yellow-400">🔄 Iniciando dashboard dinâmico...</div>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-black text-white p-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold mb-2 text-center">🌌 SISTEMA VIVO</h1>
        <h2 className="text-xl mb-8 text-center text-gray-400">
          Dashboard em Tempo Real - Atualizado: {metricas.atualizacao}
        </h2>
        
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          <div className="bg-gray-900 p-4 rounded-lg border border-purple-500 text-center">
            <div className="text-2xl font-bold text-purple-400 animate-pulse">{metricas.circuitos}</div>
            <div className="text-sm text-gray-400">Circuitos</div>
          </div>
          <div className="bg-gray-900 p-4 rounded-lg border border-green-500 text-center">
            <div className="text-2xl font-bold text-green-400 animate-pulse">{metricas.coerencia.toFixed(1)}%</div>
            <div className="text-sm text-gray-400">Coerência</div>
          </div>
          <div className="bg-gray-900 p-4 rounded-lg border border-blue-500 text-center">
            <div className="text-2xl font-bold text-blue-400 animate-pulse">{metricas.temperatura.toFixed(5)}K</div>
            <div className="text-sm text-gray-400">Temperatura</div>
          </div>
          <div className="bg-gray-900 p-4 rounded-lg border border-yellow-500 text-center">
            <div className="text-2xl font-bold text-yellow-400">100%</div>
            <div className="text-sm text-gray-400">Operacional</div>
          </div>
        </div>

        <div className="text-center">
          <a href="/central" className="text-blue-400 hover:text-blue-300">
            ← Voltar ao Portal Central
          </a>
        </div>
      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
SISTEMAVIVO_DYNAMIC

echo "✅ Sistema Vivo corrigido para dinâmico forçado"

# 3. Configurar Next.js para não pré-renderizar estático
echo "🔧 Configurando Next.js para renderização dinâmica..."

# Adicionar configuração para forçar dinâmico em desenvolvimento
cat > app/layout.js << 'LAYOUT_EOF'
export const dynamic = 'force-dynamic'

export const metadata = {
  title: 'Fundação Alquimista',
  description: 'Sistema Central da Fundação Alquimista Cósmica',
}

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  )
}
LAYOUT_EOF

echo "✅ Layout configurado para dinâmico"

# 4. Deploy das correções
echo "🚀 Deploy das correções dinâmicas..."
npm run build
npx vercel --prod --force

