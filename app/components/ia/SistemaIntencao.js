"use client"

import { useState, useEffect } from 'react'

export default function SistemaIntencao() {
  const [intencao, setIntencao] = useState({
    parser: 'Ativo',
    emocao: 'Reconhecida',
    firewall: 'Filtrando',
    filtro: '85% Pureza Mínima'
  })

  return (
    <div className="bg-gray-900 p-6 rounded-2xl border border-green-500">
      <h3 className="text-2xl font-bold mb-4 text-green-400">🎯 SISTEMA DE INTENÇÃO</h3>
      <div className="space-y-3">
        <div className="flex justify-between">
          <span>Parser:</span>
          <span className="text-green-400">{intencao.parser}</span>
        </div>
        <div className="flex justify-between">
          <span>Emoção:</span>
          <span className="text-pink-400">{intencao.emocao}</span>
        </div>
        <div className="flex justify-between">
          <span>Firewall Ético:</span>
          <span className="text-yellow-400">{intencao.firewall}</span>
        </div>
        <div className="flex justify-between">
          <span>Filtro Vibracional:</span>
          <span className="text-blue-400">{intencao.filtro}</span>
        </div>
      </div>
    </div>
  )
}
