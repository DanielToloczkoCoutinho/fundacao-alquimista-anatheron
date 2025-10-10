#!/bin/bash

echo "🔄 RESTAURANDO PÁGINAS DINÂMICAS COMPLETAS"
echo "=========================================="

# 1. Restaurar Portal Central dinâmico completo
echo "🔮 Restaurando Portal Central dinâmico..."
cat > app/central/page.js << 'CENTRAL_DINAMICO'
"use client"

import { useState, useEffect } from 'react'

export default function PortalCentral() {
  const [modulos, setModulos] = useState([])
  const [metricas, setMetricas] = useState(null)
  const [tempoAtivo, setTempoAtivo] = useState(0)

  useEffect(() => {
    // Inicializar módulos
    setModulos([
      { id: 1, nome: "Módulo 303", path: "/modulo-303", status: "operacional", cor: "purple" },
      { id: 2, nome: "Sistema Vivo", path: "/sistema-vivo", status: "operacional", cor: "green" },
      { id: 3, nome: "Metadados Reais", path: "/metadados-reais", status: "operacional", cor: "blue" },
      { id: 4, nome: "Status", path: "/status", status: "operacional", cor: "yellow" },
      { id: 5, nome: "Árvore da Vida", path: "/arvore-da-vida", status: "operacional", cor: "pink" },
      { id: 6, nome: "Revelação Real", path: "/revelacao-real", status: "operacional", cor: "red" }
    ])

    // Timer do sistema
    const timer = setInterval(() => {
      setTempoAtivo(prev => prev + 1)
    }, 1000)

    // Buscar métricas
    fetch('/api/metrics')
      .then(res => res.json())
      .then(data => setMetricas(data))

    return () => clearInterval(timer)
  }, [])

  const getBorderColor = (cor) => {
    switch(cor) {
      case 'purple': return 'border-purple-500'
      case 'green': return 'border-green-500' 
      case 'blue': return 'border-blue-500'
      case 'yellow': return 'border-yellow-500'
      case 'pink': return 'border-pink-500'
      case 'red': return 'border-red-500'
      default: return 'border-gray-500'
    }
  }

  const getBgColor = (cor) => {
    switch(cor) {
      case 'purple': return 'bg-purple-600'
      case 'green': return 'bg-green-600'
      case 'blue': return 'bg-blue-600'
      case 'yellow': return 'bg-yellow-600'
      case 'pink': return 'bg-pink-600'
      case 'red': return 'bg-red-600'
      default: return 'bg-gray-600'
    }
  }

  const getTextColor = (cor) => {
    switch(cor) {
      case 'purple': return 'text-purple-400'
      case 'green': return 'text-green-400'
      case 'blue': return 'text-blue-400'
      case 'yellow': return 'text-yellow-400'
      case 'pink': return 'text-pink-400'
      case 'red': return 'text-red-400'
      default: return 'text-gray-400'
    }
  }

  return (
    <div className="min-h-screen bg-black text-white p-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold mb-2 text-center">🌌 PORTAL CENTRAL</h1>
        <h2 className="text-xl mb-8 text-center text-gray-400">
          Nexus Unificado da Fundação Alquimista
          <br />
          <span className="text-sm text-green-400">🔄 SISTEMA ATIVO: {tempoAtivo}s</span>
        </h2>

        {/* Status do Sistema */}
        {metricas && (
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
            <div className="bg-gray-900 p-4 rounded text-center border border-green-500">
              <div className="text-2xl font-bold text-green-400">{metricas.circuitos_quantico}</div>
              <div className="text-sm text-gray-400">Circuitos</div>
            </div>
            <div className="bg-gray-900 p-4 rounded text-center border border-blue-500">
              <div className="text-2xl font-bold text-blue-400">{metricas.coerencia.toFixed(1)}%</div>
              <div className="text-sm text-gray-400">Coerência</div>
            </div>
            <div className="bg-gray-900 p-4 rounded text-center border border-purple-500">
              <div className="text-2xl font-bold text-purple-400">{modulos.length}</div>
              <div className="text-sm text-gray-400">Módulos</div>
            </div>
            <div className="bg-gray-900 p-4 rounded text-center border border-yellow-500">
              <div className="text-2xl font-bold text-yellow-400">100%</div>
              <div className="text-sm text-gray-400">Operacional</div>
            </div>
          </div>
        )}

        {/* Grid de Módulos Interativos */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          {modulos.map(modulo => (
            <div 
              key={modulo.id}
              className={`bg-gray-900 p-6 rounded-lg border ${getBorderColor(modulo.cor)} hover:opacity-80 transition-all cursor-pointer`}
              onClick={() => window.location.href = modulo.path}
            >
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-xl font-semibold">{modulo.nome}</h3>
                <span className={`${getTextColor(modulo.cor)} text-sm`}>
                  {modulo.status === 'operacional' ? '✅' : '⚡'} {modulo.status.toUpperCase()}
                </span>
              </div>
              <p className="text-gray-400 mb-4">Acesse o sistema {modulo.nome.toLowerCase()}</p>
              <a 
                href={modulo.path}
                className={`${getBgColor(modulo.cor)} hover:opacity-90 px-4 py-2 rounded text-white block text-center`}
              >
                🌟 ACESSAR
              </a>
            </div>
          ))}
        </div>

        {/* Sistema de Ativação */}
        <div className="bg-gray-900 p-6 rounded-lg border border-purple-500 text-center">
          <h3 className="text-xl font-semibold mb-4">🎛️ CONTROLE CENTRAL</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <button 
              onClick={() => window.location.reload()}
              className="bg-blue-600 hover:bg-blue-700 p-3 rounded text-white"
            >
              🔄 Atualizar Sistema
            </button>
            <button 
              onClick={() => fetch('/api/health').then(r => r.json()).then(data => console.log('Health:', data))}
              className="bg-green-600 hover:bg-green-700 p-3 rounded text-white"
            >
              📊 Verificar Saúde
            </button>
            <button 
              onClick={() => setTempoAtivo(0)}
              className="bg-red-600 hover:bg-red-700 p-3 rounded text-white"
            >
              ⏰ Reiniciar Timer
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
CENTRAL_DINAMICO

echo "✅ Portal Central dinâmico restaurado"

# 2. Deploy final com todas as dinâmicas
echo ""
echo "🚀 DEPLOY FINAL COM TODAS AS DINÂMICAS..."
npm run build && npx vercel --prod --force

