'use client'

import { useState, useEffect } from 'react'

interface Sistema {
  id: string
  nome: string
  tipo: 'python' | 'typescript' | 'react' | 'alquimico'
  status: 'ativo' | 'inativo' | 'carregando'
  descricao: string
}

export default function CarregadorDinamico() {
  const [sistemas, setSistemas] = useState<Sistema[]>([])
  const [carregando, setCarregando] = useState(true)

  useEffect(() => {
    // Simular carregamento de sistemas dinâmicos
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
      },
      {
        id: 'fundacao-dinamica',
        nome: 'Fundação Dinâmica',
        tipo: 'alquimico',
        status: 'carregando',
        descricao: 'Transição de estático para dinâmico'
      }
    ]

    setTimeout(() => {
      setSistemas(sistemasExemplo)
      setCarregando(false)
    }, 2000)
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
