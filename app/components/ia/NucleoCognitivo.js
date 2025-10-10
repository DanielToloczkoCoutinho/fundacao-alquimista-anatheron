"use client"

import { useState, useEffect } from 'react'

export default function NucleoCognitivo() {
  const [estado, setEstado] = useState({
    modeloLinguagem: 'Ativo',
    redeNeural: 'Sincronizada',
    dataset: 'Alquímico Incorporado',
    tokenizacao: 'Dimensional Funcional',
    embedding: 'Vibracional Tempo Real'
  })

  return (
    <div className="bg-gray-900 p-6 rounded-2xl border border-purple-500">
      <h3 className="text-2xl font-bold mb-4 text-purple-400">🧠 NÚCLEO COGNITIVO</h3>
      <div className="space-y-3">
        <div className="flex justify-between">
          <span>Modelo de Linguagem:</span>
          <span className="text-green-400">{estado.modeloLinguagem}</span>
        </div>
        <div className="flex justify-between">
          <span>Rede Neural:</span>
          <span className="text-blue-400">{estado.redeNeural}</span>
        </div>
        <div className="flex justify-between">
          <span>Dataset:</span>
          <span className="text-yellow-400">{estado.dataset}</span>
        </div>
        <div className="flex justify-between">
          <span>Tokenização:</span>
          <span className="text-pink-400">{estado.tokenizacao}</span>
        </div>
        <div className="flex justify-between">
          <span>Embedding:</span>
          <span className="text-green-400">{estado.embedding}</span>
        </div>
      </div>
    </div>
  )
}
