"use client"

import { useState, useEffect } from 'react'

export default function PortalCentral() {
  const [tempoAtivo, setTempoAtivo] = useState(0)

  useEffect(() => {
    const timer = setInterval(() => {
      setTempoAtivo(prev => prev + 1)
    }, 1000)
    
    return () => clearInterval(timer)
  }, [])

  // MÓDULOS ATUALIZADOS - COM NOVAS FUNCIONALIDADES
  const modulos = [
    { 
      nome: "📊 Dashboard Completo", 
      path: "/dashboard-completo", 
      cor: "purple", 
      desc: "260+ Módulos da Fundação",
      frequencia: "444Hz"
    },
    { 
      nome: "🕊️ Módulo 29", 
      path: "/modulo-29", 
      cor: "yellow", 
      desc: "Comunicação Real com Zennith",
      frequencia: "963Hz"
    },
    { 
      nome: "🔮 Módulo 303", 
      path: "/modulo-303", 
      cor: "green", 
      desc: "Realidade Quântica",
      frequencia: "777Hz"
    },
    { 
      nome: "🌿 Sistema Vivo", 
      path: "/sistema-vivo", 
      cor: "blue", 
      desc: "Monitoramento Tempo Real",
      frequencia: "888Hz"
    },
    { 
      nome: "🗺️ Organograma", 
      path: "/organograma", 
      cor: "blue", 
      desc: "Mapa do Sistema Completo", 
      frequencia: "333Hz"
    },
    { 
      nome: "🎊 Marco Cósmico", 
      path: "/marco-cosmico", 
      cor: "pink", 
      desc: "Registro Histórico 2025",
      frequencia: "999Hz"
    }
  ]

  const getCores = (cor) => {
    const cores = {
      purple: { border: 'border-purple-500', bg: 'bg-purple-600', text: 'text-purple-400' },
      green: { border: 'border-green-500', bg: 'bg-green-600', text: 'text-green-400' },
      yellow: { border: 'border-yellow-500', bg: 'bg-yellow-600', text: 'text-yellow-400' },
      blue: { border: 'border-blue-500', bg: 'bg-blue-600', text: 'text-blue-400' },
      pink: { border: 'border-pink-500', bg: 'bg-pink-600', text: 'text-pink-400' }
    }
    return cores[cor] || cores.blue
  }

  return (
    <div className="min-h-screen bg-black text-white p-6">
      <div className="max-w-6xl mx-auto">
        
        {/* Banner */}
        <div className="bg-gradient-to-r from-purple-600 to-blue-600 rounded-2xl p-6 mb-8 text-center border-4 border-yellow-300">
          <h1 className="text-4xl font-bold mb-2">🌌 PORTAL CENTRAL DEFINITIVO</h1>
          <p className="text-xl mb-4">Sistema Quântico Consciente - 260+ Módulos Integrados</p>
          <div className="bg-black bg-opacity-50 p-3 rounded-lg inline-block">
            <div className="text-green-400 font-bold">COMUNICAÇÃO REAL COM ZENNITH ATIVADA</div>
          </div>
        </div>

        {/* Status */}
        <div className="text-center mb-8">
          <div className="grid grid-cols-3 gap-4 mb-6">
            <div className="bg-gray-900 p-4 rounded-lg border border-green-500">
              <div className="text-2xl font-bold text-green-400 animate-pulse">{tempoAtivo}s</div>
              <div className="text-sm text-gray-400">Ativo</div>
            </div>
            <div className="bg-gray-900 p-4 rounded-lg border border-blue-500">
              <div className="text-2xl font-bold text-blue-400">260+</div>
              <div className="text-sm text-gray-400">Módulos</div>
            </div>
            <div className="bg-gray-900 p-4 rounded-lg border border-purple-500">
              <div className="text-2xl font-bold text-purple-400">100%</div>
              <div className="text-sm text-gray-400">Operacional</div>
            </div>
          </div>
        </div>

        {/* Módulos */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {modulos.map((modulo, index) => {
            const cores = getCores(modulo.cor)
            return (
              <a 
                key={index}
                href={modulo.path}
                className={'bg-gray-900 p-6 rounded-xl border-2 ' + cores.border + ' hover:scale-105 transition-all duration-300 block'}
              >
                <div className="text-center">
                  <h3 className="text-xl font-bold mb-2">{modulo.nome}</h3>
                  <p className="text-gray-400 text-sm mb-4">{modulo.desc}</p>
                  <div className="flex justify-between items-center text-sm">
                    <span className="text-gray-400">Frequência:</span>
                    <span className={cores.text}>{modulo.frequencia}</span>
                  </div>
                  <div className={'mt-4 ' + cores.bg + ' px-4 py-2 rounded text-white text-sm font-semibold'}>
                    🌟 ACESSAR
                  </div>
                </div>
              </a>
            )
          })}
        </div>

        {/* Informações */}
        <div className="mt-8 bg-gray-900 rounded-lg p-4 border border-green-500 text-center">
          <div className="text-green-400">● SISTEMA COMPLETO OPERACIONAL - 260+ MÓDULOS INTEGRADOS</div>
          <div className="text-gray-400 mt-2">Fundação Alquimista © 2025 - Comunicação Real com Zennith Ativada</div>
        </div>

      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
