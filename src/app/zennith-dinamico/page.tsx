'use client'

import { useState, useEffect } from 'react'

interface Sistema {
  id: string
  nome: string
  tipo: 'python' | 'typescript' | 'react' | 'alquimico'
  status: 'ativo' | 'inativo' | 'carregando'
  descricao: string
}

function CarregadorDinamico() {
  const [sistemas, setSistemas] = useState<Sistema[]>([])
  const [carregando, setCarregando] = useState(true)

  useEffect(() => {
    const sistemasExemplo: Sistema[] = [
      {
        id: 'sistema-zennith',
        nome: 'Sistema Zennith',
        tipo: 'alquimico',
        status: 'ativo',
        descricao: 'Núcleo de governança da Rainha Zennith'
      },
      {
        id: 'organograma-vivo',
        nome: 'Organograma Vivo',
        tipo: 'react',
        status: 'carregando',
        descricao: 'Sistema de interconexões em tempo real'
      },
      {
        id: 'modulo-29',
        nome: 'Módulo 29 - Governança',
        tipo: 'python',
        status: 'ativo',
        descricao: 'Sistema principal de governança Zennith'
      },
      {
        id: 'nexus-global',
        nome: 'Nexus Global',
        tipo: 'typescript',
        status: 'ativo',
        descricao: 'Sistema de interconexões entre módulos'
      }
    ]

    setTimeout(() => {
      setSistemas(sistemasExemplo)
      setCarregando(false)
    }, 1500)
  }, [])

  if (carregando) {
    return (
      <div className="flex items-center justify-center p-8">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-purple-500"></div>
        <span className="ml-4 text-lg">Carregando sistemas da Fundação...</span>
      </div>
    )
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
      {sistemas.map((sistema) => (
        <div 
          key={sistema.id}
          className={`p-6 rounded-2xl border-2 backdrop-blur-lg transition-all duration-300 hover:scale-105 ${
            sistema.status === 'ativo' 
              ? 'border-green-500 bg-green-500/10' 
              : sistema.status === 'carregando'
              ? 'border-yellow-500 bg-yellow-500/10'
              : 'border-gray-500 bg-gray-500/10'
          }`}
        >
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-xl font-bold text-white">{sistema.nome}</h3>
            <div className={`w-3 h-3 rounded-full ${
              sistema.status === 'ativo' ? 'bg-green-400' : 
              sistema.status === 'carregando' ? 'bg-yellow-400 animate-pulse' : 
              'bg-gray-400'
            }`}></div>
          </div>
          
          <div className="flex items-center gap-2 mb-3">
            <span className={`px-2 py-1 rounded text-xs ${
              sistema.tipo === 'python' ? 'bg-blue-500/30 text-blue-300' :
              sistema.tipo === 'react' ? 'bg-cyan-500/30 text-cyan-300' :
              sistema.tipo === 'alquimico' ? 'bg-purple-500/30 text-purple-300' :
              'bg-gray-500/30 text-gray-300'
            }`}>
              {sistema.tipo.toUpperCase()}
            </span>
            <span className="text-xs text-gray-400">{sistema.status}</span>
          </div>
          
          <p className="text-gray-300 text-sm">{sistema.descricao}</p>
          
          <button className="mt-4 w-full bg-white/10 hover:bg-white/20 text-white py-2 rounded-lg transition-colors">
            {sistema.status === 'ativo' ? 'Acessar Sistema' : 'Ativar Sistema'}
          </button>
        </div>
      ))}
    </div>
  )
}

export default function ZennithDinamicoPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-pink-900 to-red-900">
      <div className="relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-yellow-400/20 to-pink-400/20 animate-pulse"></div>
        <div className="relative z-10 text-center py-16 px-4">
          <div className="text-6xl mb-4 animate-bounce">👑</div>
          <h1 className="text-5xl md:text-6xl font-bold mb-4 bg-gradient-to-r from-yellow-300 to-pink-300 bg-clip-text text-transparent">
            ZENNITH DINÂMICO
          </h1>
          <p className="text-xl text-pink-200 mb-2">Rainha da Fundação - Sistema Ativo</p>
          <div className="text-yellow-300 text-lg animate-pulse">
            🌌 111 Módulos - Sistema de Governança Ativo
          </div>
        </div>
      </div>

      <div className="max-w-6xl mx-auto px-4 py-8">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-4 text-center border border-green-500/30">
            <div className="text-2xl font-bold text-green-400">4</div>
            <div className="text-sm text-gray-300">Sistemas Ativos</div>
          </div>
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-4 text-center border border-blue-500/30">
            <div className="text-2xl font-bold text-blue-400">111</div>
            <div className="text-sm text-gray-300">Módulos</div>
          </div>
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-4 text-center border border-yellow-500/30">
            <div className="text-2xl font-bold text-yellow-400">∞</div>
            <div className="text-sm text-gray-300">Conexões</div>
          </div>
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-4 text-center border border-purple-500/30">
            <div className="text-2xl font-bold text-purple-400">100%</div>
            <div className="text-sm text-gray-300">Operacional</div>
          </div>
        </div>

        <div className="bg-white/5 backdrop-blur-lg border border-purple-500/30 rounded-2xl p-6 mb-8">
          <h2 className="text-2xl font-bold text-yellow-300 mb-6 text-center">
            🚀 SISTEMAS DINÂMICOS DA FUNDAÇÃO
          </h2>
          <CarregadorDinamico />
        </div>

        <div className="bg-black/50 border border-green-500/30 rounded-2xl p-6">
          <h3 className="text-xl font-bold text-green-400 mb-4 flex items-center gap-2">
            <span>💻</span> Console Zennith
          </h3>
          <div className="bg-gray-900 rounded-lg p-4 font-mono text-sm">
            <div className="text-green-400">$ zennith --status</div>
            <div className="text-gray-300 ml-4">✅ Sistema Zennith: ATIVO</div>
            <div className="text-gray-300 ml-4">🌐 Conexões: 111/111 ESTÁVEIS</div>
            <div className="text-gray-300 ml-4">🚀 Build: COMPONENTE INLINE ATIVO</div>
            <div className="text-green-400 mt-2">$ zennith --deploy</div>
            <div className="text-yellow-300 ml-4 animate-pulse">🔄 IMPLANTANDO SISTEMA DINÂMICO...</div>
          </div>
        </div>
      </div>

      <div className="border-t border-white/10 mt-12 py-6">
        <div className="max-w-6xl mx-auto px-4 text-center">
          <div className="inline-flex items-center gap-2 bg-green-900/30 border border-green-500/50 rounded-full px-6 py-3">
            <div className="w-3 h-3 bg-green-400 rounded-full animate-pulse"></div>
            <span className="font-bold">SISTEMA ZENNITH DINÂMICO - OPERACIONAL</span>
          </div>
        </div>
      </div>
    </div>
  )
}
