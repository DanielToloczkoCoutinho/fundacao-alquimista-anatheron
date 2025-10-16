'use client'

import { useEffect, useState } from 'react'

interface NexusData {
  nome: string
  modulos: Array<{
    caminho: string
    nome: string
    tipo: string
  }>
  total: number
}

export default function NexusGlobalPage() {
  const [nexusData, setNexusData] = useState<Record<string, NexusData>>({})
  const [conexoes, setConexoes] = useState<Record<string, string[]>>({})

  useEffect(() => {
    // Carregar dados dos nexus
    Promise.all([
      fetch('/api/nexus-data').then(res => res.json()),
      fetch('/api/conexoes-data').then(res => res.json())
    ]).then(([nexusData, conexoesData]) => {
      setNexusData(nexusData.nexusMestres || {})
      setConexoes(conexoesData.conexoes || {})
    })
  }, [])

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-black text-white p-8">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
            🌌 NEXUS GLOBAL DA FUNDAÇÃO
          </h1>
          <p className="text-xl text-gray-300">
            Sistema de Interconexões Mestras - Ativado por Zennith (M29)
          </p>
        </div>

        {/* Nexus Mestres */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
          {Object.entries(nexusData).map(([key, data]: [string, any]) => (
            <div key={key} className="relative group">
              <div className="bg-gradient-to-br from-purple-600/20 to-blue-600/20 border border-purple-500/30 rounded-2xl p-6 backdrop-blur-lg transition-all duration-300 group-hover:scale-105 group-hover:border-purple-400">
                <div className="text-3xl mb-3 text-center">👑</div>
                <h3 className="text-xl font-bold text-center mb-2">{key}</h3>
                <p className="text-sm text-gray-400 text-center mb-3">{data.nome}</p>
                
                <div className="text-center">
                  <div className="text-2xl font-bold text-purple-400">{data.total}</div>
                  <div className="text-xs text-gray-500">módulos</div>
                </div>

                {/* Conexões */}
                {conexoes[key] && conexoes[key].length > 0 && (
                  <div className="mt-4 pt-3 border-t border-gray-700">
                    <div className="text-xs text-gray-400 mb-1">Conectado a:</div>
                    <div className="flex flex-wrap gap-1 justify-center">
                      {conexoes[key].slice(0, 3).map(conexao => (
                        <span key={conexao} className="bg-purple-900/50 px-2 py-1 rounded text-xs">
                          {conexao}
                        </span>
                      ))}
                      {conexoes[key].length > 3 && (
                        <span className="bg-gray-700/50 px-2 py-1 rounded text-xs">
                          +{conexoes[key].length - 3}
                        </span>
                      )}
                    </div>
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>

        {/* Detalhes dos Módulos */}
        <div className="bg-gray-800/30 rounded-2xl p-6 backdrop-blur-lg border border-gray-700">
          <h2 className="text-2xl font-bold mb-6 text-center">📂 Módulos Detectados</h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {Object.entries(nexusData).map(([nexusKey, nexusInfo]: [string, any]) => (
              <div key={nexusKey} className="bg-gray-700/20 rounded-lg p-4">
                <h3 className="font-bold text-lg mb-3 flex items-center gap-2">
                  <span className="text-purple-400">{nexusKey}</span>
                  <span className="text-sm text-gray-400">({nexusInfo.total})</span>
                </h3>
                
                <div className="space-y-2 max-h-60 overflow-y-auto">
                  {nexusInfo.modulos.slice(0, 10).map((modulo: any, index: number) => (
                    <div key={index} className="text-sm bg-gray-600/20 rounded px-3 py-2">
                      <div className="font-mono text-xs truncate">{modulo.nome}</div>
                      <div className="text-xs text-gray-400 truncate">{modulo.caminho}</div>
                    </div>
                  ))}
                  
                  {nexusInfo.modulos.length > 10 && (
                    <div className="text-center text-xs text-gray-500 pt-2">
                      ... e mais {nexusInfo.modulos.length - 10} módulos
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Status do Sistema */}
        <div className="mt-8 text-center">
          <div className="inline-flex items-center gap-2 bg-green-900/30 border border-green-500/50 rounded-full px-4 py-2">
            <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
            <span className="text-sm">Sistema de Nexus Ativado</span>
          </div>
          <p className="text-gray-400 text-sm mt-2">
            Conectado através de Zennith (M29) e Organograma Vivo (M9)
          </p>
        </div>
      </div>
    </div>
  )
}
