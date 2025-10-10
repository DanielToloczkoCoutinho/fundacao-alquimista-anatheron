'use client'
export default function EnergyLab() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-green-900 to-blue-900 text-white p-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold mb-8">⚡ EnergyLab</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Painel de Controle */}
          <div className="bg-black bg-opacity-50 p-6 rounded-2xl">
            <h2 className="text-2xl font-bold mb-4">Controle de Energia</h2>
            <div className="space-y-4">
              <div className="flex justify-between">
                <span>Nível Quântico:</span>
                <span className="text-green-400">87%</span>
              </div>
              <div className="w-full bg-gray-700 rounded-full h-2">
                <div className="bg-green-500 h-2 rounded-full" style={{width: '87%'}}></div>
              </div>
            </div>
          </div>

          {/* Visualização 3D */}
          <div className="bg-black bg-opacity-50 p-6 rounded-2xl">
            <h2 className="text-2xl font-bold mb-4">Dobramento Proteico</h2>
            <div className="h-64 bg-gradient-to-br from-green-500 to-blue-500 rounded-lg flex items-center justify-center">
              <span className="text-2xl">🎮 Visualização 3D Ativa</span>
            </div>
          </div>
        </div>

        {/* Gráficos */}
        <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="bg-black bg-opacity-50 p-4 rounded-xl text-center">
            <div className="text-3xl">⚛️</div>
            <div>Partículas Ativas</div>
            <div className="text-green-400 text-2xl">1.2M</div>
          </div>
          <div className="bg-black bg-opacity-50 p-4 rounded-xl text-center">
            <div className="text-3xl">🔬</div>
            <div>Experimentos</div>
            <div className="text-blue-400 text-2xl">47</div>
          </div>
          <div className="bg-black bg-opacity-50 p-4 rounded-xl text-center">
            <div className="text-3xl">🎯</div>
            <div>Eficiência</div>
            <div className="text-yellow-400 text-2xl">94%</div>
          </div>
        </div>
      </div>
    </div>
  )
}
