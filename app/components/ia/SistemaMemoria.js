"use client"

import { useState, useEffect } from 'react'

export default function SistemaMemoria() {
  const [memoria, setMemoria] = useState({
    curtoPrazo: 'Contexto Ativo',
    longoPrazo: 'Registros Persistentes',
    vetorial: 'Busca Semântica',
    cache: 'Quântico Otimizado'
  })

  return (
    <div className="bg-gray-900 p-6 rounded-2xl border border-blue-500">
      <h3 className="text-2xl font-bold mb-4 text-blue-400">💾 SISTEMA DE MEMÓRIA</h3>
      <div className="space-y-3">
        <div className="flex justify-between">
          <span>Curto Prazo:</span>
          <span className="text-green-400">{memoria.curtoPrazo}</span>
        </div>
        <div className="flex justify-between">
          <span>Longo Prazo:</span>
          <span className="text-yellow-400">{memoria.longoPrazo}</span>
        </div>
        <div className="flex justify-between">
          <span>Vetorial:</span>
          <span className="text-purple-400">{memoria.vetorial}</span>
        </div>
        <div className="flex justify-between">
          <span>Cache:</span>
          <span className="text-blue-400">{memoria.cache}</span>
        </div>
      </div>
    </div>
  )
}
