'use client'
export default function BlockchainDashboard() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-orange-900 to-red-900 text-white p-8">
      <div className="text-center mb-12">
        <h1 className="text-6xl font-bold mb-4 bg-gradient-to-r from-yellow-400 to-red-500 bg-clip-text text-transparent">
          ⛓️ DASHBOARD BLOCKCHAIN
        </h1>
        <p className="text-2xl text-yellow-300">5 Sistemas Blockchain + Web3</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
        <div className="bg-gradient-to-br from-yellow-500 to-orange-500 p-6 rounded-2xl text-center">
          <div className="text-4xl font-bold">5</div>
          <div className="text-lg">Blockchains</div>
          <div className="text-sm opacity-75">Sistemas Ativos</div>
        </div>

        <div className="bg-gradient-to-br from-green-500 to-teal-500 p-6 rounded-2xl text-center">
          <div className="text-4xl font-bold">1</div>
          <div className="text-lg">Web3</div>
          <div className="text-sm opacity-75">DApps</div>
        </div>

        <div className="bg-gradient-to-br from-purple-500 to-pink-500 p-6 rounded-2xl text-center">
          <div className="text-4xl font-bold">∞</div>
          <div className="text-lg">Transações</div>
          <div className="text-sm opacity-75">Imutáveis</div>
        </div>
      </div>

      {/* DADOS DA BLOCKCHAIN */}
      <div className="bg-gray-800 p-8 rounded-2xl mb-8">
        <h2 className="text-3xl font-bold mb-6 text-center">🔐 DADOS DISTRIBUÍDOS</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div>
            <h3 className="text-xl font-bold mb-4">📊 Estatísticas da Rede</h3>
            <div className="space-y-3">
              <div className="flex justify-between">
                <span>Blocos Validados:</span>
                <span className="text-green-400">12,847</span>
              </div>
              <div className="flex justify-between">
                <span>Hash Rate:</span>
                <span className="text-green-400">284 TH/s</span>
              </div>
              <div className="flex justify-between">
                <span>Transações:</span>
                <span className="text-green-400">8.2K</span>
              </div>
            </div>
          </div>

          <div>
            <h3 className="text-xl font-bold mb-4">🛡️ Segurança</h3>
            <div className="space-y-3">
              <div className="flex justify-between">
                <span>Consenso:</span>
                <span className="text-green-400">Proof of Stake</span>
              </div>
              <div className="flex justify-between">
                <span>Criptografia:</span>
                <span className="text-green-400">AES-512</span>
              </div>
              <div className="flex justify-between">
                <span>Validação:</span>
                <span className="text-green-400">Multi-assinatura</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="text-center">
        <div className="inline-block bg-gradient-to-r from-yellow-600 to-red-600 p-8 rounded-2xl border-4 border-yellow-400">
          <h3 className="text-3xl font-bold mb-4">⛓️ SISTEMA DESCENTRALIZADO</h3>
          <p className="text-xl">5 blockchains operando em consenso</p>
          <p className="text-yellow-300 mt-4 text-2xl font-bold">
            DADOS IMUTÁVEIS E VERIFICÁVEIS!
          </p>
        </div>
      </div>
    </div>
  )
}
