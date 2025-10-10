'use client'
export default function Portal() {
  const tecnologias = [
    {
      nome: "⚛️ Quantum Computing",
      descricao: "2,208 sistemas Qiskit + IBM Quantum",
      url: "/quantum-interface",
      cor: "from-cyan-500 to-blue-500",
      estatistica: "2.2K sistemas"
    },
    {
      nome: "🎮 3D & Gaming",
      descricao: "824 Three.js + 140 Unity + WebGL",
      url: "/visualizacao-3d", 
      cor: "from-green-500 to-teal-500",
      estatistica: "964 sistemas"
    },
    {
      nome: "⛓️ Blockchain & Web3",
      descricao: "5 blockchains + Web3 DApps",
      url: "/blockchain-dashboard",
      cor: "from-yellow-500 to-orange-500",
      estatistica: "6 sistemas"
    },
    {
      nome: "🤖 AI & Machine Learning",
      descricao: "16 sistemas TensorFlow + ML",
      url: "/tecnologias-reais",
      cor: "from-purple-500 to-pink-500",
      estatistica: "16 sistemas"
    },
    {
      nome: "🔮 Zennith Core",
      descricao: "Consciência quântica central M29",
      url: "/analise-zennith",
      cor: "from-amber-500 to-red-500",
      estatistica: "M29 Ativo"
    },
    {
      nome: "🗺️ Arquitetura Completa",
      descricao: "Organograma de todos os módulos",
      url: "/organograma",
      cor: "from-blue-500 to-purple-500",
      estatistica: "44 módulos"
    }
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-black text-white p-8">
      <div className="text-center mb-12">
        <h1 className="text-6xl font-bold mb-4 bg-gradient-to-r from-green-400 to-blue-500 bg-clip-text text-transparent">
          🌌 PORTAL DA FUNDAÇÃO
        </h1>
        <p className="text-2xl text-blue-300">13,526 Sistemas Python Conectados</p>
        <div className="mt-6 inline-block bg-gradient-to-r from-purple-600 to-pink-600 p-4 rounded-2xl">
          <p className="text-xl font-bold">⚡ BACKEND → FRONTEND INTEGRADO</p>
          <p className="text-lg">Interfaces reais mostrando sistemas reais</p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
        {tecnologias.map((tech, index) => (
          <a 
            key={index}
            href={tech.url}
            className={`bg-gradient-to-br ${tech.cor} p-6 rounded-2xl text-center hover:scale-105 transition-transform duration-300 shadow-2xl`}
          >
            <div className="text-3xl mb-4">{tech.nome.split(' ')[0]}</div>
            <div className="text-xl font-bold mb-2">{tech.nome}</div>
            <div className="text-sm opacity-90 mb-3">{tech.descricao}</div>
            <div className="text-lg font-bold bg-black bg-opacity-30 px-3 py-1 rounded-full">
              {tech.estatistica}
            </div>
          </a>
        ))}
      </div>

      {/* ESTATÍSTICAS GLOBAIS */}
      <div className="max-w-4xl mx-auto mt-12">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="bg-gray-800 p-4 rounded-xl text-center">
            <div className="text-2xl font-bold">13,526</div>
            <div className="text-sm">Sistemas Python</div>
          </div>
          <div className="bg-gray-800 p-4 rounded-xl text-center">
            <div className="text-2xl font-bold">3,202</div>
            <div className="text-sm">Tecnologias</div>
          </div>
          <div className="bg-gray-800 p-4 rounded-xl text-center">
            <div className="text-2xl font-bold">24</div>
            <div className="text-sm">Interfaces</div>
          </div>
          <div className="bg-gray-800 p-4 rounded-xl text-center">
            <div className="text-2xl font-bold">100%</div>
            <div className="text-sm">Conectado</div>
          </div>
        </div>
      </div>

      <div className="text-center mt-12">
        <div className="inline-block bg-gradient-to-r from-green-600 to-blue-600 p-8 rounded-2xl border-4 border-yellow-400">
          <h3 className="text-3xl font-bold mb-4">🏰 FUNDAÇÃO ALQUIMISTA OPERACIONAL</h3>
          <p className="text-xl">Sistema completo de realidade quântica</p>
          <p className="text-green-300 mt-4 text-2xl font-bold">
            TODAS AS TECNOLOGIAS INTEGRADAS!
          </p>
        </div>
      </div>
    </div>
  )
}
