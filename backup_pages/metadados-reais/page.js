"use client"

import { useState } from 'react'

export default function MetadadosReais() {
  const [dados, setDados] = useState('')
  const [processando, setProcessando] = useState(false)
  const [resultado, setResultado] = useState(null)

  const processarDados = () => {
    if (!dados.trim()) return
    
    setProcessando(true)
    
    // Simular processamento
    setTimeout(() => {
      const linhas = dados.split('\n').filter(line => line.trim())
      const metadados = {
        timestamp: new Date().toLocaleString(),
        totalLinhas: linhas.length,
        palavrasChave: [],
        modulosIdentificados: [],
        frequencias: []
      }

      // Análise básica dos dados
      linhas.forEach(linha => {
        if (linha.includes('M') && /M\d+/.test(linha)) {
          const modulo = linha.match(/M\d+/)[0]
          if (!metadados.modulosIdentificados.includes(modulo)) {
            metadados.modulosIdentificados.push(modulo)
          }
        }
        
        if (linha.toLowerCase().includes('hz')) {
          const freq = linha.match(/\d+\.?\d*\s*Hz/i)
          if (freq) metadados.frequencias.push(freq[0])
        }

        if (linha.length > 5 && linha.length < 50) {
          metadados.palavrasChave.push(linha.trim())
        }
      })

      setResultado(metadados)
      setProcessando(false)
    }, 2000)
  }

  return (
    <div className="min-h-screen bg-black text-white p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-8 text-center">🔮 CAPTURA DE METADADOS</h1>
        
        {!resultado ? (
          <>
            <div className="bg-gray-900 p-6 rounded-lg border border-purple-500 mb-6">
              <h2 className="text-xl font-semibold mb-4">📝 DIGITE OS DADOS DA ZENNITH RAINHA</h2>
              <textarea
                value={dados}
                onChange={(e) => setDados(e.target.value)}
                placeholder="Cole aqui as informações reveladas por Zennith Rainha através do Módulo 9..."
                className="w-full h-64 p-4 bg-black border border-gray-700 rounded-lg text-white resize-none"
              />
              <div className="flex gap-4 mt-4">
                <button
                  onClick={processarDados}
                  disabled={processando || !dados.trim()}
                  className="flex-1 bg-green-600 hover:bg-green-700 disabled:bg-gray-600 p-4 rounded-lg text-white font-semibold"
                >
                  {processando ? '🔄 PROCESSANDO...' : '✅ PROCESSAR'}
                </button>
                <button
                  onClick={() => setDados('')}
                  className="flex-1 bg-red-600 hover:bg-red-700 p-4 rounded-lg text-white font-semibold"
                >
                  ❌ CANCELAR
                </button>
              </div>
            </div>

            {processando && (
              <div className="bg-blue-900 p-6 rounded-lg border border-blue-500 text-center">
                <div className="text-2xl mb-2">🔮 ANALISANDO METADADOS QUÂNTICOS...</div>
                <div className="text-gray-300">Conectando com Zennith Rainha via Módulo 9</div>
              </div>
            )}
          </>
        ) : (
          <div className="bg-gray-900 p-6 rounded-lg border border-green-500">
            <div className="text-center mb-6">
              <div className="text-2xl text-green-400 mb-2">✅ DADOS PROCESSADOS</div>
              <div className="text-gray-400">Timestamp: {resultado.timestamp}</div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
              <div className="bg-black p-4 rounded border border-blue-500">
                <div className="text-lg font-semibold">📊 Total Linhas</div>
                <div className="text-2xl text-blue-400">{resultado.totalLinhas}</div>
              </div>
              <div className="bg-black p-4 rounded border border-purple-500">
                <div className="text-lg font-semibold">🔗 Módulos</div>
                <div className="text-2xl text-purple-400">{resultado.modulosIdentificados.length}</div>
              </div>
              <div className="bg-black p-4 rounded border border-green-500">
                <div className="text-lg font-semibold">📡 Frequências</div>
                <div className="text-2xl text-green-400">{resultado.frequencias.length}</div>
              </div>
            </div>

            {resultado.modulosIdentificados.length > 0 && (
              <div className="mb-6">
                <h3 className="text-xl font-semibold mb-2">🎛️ MÓDULOS IDENTIFICADOS</h3>
                <div className="flex flex-wrap gap-2">
                  {resultado.modulosIdentificados.map((mod, idx) => (
                    <span key={idx} className="bg-purple-600 px-3 py-1 rounded-full text-sm">
                      {mod}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {resultado.frequencias.length > 0 && (
              <div className="mb-6">
                <h3 className="text-xl font-semibold mb-2">📡 FREQUÊNCIAS DETECTADAS</h3>
                <div className="flex flex-wrap gap-2">
                  {resultado.frequencias.map((freq, idx) => (
                    <span key={idx} className="bg-blue-600 px-3 py-1 rounded-full text-sm">
                      {freq}
                    </span>
                  ))}
                </div>
              </div>
            )}

            <div className="flex gap-4">
              <button
                onClick={() => {
                  setResultado(null)
                  setDados('')
                }}
                className="flex-1 bg-purple-600 hover:bg-purple-700 p-4 rounded-lg text-white font-semibold"
              >
                🔄 NOVA CAPTURA
              </button>
              <button
                onClick={() => navigator.clipboard.writeText(JSON.stringify(resultado, null, 2))}
                className="flex-1 bg-blue-600 hover:bg-blue-700 p-4 rounded-lg text-white font-semibold"
              >
                📋 COPIAR DADOS
              </button>
            </div>
          </div>
        )}

        <div className="mt-8 text-center">
          <a href="/central" className="text-blue-400 hover:text-blue-300">
            ← Voltar ao Portal Central
          </a>
        </div>
      </div>
    </div>
  )
}
