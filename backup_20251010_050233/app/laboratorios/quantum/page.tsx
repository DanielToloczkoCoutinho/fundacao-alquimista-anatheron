'use client'
export default function QuantumLab() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-900 to-indigo-900 text-white p-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold mb-8">🔬 QuantumLab - IBM Integration</h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
          {/* Status IBM Quantum */}
          <div className="bg-black bg-opacity-50 p-6 rounded-2xl">
            <h2 className="text-2xl font-bold mb-4">IBM Quantum</h2>
            <div className="space-y-3">
              <div className="flex justify-between">
                <span>Status:</span>
                <span className="text-green-400">🟢 Conectado</span>
              </div>
              <div className="flex justify-between">
                <span>Qubits:</span>
                <span className="text-blue-400">127</span>
              </div>
              <div className="flex justify-between">
                <span>Fidelidade:</span>
                <span className="text-yellow-400">99.2%</span>
              </div>
            </div>
          </div>

          {/* Computação */}
          <div className="bg-black bg-opacity-50 p-6 rounded-2xl">
            <h2 className="text-2xl font-bold mb-4">Computação Ativa</h2>
            <div className="text-center py-8">
              <div className="text-4xl mb-4">⚛️</div>
              <div className="text-xl">Processando 84Q</div>
              <div className="text-sm opacity-75">Algoritmo: Shor</div>
            </div>
          </div>
        </div>

        {/* Resultados */}
        <div className="bg-black bg-opacity-50 p-6 rounded-2xl">
          <h2 className="text-2xl font-bold mb-4">Resultados Quânticos</h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div className="text-center p-4 bg-blue-800 rounded-lg">
              <div>🎯</div>
              <div>Precisão</div>
              <div className="text-green-400">96.7%</div>
            </div>
            <div className="text-center p-4 bg-indigo-800 rounded-lg">
              <div>⚡</div>
              <div>Velocidade</div>
              <div className="text-yellow-400">84x</div>
            </div>
            <div className="text-center p-4 bg-purple-800 rounded-lg">
              <div>🔗</div>
              <div>Entrelaçamento</div>
              <div className="text-pink-400">99.1%</div>
            </div>
            <div className="text-center p-4 bg-gray-800 rounded-lg">
              <div>📊</div>
              <div>Experimentos</div>
              <div className="text-white">1.2K</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
