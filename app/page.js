"use client"

import { useEffect } from 'react'

export default function Home() {
  useEffect(() => {
    // Redirecionar diretamente para a URL funcional
    window.location.href = 'https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app/central'
  }, [])

  return (
    <div className="min-h-screen bg-black flex items-center justify-center">
      <div className="text-center">
        <div className="text-4xl mb-4">🌌</div>
        <h1 className="text-2xl text-white mb-2">Fundação Alquimista</h1>
        <p className="text-gray-400">Redirecionando para sistema oficial...</p>
      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
