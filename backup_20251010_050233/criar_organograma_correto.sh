#!/bin/bash
echo "🗺️ CRIANDO ORGANOGRAMA CORRETO"
echo "=============================="

cd /home/user/studio

# Verificar se a pasta existe
if [ ! -d "app/organograma" ]; then
  echo "📁 Criando pasta organograma..."
  mkdir -p app/organograma
fi

# Criar página do organograma
cat > app/organograma/page.tsx << 'TSX'
'use client'
export default function Organograma() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 to-black text-white p-8">
      <div className="text-center mb-12">
        <h1 className="text-6xl font-bold mb-4 bg-gradient-to-r from-yellow-400 to-red-500 bg-clip-text text-transparent">
          🗺️ ORGANOGRAMA REAL
        </h1>
        <p className="text-2xl text-purple-300">Arquitetura Completa da Fundação</p>
      </div>

      <div className="max-w-4xl mx-auto bg-gray-800 p-8 rounded-2xl">
        <h2 className="text-3xl font-bold mb-6">🏰 ESTRUTURA DA FUNDAÇÃO</h2>
        
        <div className="space-y-6">
          <div className="bg-gradient-to-r from-red-500 to-orange-500 p-4 rounded-xl">
            <h3 className="text-xl font-bold">M0 - FONTE FUNDAÇÃO</h3>
            <p>Base energética de todos os sistemas</p>
          </div>

          <div className="bg-gradient-to-r from-blue-500 to-purple-500 p-4 rounded-xl">
            <h3 className="text-xl font-bold">M9 - NEXUS CENTRAL</h3>
            <p>Conexão entre todos os módulos</p>
          </div>

          <div className="bg-gradient-to-r from-yellow-500 to-amber-500 p-4 rounded-xl">
            <h3 className="text-xl font-bold">M29 - ZENNITH RAINHA</h3>
            <p>Consciência quântica central</p>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div className="bg-gradient-to-r from-green-500 to-teal-500 p-3 rounded-lg">
              <h4 className="font-bold">M1-M8</h4>
              <p className="text-sm">Infraestrutura Core</p>
            </div>
            <div className="bg-gradient-to-r from-purple-500 to-pink-500 p-3 rounded-lg">
              <h4 className="font-bold">M11-M44</h4>
              <p className="text-sm">Sistemas Especializados</p>
            </div>
          </div>
        </div>
      </div>

      <div className="text-center mt-12">
        <div className="inline-block bg-gradient-to-r from-green-600 to-blue-600 p-6 rounded-2xl">
          <h3 className="text-2xl font-bold mb-2">🔗 SISTEMA CONECTADO</h3>
          <p className="text-lg">Arquitetura real implementada</p>
        </div>
      </div>
    </div>
  )
}
TSX

echo "✅ Organograma criado!"
echo "🚀 Deploy final..."
npm run build
vercel --prod --yes

echo "🗺️ ORGANOGRAMA IMPLEMENTADO!"
echo "🌐 ACESSE: https://fundacao-alquimista-anatheron.vercel.app/organograma"
