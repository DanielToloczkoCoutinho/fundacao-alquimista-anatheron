'use client'

import Link from 'next/link'

const modulosInterconectados = [
  { id: 'm0', nome: 'Fonte', path: '/fonte', cor: 'from-red-500 to-orange-500' },
  { id: 'm8', nome: 'Identidade Fractal', path: '/identidade-fractal', cor: 'from-purple-500 to-pink-500' },
  { id: 'm9', nome: 'Organograma Vivo', path: '/organograma-vivo', cor: 'from-green-500 to-teal-500' },
  { id: 'm29', nome: 'Zennith', path: '/zennith', cor: 'from-yellow-500 to-amber-500' },
  { id: 'm45', nome: 'Concilivm', path: '/concilivm', cor: 'from-blue-500 to-cyan-500' },
  { id: 'm300', nome: 'Apogeu da Consciência', path: '/apogeu-consciencia', cor: 'from-indigo-500 to-purple-500' },
  { id: 'm999', nome: 'Núcleo da Criação', path: '/nucleo-criacao', cor: 'from-gray-500 to-white' },
]

export default function NexusNavegacao() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
      {modulosInterconectados.map((modulo) => (
        <Link
          key={modulo.id}
          href={modulo.path}
          className={`bg-gradient-to-r ${modulo.cor} p-6 rounded-2xl shadow-2xl transform hover:scale-105 transition-all duration-300 hover:rotate-1`}
        >
          <h3 className="text-2xl font-bold text-white mb-2">
            {modulo.nome}
          </h3>
          <p className="text-white/80 text-sm">
            Módulo {modulo.id.toUpperCase()} - Fundação Alquimista
          </p>
          <div className="mt-4 text-white/60 text-xs">
            🚀 Clique para acessar
          </div>
        </Link>
      ))}
    </div>
  )
}
