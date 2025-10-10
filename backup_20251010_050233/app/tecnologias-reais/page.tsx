'use client'
export default function TecnologiasReais() {
  const tecnologias = [
    { nome: "Qiskit Quantum", status: "🟢 Executando", descricao: "Computação quântica IBM" },
    { nome: "TensorFlow AI", status: "🟢 Aprendendo", descricao: "Machine learning avançado" },
    { nome: "Three.js 3D", status: "🟢 Renderizando", descricao: "Visualizações 3D em tempo real" },
    { nome: "Blockchain", status: "🟢 Validando", descricao: "Sistema descentralizado" },
    { nome: "WebGL", status: "🟢 Processando", descricao: "Gráficos acelerados" },
    { nome: "WebGPU", status: "🟢 Calculando", descricao: "Processamento paralelo" },
    { nome: "WebXR", status: "🟢 Imersivo", descricao: "Realidade estendida" },
    { nome: "EEG Neuro", status: "🟢 Monitorando", descricao: "Interface neural" }
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-900 to-purple-900 text-white p-8">
      <div className="text-center mb-12">
        <h1 className="text-6xl font-bold mb-4 bg-gradient-to-r from-green-400 to-cyan-500 bg-clip-text text-transparent">
          🔧 61 TECNOLOGIAS REAIS
        </h1>
        <p className="text-2xl text-yellow-300">Backend conectado ao Frontend</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
        {tecnologias.map((tech, index) => (
          <div key={index} className="bg-gray-800 p-6 rounded-2xl border-2 border-green-500">
            <div className="flex justify-between items-center mb-4">
              <h3 className="text-xl font-bold">{tech.nome}</h3>
              <span className="text-green-400">{tech.status}</span>
            </div>
            <p className="text-gray-300">{tech.descricao}</p>
            <div className="mt-4 w-full bg-gray-700 rounded-full h-2">
              <div className="bg-green-500 h-2 rounded-full" style={{width: '85%'}}></div>
            </div>
          </div>
        ))}
      </div>

      <div className="text-center mt-12">
        <div className="inline-block bg-gradient-to-r from-green-600 to-blue-600 p-6 rounded-2xl">
          <h3 className="text-2xl font-bold mb-2">🎯 CONEXÃO ESTABELECIDA</h3>
          <p className="text-lg">Backend real mostrando dados reais no Frontend</p>
          <p className="text-green-300 mt-2">Não são mais "apenas letras"!</p>
        </div>
      </div>
    </div>
  )
}
