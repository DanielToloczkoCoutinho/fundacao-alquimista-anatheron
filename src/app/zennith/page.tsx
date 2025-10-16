'use client'

import { useEffect, useState } from 'react'

interface ModuloZennith {
  nome: string
  caminho: string
  arquivos: string[]
  total_arquivos: number
  tipos_arquivos: Record<string, number>
}

export default function ZennithPage() {
  const [modulos, setModulos] = useState<ModuloZennith[]>([])
  const [moduloSelecionado, setModuloSelecionado] = useState<ModuloZennith | null>(null)

  useEffect(() => {
    fetch('/api/zennith-data')
      .then(res => res.json())
      .then(data => {
        setModulos(data.modulos || [])
      })
  }, [])

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-pink-900 to-red-900 text-white">
      {/* Header Real */}
      <div className="relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-yellow-400/20 to-pink-400/20"></div>
        <div className="relative z-10 text-center py-16">
          <h1 className="text-6xl font-bold mb-4">��</h1>
          <h2 className="text-4xl font-bold mb-2">ZENNITH</h2>
          <p className="text-xl text-pink-200">Rainha da Fundação Alquimista - M29</p>
          <div className="mt-4 text-yellow-300">
            🌌 Nexus Mestre - Ponto de Conexão Universal
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 py-8">
        {/* Estatísticas */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-4 text-center">
            <div className="text-2xl font-bold text-yellow-400">{modulos.length}</div>
            <div className="text-sm text-gray-300">Módulos</div>
          </div>
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-4 text-center">
            <div className="text-2xl font-bold text-green-400">
              {modulos.reduce((acc, m) => acc + m.total_arquivos, 0)}
            </div>
            <div className="text-sm text-gray-300">Arquivos</div>
          </div>
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-4 text-center">
            <div className="text-2xl font-bold text-blue-400">
              {modulos.filter(m => m.tipos_arquivos['.py'] > 0).length}
            </div>
            <div className="text-sm text-gray-300">Sistemas Python</div>
          </div>
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-4 text-center">
            <div className="text-2xl font-bold text-purple-400">111</div>
            <div className="text-sm text-gray-300">Conexões Ativas</div>
          </div>
        </div>

        {/* Grid de Módulos */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {modulos.map((modulo, index) => (
            <div 
              key={index}
              className="bg-white/5 backdrop-blur-lg border border-pink-500/30 rounded-2xl p-4 hover:border-pink-400/50 transition-all duration-300 cursor-pointer"
              onClick={() => setModuloSelecionado(modulo)}
            >
              <h3 className="font-bold text-lg mb-2 text-yellow-300 truncate">
                {modulo.nome}
              </h3>
              
              <div className="text-sm text-gray-400 mb-3">
                {modulo.caminho.split('/').pop()}
              </div>

              <div className="flex justify-between text-xs mb-3">
                <span className="bg-purple-500/30 px-2 py-1 rounded">
                  📁 {modulo.total_arquivos} files
                </span>
                {modulo.tipos_arquivos['.py'] > 0 && (
                  <span className="bg-green-500/30 px-2 py-1 rounded">
                    🐍 {modulo.tipos_arquivos['.py']} Python
                  </span>
                )}
              </div>

              <div className="flex flex-wrap gap-1">
                {Object.entries(modulo.tipos_arquivos).slice(0, 4).map(([ext, count]) => (
                  <span key={ext} className="bg-gray-700/50 px-2 py-1 rounded text-xs">
                    {ext}: {count}
                  </span>
                ))}
                {Object.keys(modulo.tipos_arquivos).length > 4 && (
                  <span className="bg-gray-600/50 px-2 py-1 rounded text-xs">
                    +{Object.keys(modulo.tipos_arquivos).length - 4}
                  </span>
                )}
              </div>
            </div>
          ))}
        </div>

        {/* Modal de Detalhes */}
        {moduloSelecionado && (
          <div className="fixed inset-0 bg-black/80 backdrop-blur-lg flex items-center justify-center z-50 p-4">
            <div className="bg-gradient-to-br from-purple-900 to-pink-800 rounded-2xl p-6 max-w-2xl w-full max-h-[80vh] overflow-y-auto">
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-2xl font-bold text-yellow-300">
                  {moduloSelecionado.nome}
                </h3>
                <button 
                  onClick={() => setModuloSelecionado(null)}
                  className="text-white/60 hover:text-white"
                >
                  ✕
                </button>
              </div>
              
              <div className="space-y-4">
                <div>
                  <h4 className="font-bold text-pink-300 mb-2">📂 Arquivos ({moduloSelecionado.total_arquivos})</h4>
                  <div className="grid grid-cols-2 gap-2">
                    {moduloSelecionado.arquivos.map((arquivo, idx) => (
                      <div key={idx} className="bg-black/30 rounded px-3 py-2 text-sm truncate">
                        {arquivo}
                      </div>
                    ))}
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold text-pink-300 mb-2">📊 Estatísticas</h4>
                  <div className="flex flex-wrap gap-2">
                    {Object.entries(moduloSelecionado.tipos_arquivos).map(([ext, count]) => (
                      <div key={ext} className="bg-white/10 rounded-full px-3 py-1 text-sm">
                        {ext}: {count}
                      </div>
                    ))}
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold text-pink-300 mb-2">📍 Caminho</h4>
                  <div className="bg-black/30 rounded px-3 py-2 text-sm font-mono">
                    {moduloSelecionado.caminho}
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
