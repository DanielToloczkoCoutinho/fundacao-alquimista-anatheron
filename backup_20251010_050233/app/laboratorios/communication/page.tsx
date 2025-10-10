'use client'
export default function CommunicationLab() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 to-pink-900 text-white p-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold mb-8">📡 CommunicationLab</h1>
        
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Interface Neural */}
          <div className="bg-black bg-opacity-50 p-6 rounded-2xl">
            <h2 className="text-2xl font-bold mb-4">Interface Neural</h2>
            <div className="space-y-4">
              <div className="flex items-center space-x-4">
                <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
                <span>Conexão Estável</span>
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div className="text-center p-4 bg-purple-800 rounded-lg">
                  <div className="text-2xl">🧠</div>
                  <div>Neurônios</div>
                  <div className="text-xl">86B</div>
                </div>
                <div className="text-center p-4 bg-pink-800 rounded-lg">
                  <div className="text-2xl">⚡</div>
                  <div>Latência</div>
                  <div className="text-xl">3ms</div>
                </div>
              </div>
            </div>
          </div>

          {/* Chat Quântico */}
          <div className="bg-black bg-opacity-50 p-6 rounded-2xl">
            <h2 className="text-2xl font-bold mb-4">Chat Quântico</h2>
            <div className="h-48 bg-gradient-to-br from-purple-500 to-pink-500 rounded-lg p-4">
              <div className="text-center mt-12">
                <div className="text-2xl mb-2">💬</div>
                <div>Conexão Quântica Ativa</div>
                <div className="text-sm opacity-75">Entrelaçamento: 99.7%</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
