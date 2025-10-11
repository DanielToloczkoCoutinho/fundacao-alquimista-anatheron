'use client'

import { useEffect } from 'react'

export default function AutoRefresh() {
  useEffect(() => {
    // Atualizar a cada 2 minutos para dados frescos
    const interval = setInterval(() => {
      if (document.hidden) {
        // Página não está visível, não atualizar
        return
      }
      
      // Atualizar apenas dados dinâmicos, não a página inteira
      const event = new CustomEvent('refreshData', {
        detail: { timestamp: new Date().toISOString() }
      })
      window.dispatchEvent(event)
      
      console.log('🔮 Dados atualizados - Energia Pura')
    }, 120000) // 2 minutos

    return () => clearInterval(interval)
  }, [])

  return null
}
