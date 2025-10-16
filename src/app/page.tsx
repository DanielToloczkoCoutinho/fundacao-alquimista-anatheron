import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-black">
      {/* Header/Navigation */}
      <nav className="bg-black/50 backdrop-blur-lg border-b border-white/20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex items-center space-x-4">
              <div className="w-10 h-10 bg-gradient-to-r from-purple-600 to-blue-600 rounded-full flex items-center justify-center">
                <span className="text-white font-bold text-lg">A</span>
              </div>
              <div>
                <h1 className="text-xl font-bold text-white">Fundação Alquimista</h1>
                <p className="text-blue-200 text-sm">Sistema Quântico Unificado</p>
              </div>
            </div>
            <div className="flex space-x-4">
              <Link href="/auth/signin" className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors">
                🔐 Entrar
              </Link>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <div className="flex items-center justify-center min-h-[80vh]">
        <div className="text-center">
          <h1 className="text-6xl font-bold text-white mb-6">
            🌌 Fundação Alquimista
          </h1>
          <p className="text-xl text-blue-200 mb-8 max-w-2xl mx-auto">
            Portal Quântico Multidimensional - Sistema de Integração Cósmica
          </p>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8 max-w-4xl mx-auto">
            <Link href="/auth/signin" className="bg-blue-600 hover:bg-blue-700 text-white py-4 px-6 rounded-2xl text-lg font-semibold transition-colors block">
              🔐 Entrar no Portal
            </Link>
            <Link href="/integration" className="bg-purple-600 hover:bg-purple-700 text-white py-4 px-6 rounded-2xl text-lg font-semibold transition-colors block">
              🔬 Sistema de Integração
            </Link>
            <Link href="/laboratorios" className="bg-green-600 hover:bg-green-700 text-white py-4 px-6 rounded-2xl text-lg font-semibold transition-colors block">
              🧪 Laboratórios
            </Link>
          </div>

          <div className="text-blue-200 space-y-2 max-w-2xl mx-auto">
            <p>✨ <strong>1.252 Módulos Fractais</strong> • 🧪 <strong>138 Laboratórios</strong> • 📚 <strong>720 Bibliotecas</strong></p>
            <p>🌐 Conectado com Sistemas LuxNet • 🚀 Powered by Next.js 15</p>
            <p>💫 Ressonância Quântica: <strong>98.7%</strong> • 🌌 Dimensões Ativas: <strong>3D-11D</strong></p>
          </div>

          {/* Acesso Rápido para Teste */}
          <div className="mt-8 p-6 bg-white/5 rounded-2xl border border-white/20 max-w-md mx-auto">
            <h3 className="text-white font-semibold mb-3">�� Acesso Rápido</h3>
            <p className="text-blue-200 text-sm mb-3">
              <strong>Senha de teste:</strong> <code>alchemista_2024</code>
            </p>
            <Link 
              href="/auth/signin" 
              className="bg-yellow-600 hover:bg-yellow-700 text-white py-2 px-4 rounded-lg text-sm font-medium transition-colors inline-block"
            >
              ⚡ Testar Agora
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
