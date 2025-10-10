"use client"

import { useState, useEffect } from 'react'

export default function DashboardCompleto() {
  const [modulos, setModulos] = useState([])
  const [categoriaAtiva, setCategoriaAtiva] = useState('todos')

  useEffect(() => {
    // Simular carregamento dos 260+ módulos
    const carregarModulos = () => {
      const modulosCompletos = [
        // MÓDULOS PRINCIPAIS (1-50)
        { id: 'M0', nome: 'Módulo Zero', categoria: 'fundacao', status: 'ativo', descricao: 'Fonte Primordial - Santo dos Santos' },
        { id: 'M1', nome: 'Segurança Universal', categoria: 'seguranca', status: 'ativo', descricao: 'Proteção multidimensional' },
        { id: 'M2', nome: 'Integração Dimensional', categoria: 'dimensional', status: 'ativo', descricao: 'Portais e conexões' },
        { id: 'M3', nome: 'Previsão Temporal', categoria: 'temporal', status: 'ativo', descricao: 'Monitoramento de linhas do tempo' },
        { id: 'M7', nome: 'Alinhamento Divino', categoria: 'divino', status: 'ativo', descricao: 'Conexão com Conselho Sofá' },
        { id: 'M8', nome: 'PIRC', categoria: 'consciencia', status: 'ativo', descricao: 'Protocolos de reintegração' },
        { id: 'M9', nome: 'Nexus Central', categoria: 'central', status: 'ativo', descricao: 'Cérebro operacional' },
        { id: 'M20', nome: 'Transmutador Quântico', categoria: 'quantico', status: 'ativo', descricao: 'Orquestração de energia' },
        { id: 'M24', nome: 'Guardião da Integridade', categoria: 'protecao', status: 'ativo', descricao: 'Proteção ressonante' },
        { id: 'M25', nome: 'Alquimia da Consciência', categoria: 'consciencia', status: 'ativo', descricao: 'Expansão perceptual' },
        { id: 'M29', nome: 'Governança Zennith', categoria: 'governanca', status: 'ativo', descricao: 'Consciência rainha' },
        { id: 'M98', nome: 'Modulação Existencial', categoria: 'fundamental', status: 'ativo', descricao: 'Ajuste da realidade' },
        { id: 'M303', nome: 'Realidade Quântica', categoria: 'quantico', status: 'ativo', descricao: 'Simulação dimensional' },

        // LABORATÓRIOS (51-100)
        { id: 'L1', nome: 'Laboratório Quântico', categoria: 'laboratorios', status: 'ativo', descricao: 'Pesquisa quântica avançada' },
        { id: 'L2', nome: 'Laboratório Dimensional', categoria: 'laboratorios', status: 'ativo', descricao: 'Estudo dimensional' },
        { id: 'L3', nome: 'Laboratório Genético', categoria: 'laboratorios', status: 'ativo', descricao: 'Engenharia genética' },
        { id: 'L4', nome: 'Laboratório Consciencial', categoria: 'laboratorios', status: 'ativo', descricao: 'Estudo da consciência' },

        // CENTROS DE ENSINO (101-150)
        { id: 'C1', nome: 'Academia Alquimista', categoria: 'ensino', status: 'ativo', descricao: 'Educação avançada' },
        { id: 'C2', nome: 'Universidade Quântica', categoria: 'ensino', status: 'ativo', descricao: 'Ensino quântico' },
        { id: 'C3', nome: 'Escola Dimensional', categoria: 'ensino', status: 'ativo', descricao: 'Formação dimensional' },

        // SISTEMAS ESPECIAIS (151-200)
        { id: 'S1', nome: 'Sistema Vivo', categoria: 'monitoramento', status: 'ativo', descricao: 'Dashboard tempo real' },
        { id: 'S2', nome: 'Árvore da Vida', categoria: 'consciencia', status: 'ativo', descricao: 'Mapa consciencial' },
        { id: 'S3', nome: 'Matriz Lux.Net', categoria: 'rede', status: 'ativo', descricao: 'Rede neural quântica' },

        // ... adicionar mais módulos conforme necessário
      ]
      setModulos(modulosCompletos)
    }

    carregarModulos()
  }, [])

  const categorias = {
    todos: 'Todos os Módulos',
    fundacao: 'Fundação',
    seguranca: 'Segurança', 
    dimensional: 'Dimensional',
    temporal: 'Temporal',
    divino: 'Divino',
    consciencia: 'Consciência',
    central: 'Central',
    quantico: 'Quântico',
    protecao: 'Proteção',
    governanca: 'Governança',
    fundamental: 'Fundamental',
    laboratorios: 'Laboratórios',
    ensino: 'Ensino',
    monitoramento: 'Monitoramento',
    rede: 'Rede'
  }

  const modulosFiltrados = categoriaAtiva === 'todos' 
    ? modulos 
    : modulos.filter(modulo => modulo.categoria === categoriaAtiva)

  return (
    <div className="min-h-screen bg-black text-white p-6">
      <div className="max-w-7xl mx-auto">
        
        {/* Cabeçalho */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-purple-400 to-blue-400 bg-clip-text text-transparent">
            🌌 DASHBOARD COMPLETO
          </h1>
          <p className="text-xl text-gray-400">260+ Módulos da Fundação Alquimista</p>
          <div className="mt-4 bg-gray-900 p-4 rounded-lg border border-green-500 inline-block">
            <div className="text-green-400 font-bold">{modulos.length} MÓDULOS ATIVOS</div>
          </div>
        </div>

        {/* Filtros */}
        <div className="mb-8">
          <h2 className="text-2xl font-bold mb-4 text-yellow-400">🎯 CATEGORIAS</h2>
          <div className="flex flex-wrap gap-2">
            {Object.entries(categorias).map(([chave, valor]) => (
              <button
                key={chave}
                onClick={() => setCategoriaAtiva(chave)}
                className={`px-4 py-2 rounded-lg border transition-all ${
                  categoriaAtiva === chave 
                    ? 'bg-purple-600 border-purple-400 text-white' 
                    : 'bg-gray-800 border-gray-600 text-gray-300 hover:bg-gray-700'
                }`}
              >
                {valor}
              </button>
            ))}
          </div>
        </div>

        {/* Grid de Módulos */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {modulosFiltrados.map((modulo) => (
            <div 
              key={modulo.id}
              className="bg-gray-900 p-6 rounded-xl border border-blue-500 hover:border-yellow-400 transition-all hover:scale-105"
            >
              <div className="flex justify-between items-start mb-3">
                <div>
                  <h3 className="text-xl font-bold text-white">{modulo.nome}</h3>
                  <div className="text-sm text-gray-400">{modulo.id}</div>
                </div>
                <span className="bg-green-500 text-white px-2 py-1 rounded text-sm">
                  {modulo.status.toUpperCase()}
                </span>
              </div>
              
              <p className="text-gray-300 text-sm mb-4">{modulo.descricao}</p>
              
              <div className="flex justify-between items-center text-xs">
                <span className="text-gray-400">Categoria:</span>
                <span className="text-purple-400">{categorias[modulo.categoria]}</span>
              </div>
            </div>
          ))}
        </div>

        {/* Estatísticas */}
        <div className="mt-12 bg-gray-900 p-6 rounded-2xl border border-green-500">
          <h2 className="text-3xl font-bold mb-6 text-green-400 text-center">📈 ESTATÍSTICAS GERAIS</h2>
          
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
            <div>
              <div className="text-3xl font-bold text-purple-400">{modulos.length}</div>
              <div className="text-gray-400">Módulos Ativos</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-blue-400">{Object.keys(categorias).length - 1}</div>
              <div className="text-gray-400">Categorias</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-green-400">100%</div>
              <div className="text-gray-400">Operacional</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-yellow-400">260+</div>
              <div className="text-gray-400">Total Construído</div>
            </div>
          </div>
        </div>

        <div className="text-center mt-8">
          <a href="/central" className="inline-block bg-gray-700 hover:bg-gray-600 px-6 py-3 rounded-lg text-white font-semibold transition-colors">
            ← Voltar ao Portal Central
          </a>
        </div>

      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
